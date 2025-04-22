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

     # This query calculates the difference between the total points (PTS) scored by the Ferrari team
     # and the total points scored by the Maserati team.

     cursor.execute("""
       SELECT 
             (SELECT SUM(PTS) FROM teams WHERE Team = 'Ferrari') -
             (SELECT SUM(PTS) FROM teams WHERE Team = 'Maserati') AS diff;
      """)

     print(', '.join(str(row) for row in cursor.fetchall()))





