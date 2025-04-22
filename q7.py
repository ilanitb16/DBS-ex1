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

     # This query finds all unique drivers who are either French (Nationality = 'FRA')
     # or who have won a race driving a Ferrari, and lists them together in alphabetical order.

     cursor.execute("""
        SELECT DISTINCT Driver AS driver
        FROM drivers 
        WHERE Nationality = 'FRA'
        
        UNION
        
        SELECT DISTINCT Winner AS driver
        FROM winners 
        WHERE Car = 'Ferrari'
        ORDER BY driver;
      """)

     print(', '.join(str(row) for row in cursor.fetchall()))





