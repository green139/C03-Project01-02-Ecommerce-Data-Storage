import mysql.connector
import random
import time
import datetime


# Global methods to push interact with the Database

# This method establishes the connection with the MySQL

def create_server_connection(host_name, user_name, user_password):
    # Implement the logic to create the server connection
    # pass

    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("Mysql Database connection successful")
    except Exception as err:
        print(f"Error: '{err}' ")

    return connection

# This method will create the database and make it an active database

def create_and_switch_database(connection, db_name, switch_db):
    # For database creation use this method
    # If you have created your database using UI, no need to implement anything
    # pass

    cursor = connection.cursor()
    try:
        drop_query = "DROP DATABASE IF EXISTS " + db_name
        db_query = "CREATE DATABASE " + db_name
        switch_query = "USE " + switch_db
        cursor.execute(drop_query)
        cursor.execute(db_query)
        cursor.execute(switch_query)
        print("Database created successfully")

    except Exception as err:
        print(f"Error in creating database : '{err}'")


# This method will establish the connection with the newly created DB
def create_db_connection(host_name, user_name, user_password, db_name):
    # pass
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Exception as err:
        print(f"Error in Connecting with the database: '{err}'")

    return connection

# Use this function to create the tables in a database
def create_table(connection, table_creation_statement):
    # pass
    if connection is not None:
        cursor = connection.cursor()
    try:
        cursor.execute(table_creation_statement)
        connection.commit()
        print("Table creation successful")
    except Exception as err:
        print(f"Error is table_creation: '{err}'")


# Perform all single insert statments in the specific table through a single function call
def create_insert_query(connection, query):
    # This method will perform creation of the table
    # this can also be used to perform single data point insertion in the desired table
    # pass
    if connection is not None:
        cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Insert operation successful")
    except Exception as err:
        print(f"Error in table creation: '{err}'")


# retrieving the data from the table based on the given query
def select_query(connection, query):
    # fetching the data points from the table
    # pass
    if connection is not None:
        cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as err:
        print(f"Error in select query: '{err}'")


# Execute multiple insert statements in a table
def insert_many_records(connection, sql, val):
    # pass

    if connection is not None:
        cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Many Insert operations are successful")
    except Exception as err:
        print(f"Error in many insert query: '{err}'")


