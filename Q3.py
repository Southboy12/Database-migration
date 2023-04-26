import pandas as pd
from util import get_database_conn, distance



"""

Question 3

You receive a distress call from the middle of the North Atlantic Ocean. The person on the
line gave you a coordinates of lat: 32.610982, long: -38.706256 and asked for the nearest port
with provisions, water, fuel_oil and diesel. Your answer should include the columns country,
port_name, port_latitude and port_longitude only.

"""



def answer3():
    print('testing')
    conn =get_database_conn()
    query = """
    SELECT 
        * 
    FROM 
        "WPI Import" I
    JOIN 
        "Country Codes" S
    ON
        I."WPI_COUNTRY_CODE"=S."Country Code"
    WHERE
        "SUPPLIES_PROVISIONS"='Y' AND "SUPPLIES_WATER"='Y' AND "SUPPLIES_FUEL_OIL"='Y' AND "SUPPLIES_DIESEL_OIL"='Y'
    """

    data = pd.read_sql(query, con=conn)
    
    distances = []
    for index, row in data.iterrows():
        distance_to_location = distance(32.610982,
                                -38.706256,
                                row['LATITUDE_DEGREES'],
                                row['LONGITUDE_DEGREES'])
        distances.append(distance_to_location)
        
    # Add the distances as a new column to the data table
    data['distance_to_location'] = distances
    data.sort_values(by='distance_to_location', ascending=True, inplace=True)

    sorted_data = data[['Country Name', 'MAIN_PORT_NAME', 'LATITUDE_DEGREES', 'LONGITUDE_DEGREES']].head(1)
    
    sorted_data.to_sql('nearest_port_with_resources', con=conn, if_exists='replace', index=False)

    print('Sorted_data written to postgres')
    # # Print out the resulting table
    # data_sorted = data[['MAIN_PORT_NAME', 'distance_to_JI']].head(6)

    # # Write data to database
    # data_sorted.to_sql('top_5_nearest_ports', con=conn, if_exists='replace', index=False)

    # print('Top_5_nearest_ports data successfully written to postgres')


def main():
    answer3()


if __name__ == '__main__':
    main()