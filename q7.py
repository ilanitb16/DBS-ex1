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





