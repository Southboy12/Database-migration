import pandas as pd
import dotenv, os
from sqlalchemy import create_engine




"""
Question 1

Which country has the largest number of ports with a cargo_wharf? Your answer should
include the columns country and port_count only.

"""


def get_database_conn():
    """Credentials to connect to the database"""

    dotenv.load_dotenv('./.env')
    db_user_name = os.getenv('DB_USER_NAME')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')
    port = os.getenv('DB_PORT')
    host = os.getenv('DB_HOST')
    return create_engine(f'postgresql://{db_user_name}:{db_password}@{host}:{port}/{db_name}')


def answer2():
    conn =get_database_conn()
    query = """
        
    """

    data = pd.read_sql(query, con=conn)
    print(data.head())
    


def main():
    answer2()


if __name__ == '__main__':
    main()