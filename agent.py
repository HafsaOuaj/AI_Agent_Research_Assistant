from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
import os
from tools import search_tool,wikipedia_tool,save_tool  # Import the tools you created

# Load environment variables from .env file
load_dotenv()

tools=[search_tool,wikipedia_tool,save_tool]
# Define the model output structure using Pydantic
class ResearchAssistantOutput(BaseModel):
    topic: str
    summary: str
    references: list[str]
    tools_used: list[str]

# Initialize the LangChain ChatOpenAI model (not OpenAI's raw SDK)
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")  # Load API key from .env for security
)

# Define the parser for structured output
parser = PydanticOutputParser(pydantic_object=ResearchAssistantOutput)

# Create a chat prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a research assistant. You will be given a topic and will provide a summary, "
        "references, and tools used to research the topic. "
        "Wrap the output in the format below:\n{formatted_instructions}"
    ),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")
]).partial(formatted_instructions=parser.get_format_instructions())

# Create the agent
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,  # You can pass tools here later if needed
    prompt=prompt
)

# Create the executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)
query= input("Enter your query: ")
# Invoke the agent
print(query)
response = agent_executor.invoke({
    "query": query,
})

# Output the raw response
print("Raw response:\n", response)

# Parse structured output (if it's correctly returned)
try:
    structured_response = parser.parse(response.get("output"))
    print("\nStructured response:\n", structured_response)
except Exception as e:
    print("\nFailed to parse output:\n", e)


