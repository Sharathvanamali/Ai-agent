Here’s a professional **GitHub README.md** for your project.

You can copy-paste this directly into your repository.

---

# 🪙 Gold Price RAG Assistant

A Streamlit-based AI assistant that answers questions about historical and current gold prices using a structured Excel dataset and LLM-powered response generation.

This project uses:

* 📊 Excel (Gold.xlsx) as the data source
* 🧠 Ollama LLM (Gemma model)
* 🔍 Structured Retrieval (RAG-style filtering)
* 🎨 Streamlit UI

---

## 🚀 Features

* Ask questions about historical gold prices
* Fetch the latest/current gold rate from Excel
* Retrieve specific date-based records
* Strict factual responses (no hallucination)
* Clean conversational UI with chat history
* Fast local inference using Ollama

---

## 🏗️ Architecture

Gold.xlsx → Pandas Filtering → Structured Context → LLM Formatting → Streamlit UI

Unlike traditional embedding-based RAG systems, this project uses structured retrieval because financial time-series data requires exact matching rather than semantic similarity.

---

## 📁 Project Structure

```
├── main.py          # Streamlit app
├── vector.py        # Custom Excel-based retriever
├── Gold.xlsx        # Gold price dataset
├── chroma_db/       # (Optional if using embeddings)
└── README.md
```

---

## 🛠️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/gold-price-rag.git
cd gold-price-rag
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a requirements file, install manually:

```bash
pip install streamlit pandas langchain langchain-core langchain-ollama openpyxl
```

---

### 4️⃣ Install Ollama

Download and install Ollama from:

👉 [https://ollama.com](https://ollama.com)

Pull required models:

```bash
ollama pull gemma3
ollama pull mxbai-embed-large
```

---

## ▶️ Running the App

```bash
streamlit run main.py
```

App will open in your browser at:

```
http://localhost:8501
```

---

## 💬 Example Questions

* What is the current gold price?
* What was gold price on 2024-01-15?
* Show latest close price.
* What was the highest price in 2023?

---

## 🔍 Why Not Use Embedding-Based RAG?

Gold price data is:

* Structured
* Numeric
* Date-driven

Vector similarity search is inefficient for exact numeric queries.

Instead, this project uses:

✔ Pandas filtering
✔ Deterministic retrieval
✔ LLM only for formatting

This eliminates hallucinations and improves accuracy.

---

## ⚙️ Configuration

Update the Excel file path inside `vector.py`:

```python
XLSX_FILE = r"C:\path\to\Gold.xlsx"
```

Ensure your Excel file contains these columns:

* Date
* Open
* High
* Low
* Close
* Volume

---

## 📦 Requirements

* Python 3.9+
* Ollama installed locally
* Gold.xlsx dataset
* Streamlit

---

## 🧠 Tech Stack

* Python
* Streamlit
* Pandas
* LangChain
* Ollama LLM (Gemma)
* OpenPyXL

---

## 📈 Future Improvements

* Live gold API integration
* SQL-based backend
* Daily auto-update system
* Trend analysis
* Charts & visualization
* Deployment on cloud server

---

## 🏆 Production Note

For production-grade systems:

* Replace Excel with SQLite or PostgreSQL
* Add API layer (FastAPI)
* Containerize with Docker
* Deploy on cloud (AWS/GCP/Azure)

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Built as a structured RAG financial assistant project.

---


