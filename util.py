import math, os, dotenv
from sqlalchemy import create_engine


def get_database_conn():
    """Credentials to connect to the database"""

    dotenv.load_dotenv('./.env')
    db_user_name = os.getenv('DB_USER_NAME')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')
    port = os.getenv('DB_PORT')
    host = os.getenv('DB_HOST')
    return create_engine(f'postgresql://{db_user_name}:{db_password}@{host}:{port}/{db_name}')



def distance(lat1, lon1, lat2, lon2):
    R = 6371  # radius of the Earth in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c * 1000
