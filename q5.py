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
        SELECT drivers.Car, AVG(drivers.PTS) as avg_pts
        FROM drivers, fastest_laps
        WHERE fastest_laps.Car = drivers.Car
        AND MINUTE(STR_TO_DATE(Time, '%i:%s.%f')) < 2
        GROUP BY drivers.Car
        ORDER BY avg_pts DESC
     """)

     print(', '.join(str(row) for row in cursor.fetchall()))








