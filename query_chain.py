import pandas as pd
import warnings
from time import time
from langchain_core.runnables import RunnableLambda

from database import get_response

warnings.filterwarnings("ignore", category=UserWarning, message=".*only supports SQLAlchemy connectable.*")

def generate_sql_(question):
    print("\nGenerating SQL...")
    before = time()
    response = get_response(question)
    time_taken = time() - before
    print("Your generated SQL is ready.")
    print(f"Time Taken: {time_taken:.2f}s")
    print(f"\nGenerated SQL:\n{response}")
    return response

def run_query_(conn, query):
    print("\nExecuting SQL...")
    try:
        before = time()
        df = pd.read_sql_query(query, conn)
        time_taken = time() - before
        print(f"Time Taken: {time_taken:.2f}s")
        print("SQL was executed successfully and your data is ready!\n")
        return df
    except Exception as e:
        print(f"Error running query: {e}\n")
        return pd.DataFrame()

def get_chain(conn):
    get_input = RunnableLambda(lambda _: input("Ask a question to generate a SQL: "))
    generate_sql = RunnableLambda(generate_sql_)
    run_query = RunnableLambda(lambda query: run_query_(conn, query))

    return get_input | generate_sql | run_query
