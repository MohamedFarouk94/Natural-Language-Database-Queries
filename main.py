from query_chain import get_chain
from database import get_connection

if __name__ == "__main__":
    conn = get_connection()
    chain = get_chain(conn)
    result = chain.invoke(None)
    print("\nFinal Result:")
    print(result)
