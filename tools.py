from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

# Web search tool
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="duckduckgo_search",  
    func=search.run,
    description="Useful for searching the web. Input should be a search query.",
)

# Wikipedia tool
api_wrapper = WikipediaAPIWrapper(top_k_results=5, doc_content_char_limit=1000)
wikipedia_tool = Tool(
    name="wikipedia_query",  
    func=WikipediaQueryRun(api_wrapper=api_wrapper).run,
    description="Use this tool to look up information on Wikipedia. Input should be a search query.",
)

# Save tool
def save_to_file(data: str, filename: str = "output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"{timestamp} - {data}\n")
    print(f"Data saved to {filename}")

save_tool = Tool(
    name="save_to_file",  
    func=save_to_file,
    description="Saves the data to a file with a timestamp. Input should be a string.",
)
