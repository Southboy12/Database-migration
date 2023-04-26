import pandas as pd
from util import get_database_conn




"""
Question 1

Which country has the largest number of ports with a cargo_wharf? Your answer should
include the columns country and port_count only.

"""


def answer2():
    conn =get_database_conn()
    query = """
    SELECT 
	"Country Name", COUNT("MAIN_PORT_NAME") AS Number_of_Ports
    FROM
        "WPI Import" I 
    JOIN 
        "Country Codes" S
    ON 
        I."WPI_COUNTRY_CODE"=S."Country Code"
    WHERE 
        "LOAD_OFFLOAD_WHARVES" = 'Y'
    GROUP BY
        1
    ORDER BY
        2 DESC;
    """

    data = pd.read_sql(query, con=conn)
    largest_port = data.head(1)
    print(largest_port)

    # Write to postgres
    largest_port.to_sql('largest_port', con=conn, if_exists='replace', index=False)

    print('Largest_port written to postgres')
    


def main():
    answer2()


if __name__ == '__main__':
    main()