# RAG with LangChain, OpenAI and ChromaDB

This project implements a simple **Retrieval-Augmented Generation (RAG)** pipeline using [LangChain](https://www.langchain.com/), [OpenAI](https://openai.com/), and [ChromaDB](https://www.trychroma.com/).  

It allows you to upload PDF documents, vectorize them into a database, and then ask natural language questions to retrieve context-aware answers from the AI model.

---

## 📂 Project Structure

.
├── base/ # Folder containing your PDF documents (e.g., "The Little Prince")
├── db/ # Persistent ChromaDB database generated from PDFs
├── create_db.py # Script to load, chunk, and vectorize documents
├── main.py # Script to query the RAG system
├── .env # Environment variables (OpenAI API key)
├── requirements.txt # Project dependencies
└── README.md # Documentation

---

## ⚙️ Requirements

Install dependencies with:

pip install -r requirements.txt

## 🚀 Usage
1. Set up your environment
Modify the .env file with your OpenAI API key:

2. Add documents
Place your PDF files inside the base/ folder.
Example: base/the_little_prince.pdf

3. Create the database
Run the script to load, split, and vectorize your documents:

python create_db.py
This will generate a persistent ChromaDB database inside the db/ folder.

4. Query the system
Run the main script to ask questions about your documents:

python main.py

Type your question when prompted, and the AI will return an answer based on the indexed documents.

## 🧠 How it Works
Document Loading → PDFs are loaded from the base/ folder.

Chunking → Text is split into chunks (2000 characters, 500 overlap).

Embedding → Each chunk is vectorized with OpenAI embeddings.

Storage → Embeddings are stored in ChromaDB (db/).

Retrieval → At query time, the most relevant chunks are retrieved.

Generation → The AI model answers the question using both context and the prompt.

## 📖 Example
Input question:

Write your question: What is the main message of The Little Prince?

Output:

AI answer: The story emphasizes the value of love, friendship, and seeing with the heart rather than with the eyes.

📜 License
This project was developed for educational and portfolio purposes.
All PDF examples (like The Little Prince) are included only for demonstration.

👤 Author
Developed by Victor Souza.