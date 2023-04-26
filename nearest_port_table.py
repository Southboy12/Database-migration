import pandas as pd
from util import get_database_conn, distance



"""
Question 1

What are the 5 nearest ports to Singapore's JURONG ISLAND port? (country = 'SG',
port_name = 'JURONG ISLAND').Your answer should include the columns port_name and
distance_in_meters only.

"""

def answer1():
    conn =get_database_conn()
    query = """
    SELECT * FROM "WPI Import"
    """

    distances = []
    data = pd.read_sql(query, con=conn)
    for index, row in data.iterrows():
        if row['MAIN_PORT_NAME'] != 'JURONG ISLAND':  # Skip calculating the distance to itself
            distance_to_JI = distance(data.loc[data['MAIN_PORT_NAME'] == 'JURONG ISLAND']['LATITUDE_DEGREES'].iloc[0],
                                    data.loc[data['MAIN_PORT_NAME'] == 'JURONG ISLAND']['LONGITUDE_DEGREES'].iloc[0],
                                    row['LATITUDE_DEGREES'],
                                    row['LONGITUDE_DEGREES'])
            distances.append(distance_to_JI)
        else:
            distances.append(0)  # Set distance to itself as 0
        
    # Add the distances as a new column to the data table
    data['distance_to_JI'] = distances

    # 
    data.sort_values(by='distance_to_JI', inplace=True)

    # Print out the resulting table
    data_sorted = data[['MAIN_PORT_NAME', 'distance_to_JI']].head(6)

    print(data_sorted)

    # Write data to database
    data_sorted.to_sql('nearest_port_table', con=conn, if_exists='replace', index=False)

    print('Top_5_nearest_ports data successfully written to postgres')



def main():
    answer1()


if __name__ == '__main__':
    main()