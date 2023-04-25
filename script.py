import pandas as pd
import opendatasets as od
import zipfile, os
from pathlib import Path
import dotenv
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


def extract_from_url(url) -> Path:
    """Extract data from url"""

    # path to zip file
    path = './data/'

    # download data
    # od.download(url, path)

    # specify the path of the zip file to be extracted
    zip_path = f'{path}PUB150.ZIP'

    # specify the path to extract the zip file
    extract_data = './extracted_data/'

    # create a ZipFile object
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # extract all contents of the zip file to a specified directory
        zip_ref.extractall(extract_data)
    return Path(extract_data)

def extract_from_access_db(path: Path) -> None:
    """Read all tables in the database into a DataFrame"""

    # Iterate over each csv file in the folder 
    for file in  os.listdir(path):
        if file.endswith('.csv'):

            # Path to the csv file
            new_path = f'{path}/{file}'

            # Read the file into a pandas DataFrane
            df = pd.read_csv(new_path)

            # Get the database connection
            engine = get_database_conn()

            # Write the file to postgres
            df.to_sql(file[:-4], con=engine, if_exists='replace', index=False)
            print(f'{file} successfully written to database')
    print('All files written to database')




def main():
    url = 'https://drive.google.com/file/d/1VyCGCAfFuEK7vB1C9Vq8iPdgBdu-LDM4/view'
    path = extract_from_url(url)
    extract_from_access_db(path)


if __name__ == '__main__':
    main()