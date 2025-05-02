# 🧠 Research Assistant Agent (LangChain + OpenAI + Tools)

This project is an intelligent research assistant built using **LangChain**, **OpenAI's GPT-3.5**, and custom tools for web search, Wikipedia queries, and file-saving. The agent takes a natural language query and returns a structured research summary with references and tools used.

---

## 🚀 Features

- 🔍 **Web Search** via DuckDuckGo
- 📚 **Wikipedia Lookup** using LangChain wrapper
- 💾 **Save Output to File** with timestamp
- 🧠 Powered by `gpt-3.5-turbo` using LangChain agent interface
- 📦 Easily deployable as an API or GUI

---

## 🛠️ Requirements

- Python 3.10+
- OpenAI API key
- Virtual environment (recommended)

Install dependencies:

```bash
pip install -r requirements.txt
````

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 📁 Project Structure

```
.
├── agent.py              # Main agent logic
├── tools.py              # Tool definitions (web search, Wikipedia, save to file)
├── .env                  # Contains your OpenAI API key
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 💡 Example Query

```bash
Enter your query: Impact of climate change on agriculture
```

### ✅ Output (Structure)

```json
{
  "topic": "Impact of climate change on agriculture",
  "summary": "...",
  "references": ["https://..."],
  "tools_used": ["DuckDuckGo Search", "Wikipedia"]
}
```

---


## 🐳 Docker 

Build and run:

```bash
docker build -t research-agent .
docker run -p 8000:8000 research-agent
```

---

## 📌 Tools Used

* [LangChain](https://python.langchain.com)
* [OpenAI GPT-3.5](https://platform.openai.com/)
* [DuckDuckGo Search API](https://pypi.org/project/duckduckgo-search/)
* [Wikipedia API Wrapper](https://python.langchain.com/docs/integrations/tools/wikipedia)

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Hafsa Ouajdi**
[GitHub](https://github.com/HafsaOuajdi) | [Portfolio](https://hafsaouaj.github.io/Portfolio_Hafsa/) | [LinkedIn](https://www.linkedin.com/in/hafsaouajdi)

---
