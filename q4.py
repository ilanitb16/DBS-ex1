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
     # The query finds the car that had the most wins in the year 1999 and counts how many times that same car
     # won again in the year 2001.

     cursor.execute("""SELECT COUNT(*)
         FROM winners
         WHERE Car = (
             SELECT Car
             FROM winners
             WHERE YEAR(Date) = 1999
             GROUP BY Car
             HAVING COUNT(*) = (
                 SELECT MAX(win_count)
                 FROM (
                     SELECT COUNT(*) AS win_count
                     FROM winners
                     WHERE YEAR(Date) = 1999
                     GROUP BY Car
                 ) AS sub
             )
         )
         AND YEAR(Date) = 2001;
      """)

     print(', '.join(str(row) for row in cursor.fetchall()))




