import psycopg2


# Define a class to handle PostgreSQL database connections and operations
class PGDatabase:
    # Initialize the database connection when an instance of PGDatabase is created
    def __init__(self, host, database, user, password):
        self.host = host  # Host where the PostgreSQL server is running
        self.database = database  # Name of the PostgreSQL database
        self.user = user  # Username to connect to the database
        self.password = password  # Password for the user

        # Establish a connection to the PostgreSQL database using the provided credentials
        self.connection = psycopg2.connect(
            host=host, 
            database=database, 
            user=user, 
            password=password
        )

        self.cursor = self.connection.cursor()  # Create a cursor object to execute queries
        self.connection.autocommit = True  # Automatically commit transactions (no need for manual commit)

    # Method to execute a SQL query that modifies the database (INSERT, UPDATE, DELETE)
    def post(self, query, args=()):
        try:
            self.cursor.execute(query, args)  # Execute the SQL query with optional arguments
        except Exception as e:
            # If an error occurs, print an error message with the exception details
            print(f"Error executing query: {e}")