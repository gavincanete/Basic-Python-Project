import mysql.connector as db_connector
from mysql.connector import Error

class AddressBookDB():    
    def __init__(self):
        self.connection = self.create_connection('localhost', 'root', '$gameDeveloper97', 'basic_db')
        select_last_record = "select ID from address_book order by id desc limit 1"
        last_record = self.execute_read_query(select_last_record)

        
        if(len(last_record) != 0):
            self.counter = last_record[0][0]
            self.counter += 1
        else:
            self.counter = 1

    # Connect to database
    def create_connection(self, host_name, user_name, user_password, db_name):
        temp = None
        try:
            temp = db_connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return temp

    # Add entry to address_book table without cell#
    def add_contact(self, firstName, middleInitial, lastName, address, city):        
        create_contact = f"""
            insert into
                `address_book` (`ID`, `firstName`, `middleInitial`, `lastName`, `address`, `city`)
            
            values
                ({int(self.counter)}, '{firstName}', '{middleInitial}', '{lastName}', '{address}', '{city}')
        """        
        result = self.execute_query(create_contact)

        print(result)
        if(result == "Query executed successfully"):
            self.counter += 1            
            return "Successfully added"
        else:
            return "Failed to update Contact"

    # Used to call insert into command
    def execute_query(self, query):
        self.connection.autocommit = True
        
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            return "Query executed successfully"
        except Error as e:
             return f"The error '{e}' occurred"

    # Used to fetch data from the Database when not yet in cache
    def execute_read_query(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")


    def get_id(self):
        return str(self.counter)

    
