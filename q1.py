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

     # SQL query which fetches distinct Brazilian drivers
     cursor.execute("""
         SELECT DISTINCT Driver
         FROM drivers
         WHERE Nationality = 'BRA';
     """)

     print(', '.join(str(row) for row in cursor.fetchall()))