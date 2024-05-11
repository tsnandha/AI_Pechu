RAG POC Setup

1. Download codebase from RAG folder
2. Download Ollama from the website https://ollama.com/ and install it
3. Open PowerShell and run the following commands to pull models and run Ollama
	ollama pull nomic-embed-text
	ollama pull mistral
	ollama run llama2
4. Add a new file or use existing file in the data folder
5. Install the following packages
	pip install pypdf, langchain, chromadb, pytest, tkinter
6. Add a new file in data folder or use existing file
7. Run populate_database.py (embeds and adds docs to vector DB)
8. Run app.py and enter question (since it is local llama, it takes lot of time for response)



![image](https://github.com/tsnandha/AI_Pechu/assets/91715044/c1a4ad64-7124-4b46-9c6e-871d2059ea46)
