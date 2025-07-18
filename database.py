from sqlalchemy import create_engine


def get_connection():
    # Update this with your actual PostgreSQL credentials
    db_url = "postgresql://username:password@localhost:5432/your_database"
    engine = create_engine(db_url)
    return engine.connect()

