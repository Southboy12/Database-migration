import pandas as pd
import dotenv, os
from sqlalchemy import create_engine




"""
Question 1

What are the 5 nearest ports to Singapore's JURONG ISLAND port? (country = 'SG',
port_name = 'JURONG ISLAND').Your answer should include the columns port_name and
distance_in_meters only.

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


# """SELECT
#     port_name,
#     port_latitude,
#     port_longitude,
#     earth_distance(
#         ll_to_earth(port_latitude, port_longitude),
#         ll_to_earth(1.2667, 103.7333)
#     ) AS distance
# FROM
#     ports
# ORDER BY
#     distance ASC
# LIMIT
#     5;"""


# "MAIN_PORT_NAME",
#         earth_distance(
#             ll_to_earth(latitude_degrees, longitude_degrees),
#             ll_to_earth(1.283333, 103.733333)
#             ) AS distance

def answer1():
    conn =get_database_conn()
    query = """
    SELECT 
        "MAIN_PORT_NAME", 
        ST_Distance_Sphere(
            ST_MakePoint(103.733333, 1.283333),
            ST_MakePoint(64, 67)
        ) AS distance   
    FROM
        (select 
            *,
            CASE 
                WHEN "LATITUDE_HEMISPHERE"= 'N' THEN "LATITUDE_DEGREES" + ("LATITUDE_MINUTES" / 60.0)
                WHEN "LATITUDE_HEMISPHERE" = 'S' THEN -1.0 * ("LATITUDE_DEGREES" + ("LATITUDE_MINUTES" / 60.0))
            END AS latitude_degrees,
            CASE 
                WHEN "LONGITUDE_HEMISPHERE" = 'E' THEN "LONGITUDE_DEGREES" + "LONGITUDE_MINUTES"/60.0
            WHEN "LONGITUDE_HEMISPHERE" = 'W' THEN -1*("LONGITUDE_DEGREES" + "LONGITUDE_MINUTES"/60.0)
            END AS longitude_degrees
        from 
            "WPI Import") AS data_with_degrees;
    """

    data = pd.read_sql(query, con=conn)
    print(data.head())
    


def main():
    answer1()


if __name__ == '__main__':
    main()