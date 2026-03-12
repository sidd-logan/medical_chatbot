# MediChat Pro

A Streamlit-based application that allows users to upload medical PDF documents, process them into a searchable vector store, and interact with the content via an AI-powered chat interface. The backend uses EuriAI's chat model through the `euriai` package and LangChain utilities for embeddings and FAISS for vector storage.

---

## 🚀 Features

- Upload one or more medical PDF documents through a simple UI.
- Extract text from PDFs and split it into manageable chunks.
- Embed chunks using sentence-transformers and store them in a FAISS index.
- Retrieve relevant passages and generate answers using an LLM.
- Chat-style interface with history and timestamping.
- Configurable with environment variables (API key).

---

## 🛠️ Prerequisites

- Python 3.11 or later
- An [Euri](https://euriai.com) API key (set in `EURI_API_KEY` environment variable)

---

## 📁 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sidd-logan/medical_chatbot.git
   cd medical_chatbot
   ```
2. Create a virtual environment and activate it:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file or export the API key directly:
   ```bash
   echo "EURI_API_KEY=your_key_here" > .env
   ```
   or set the environment variable in your shell/OS.

---

## 🎯 Usage

Run the Streamlit app from the project root:

```bash
streamlit run main.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`).

1. Upload your medical PDF(s) using the sidebar.
2. Click **Process Documents** to extract, split, and index the text.
3. Enter questions in the chat box to query the documents.

The assistant will respond based on the content of your uploaded files.

---

## 🧩 Project Structure

```
├── main.py                # Streamlit application entry point
├── requirements.txt       # Python dependencies
├── app/
│   ├── chat_utils.py      # Wrapper around EuriAI chat model
│   ├── config.py          # API key configuration
│   ├── pdf_utils.py       # PDF text extraction helper
│   ├── ui.py              # Streamlit UI components (uploader)
│   └── vectorstore_utils.py  # FAISS index creation & querying
└── sample_data/           # (optional) example PDFs
```

---

## 🧠 How It Works

1. **PDF Upload**: Users upload PDF files via Streamlit's `file_uploader`.
2. **Text Extraction**: `pdf_utils.extract_text_from_pdf` reads pages with `pypdf`.
3. **Chunking**: Text is split using `RecursiveCharacterTextSplitter`.
4. **Embedding & Indexing**: Chunks are embedded with `sentence-transformers` and stored in a FAISS index using `langchain_community`.
5. **Chat**: When a question is asked, similar documents are retrieved and sent as context to the Euri chat model.

---

## 📦 Dependencies

See `requirements.txt` for the full list. Key packages include:

- `streamlit` – web UI
- `pypdf` – PDF parsing
- `faiss-cpu` – vector store
- `langchain`, `langchain_community` – LLM utilities
- `sentence-transformers` – embeddings
- `euriai` – LLM client

---

## ⚠️ Notes

- Keep your API key secure; do not commit it to source control.
- This project is a prototype; consider adding error handling, rate-limit management, and more robust UI for production.

---

## 📄 License

This project is provided "as-is" with no warranty. Modify and use at your own risk.

---

Happy chatting with your medical documents! 🏥🤖