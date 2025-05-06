import psycopg2

def connect_to_db(db_config: dict) -> psycopg2.extensions.connection:
    """Connect to the PostgreSQL database using the provided configuration."""
    try:
        conn = psycopg2.connect(
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port']
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
