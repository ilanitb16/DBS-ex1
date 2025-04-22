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

     # The query: joins the 'drivers' and 'fastest_laps' tables based on matching car names. Then, select only the records
     # where lap time is under 2 minutes or 120 seconds. For each car, calculates the average points scored
     # by its drivers and groups the results by car.
     # Orders the cars by their average points in descending order.

     cursor.execute("""
        SELECT drivers.Car, AVG(drivers.PTS) as avg_pts
        FROM drivers, fastest_laps
        WHERE fastest_laps.Car = drivers.Car
        AND MINUTE(STR_TO_DATE(Time, '%i:%s.%f')) < 2
        GROUP BY drivers.Car
        ORDER BY avg_pts DESC
     """)

     print(', '.join(str(row) for row in cursor.fetchall()))








