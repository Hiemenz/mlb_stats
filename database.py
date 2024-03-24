        
from sshtunnel import SSHTunnelForwarder
import psycopg2
import yaml 



with open('config.yaml', 'r') as file:
    # The FullLoader parameter is optional and can be omitted in most cases
    data = yaml.safe_load(file)
    
    # SSH tunnel parameters
    SSH_HOST = data.get('ssh_host')
    SSH_USERNAME = data.get('ssh_user_name')
    SSH_PASSWORD = data.get('ssh_password')
    REMOTE_DB_IP = data.get('remote_db_ip')
    REMOTE_DB_PORT = data.get('remote_db_port')

    # Database connection parameters
    DB_NAME = data.get('db_name')
    DB_USER =  data.get('db_user')
    DB_PASSWORD =  data.get('db_password')


def run_query(conn, query):
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT version();")
    
        version = cursor.fetchone()
        print(f"Database version: {version}")   
            
            
            
def execute_query(conn, query, data=None, fetch=False):
    """
    Execute a SQL query on the PostgreSQL database.

    Parameters:
    - conn: The database connection object.
    - query: The SQL query string to execute.
    - data: Optional tuple of data to pass to the query, for parameterized queries.
    - fetch: Boolean indicating whether to fetch and return the query results.

    Returns:
    - If fetch is True, returns the result of the query.
    - Otherwise, returns None.
    """
    result = None
    try:
        # Create a new cursor
        cur = conn.cursor()

        # Execute the query
        if data:
            cur.execute(query, data)
        else:
            cur.execute(query)

        # Commit the changes to the database
        conn.commit()

        # Optionally fetch the results
        if fetch:
            result = cur.fetchall()

    except Exception as e:
        # Roll back the transaction in case of error
        conn.rollback()
        print(f"An error occurred while executing the query: {e}")

    finally:
        # Close the cursor
        cur.close()

    return result            


def batch_insert_data(table_name, data_list, connection):
    """
    Insert multiple rows of data into a given table in a single operation.

    Parameters:
    - table_name: Name of the database table to insert data into.
    - data_list: List of dictionaries, where each dictionary contains data for one row. 
                 All dictionaries should have the same keys (column names).
    - connection: Active database connection object.

    Returns:
    - None
    """

    if not data_list:
        print("No data to insert.")
        return

    # Assuming all items in data_list have the same keys
    columns = ', '.join(data_list[0].keys())
    placeholders = ', '.join(['%s'] * len(data_list[0]))

    # Constructing the INSERT statement
    insert_stmt = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    # Preparing the list of values to insert
    values = [tuple(item.values()) for item in data_list]

    try:
        # Creating a cursor and executing the batch INSERT statement
        cursor = connection.cursor()
        cursor.executemany(insert_stmt, values)

        # Committing the transaction
        connection.commit()
        print(f"{len(data_list)} rows inserted successfully.")

    except Exception as e:
        # Rolling back in case of error
        connection.rollback()
        print(f"An error occurred during batch insert: {e}")

    finally:
        # Closing the cursor
        cursor.close()


def insert_data(table_name, data, connection):
    """
    Insert data into a given table.

    Parameters:
    - table_name: Name of the database table to insert data into.
    - data: Dictionary where keys are column names and values are the data for those columns.
    - connection: Active database connection object.

    Returns:
    - None
    """

    # Constructing column names and placeholders
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))

    # Constructing the INSERT statement
    insert_stmt = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    try:
        # Creating a cursor and executing the INSERT statement
        cursor = connection.cursor()
        cursor.execute(insert_stmt, list(data.values()))

        # Committing the transaction
        connection.commit()
        print("Data inserted successfully.")

    except Exception as e:
        # Rolling back in case of error
        connection.rollback()
        print(f"An error occurred: {e}")

    finally:
        # Closing the cursor
        cursor.close()

def get_connection():
    
    connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=REMOTE_DB_IP,
    port=REMOTE_DB_PORT
    
    
)
    return connection
    

def batch_generic_insert_mlb(table_name, data_list):
    
    connection = get_connection()
    print(f'sending data to {table_name}')

    batch_insert_data(table_name, data_list, connection)

    connection.close()


def main():
    pass
    

if __name__ == "__main__":
    main()