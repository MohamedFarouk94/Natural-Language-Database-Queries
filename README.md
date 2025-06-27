# Text-to-SQL Chat (Terminal Interface)

A minimal terminal-based interface that lets you ask natural language questions and get SQL-generated answers using an optimized language model.

This repo is the inference interface of the full project, originally built and optimized in a Kaggle notebook:  
🔗 [AI-Powered PostgreSQL – Kaggle Notebook](https://www.kaggle.com/code/mohamedfarouk94/ai-powered-postgresql?scriptVersionId=237714324)

---

## 🚀 Features

- Ask a question in plain English
- Translates it into an SQL query using a fine-tuned model
- Executes the SQL on a PostgreSQL database
- Displays results as a Pandas DataFrame

---

## 🛠 Setup

1. **Clone the repository** and install dependencies:

```bash
pip install -r requirements.txt
```

2. **Update your database credentials** in `database.py`:

```python
db_url = "postgresql://username:password@localhost:5432/your_database"
```

3. **Place your model and tokenizer in the following folders:**

```
models/model/
models/tokenizer/
```

4. **Run the app:**

```bash
python main.py
```

---

## 📁 Folder Structure

```
text-to-sql-chat/
│
├── models/
│   ├── model/        # Your optimized model files
│   └── tokenizer/    # Tokenizer files
│
├── main.py           # Entry point
├── query_chain.py    # LangChain chain definition
├── database.py       # Model + database connection logic
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ℹ️ Notes

- The original model was optimized from 5GB to 850MB with extensive tuning.
- This repo is intentionally simple and clean, focused purely on the **inference pipeline**.
