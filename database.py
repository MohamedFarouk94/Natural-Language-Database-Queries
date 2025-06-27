import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import psycopg2
from sqlalchemy import create_engine

model_path = "models/model"
tokenizer_path = "models/tokenizer"

model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

# Add your actual database schema here
schema = ""

def get_response(question):
    prompt = f'Database Schema: {schema}\n Question: {question} \n ANSWER WITH ONLY SQL\n'
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=500, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response[len(prompt):] 
    

def get_connection():
    # Update this with your actual PostgreSQL credentials
    db_url = "postgresql://username:password@localhost:5432/your_database"
    engine = create_engine(db_url)
    return engine.connect()
