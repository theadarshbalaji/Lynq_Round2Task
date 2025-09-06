# Weather + PDF Analyzer + LLM Demo

This repository contains three main components:  
1. **Weather MCP Server + Client** – A server exposing weather data via OpenWeather API and a chatbot client.  
2. **PDF Analyzer** – A script to extract and analyze text, metadata, and statistics from a PDF.  
3. **LLM Demo** – A sample script calling OpenAI's GPT model.

---

## 📂 Project Structure

```
├── weather_mcp.py      # MCP server to provide weather info using OpenWeather API
├── client_agent.py     # Chatbot client that queries the weather server
├── pdf_reader.py       # Script to analyze and extract info from a PDF
├── llm_call.py         # Example script calling OpenAI GPT models
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🌦️ Weather MCP Server & Client

### 1. Start the MCP Weather Server
The server is implemented in `weather_mcp.py` and uses **OpenWeather API**.

- Open `weather_mcp.py` and replace the placeholder `API_KEY` with your OpenWeather key.
- Run the server:
  ```bash
  python weather_mcp.py
  ```
- By default, it runs on `http://127.0.0.1:8000/mcp`.

### 2. Run the Weather Client
The chatbot client (`client_agent.py`) connects to the running server.

```bash
python client_agent.py
```

You can then type queries like:

**Sample Input/Output**
```
You: Is it raining in Hyderabad today?
AI: According to the weather API, it's clear sky, 30°C in Hyderabad.

You: What's the temperature in Delhi?
AI: According to the weather API, it's haze, 28°C in Delhi.

You: exit
Goodbye!
```

---

## 📄 PDF Analyzer

The `pdf_reader.py` script analyzes a PDF (default: `timetable.pdf`).

It reports:
- Page count  
- Metadata  
- Keyword search (`CS F111` by default)  
- Document statistics (characters, words, lines)  
- Most common characters  
- Instructor mentions  

### Run:
```bash
python pdf_reader.py
```

**Sample Output:**
```
PDF Analysis Report

Total pages: 12

PDF Metadata
/Author: Admin
/Title: University Timetable
/Producer: PDF Generator

Keyword 'CS F111' found on page(s): [2, 5, 7]

Document Statistics
Total characters: 45231
Total words: 7234
Total lines: 642

Most Common Characters
' ': 6543
'e': 3456
't': 2789

Instructor Mentions
Rohit Gupta: 3
Kurra Suresh: 5
Aruna Malapati: 2

Analysis complete
```

---

## 🤖 LLM Demo

The `llm_call.py` script demonstrates calling an OpenAI LLM.

1. Replace `"your-api-key-here"` with your actual **OpenAI API key**.
2. Run:
   ```bash
   python llm_call.py
   ```

**Sample Output:**
```
LLM Response: The capital of Japan is Tokyo.
```

---

## 📦 Requirements

Dependencies are listed in `requirements.txt`:

```
fastmcp>=0.1.11
requests>=2.31.0
```

Additionally, `pdf_reader.py` requires:
- `pypdf`

And `llm_call.py` requires:
- `openai`

Install them manually if needed:
```bash
pip install pypdf openai
```

---

## 🚀 Future Improvements
- Add unit tests for each module.  
- Enhance PDF analyzer with visualization.  
- Expand chatbot to handle more intents beyond weather.  

---

## 🖼️ Project Preview
![Project Screenshot](a2a06157-5935-4630-9b9f-b5fe0db90047.png)

---

## 📝 License
This project is for learning/demo purposes. Modify and use freely.
