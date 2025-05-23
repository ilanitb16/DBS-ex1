import mysql.connector

if __name__ == '__main__':
     mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="root",
         database="f1_data",
         port='3306',
     )

     cursor = mydb.cursor()

     # SQL query which wll select all the distinct drivers
     # whose nationality is 'ITA' (Italian) from the 'drivers' table
     cursor.execute("""
             SELECT DISTINCT Driver
             From drivers 
             Where Nationality = "ITA";
         """)

     print(', '.join(str(row) for row in cursor.fetchall()))


