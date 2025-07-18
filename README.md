# Natural-Language Database Query System

A minimal terminal-based interface that lets you type natural-language database queries and get the desired data using an integrated system involving an optimized language model.

This repo is the clean inference version of the full project, which was designed, fine-tuned, and optimized on Kaggle:  
🔗 [AI-Powered PostgreSQL – Kaggle Notebook](https://www.kaggle.com/code/mohamedfarouk94/ai-powered-postgresql?scriptVersionId=237714324)

---

## 🚀 What Was Done in the Project

- Built a simple customer/order/review/product schema in PostgreSQL
- Fine-tuned a Text-to-SQL model using LoRA and quantization (5GB → 850MB)
- Used LangChain’s Runnable logic to convert natural language into executable SQL
- Run SQL queries on a live PostgreSQL connection and returned answers

---

## 🧠 Technologies Used

- `transformers`, `peft`, `trl`, `datasets`, `bitsandbytes`
- PostgreSQL hosted via Supabase
- Model inference via Hugging Face Transformers
- LangChain for chaining input → model → SQL execution

---

## 🛠 Setup

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. **Update your DB credentials** in `database.py`:

```python
db_url = "postgresql://username:password@localhost:5432/your_database"
```

3. **Add your model and tokenizer** to:

```
models/model/
models/tokenizer/
```

4. **Run the app**:

```bash
python main.py
```

---

## 📁 Folder Structure

```
text-to-sql-chat/
│
├── models/
│   ├── model/        # Optimized model files (850MB)
│   └── tokenizer/    # Tokenizer files
│
├── main.py           # Entry point script
├── query_chain.py    # LangChain Runnable chain
├── database.py       # DB connection and model loading
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📓 Notebook Highlights

- PostgreSQL database was built from scratch with customer, order, and product tables.
- Data was randomly generated using Faker.
- A Text-to-SQL model was fine-tuned using LoRA and then compressed.
- The model was evaluated using several quantization methods and response quality was measured.
- Integration was tested with LangChain to provide a full natural language → SQL → DataFrame pipeline.

---

## 📌 Note

This repository is **only for inference**. The full training and optimization pipeline is documented in the Kaggle notebook linked above.
