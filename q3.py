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
     # Find the driver(s) who in 2000 had the maximum number of total laps led,
     # along with their minimum lap time.

     cursor.execute("""
         WITH driver_laps AS (
             SELECT drivers.Driver, SUM(winners.Laps) AS total_laps
             FROM drivers
             JOIN winners ON winners.Winner = drivers.Driver
             WHERE YEAR(winners.Date) = 2000
             GROUP BY drivers.Driver
         ),
         max_laps AS (
             SELECT MAX(total_laps) AS max_laps
             FROM driver_laps
         )
         SELECT dl.Driver,
                (SELECT MIN(MINUTE(STR_TO_DATE(Time, '%i:%s.%f')))
                 FROM fastest_laps
                 WHERE fastest_laps.Driver = dl.Driver) AS min_time
         FROM driver_laps dl
         JOIN max_laps ml ON dl.total_laps = ml.max_laps;
     """)

     # This is my old query where I used limit. No one clarified if we can use limit or not, so I kept both versions.

     # cursor.execute("""
     #          SELECT Driver,
     #          (SELECT MIN(MINUTE(STR_TO_DATE(Time, '%i:%s.%f')))
     #             FROM fastest_laps
     #              WHERE fastest_laps.Driver = drivers.Driver ) AS min_time
     #          FROM drivers, winners
     #          WHERE winners.Winner = drivers.Driver
     #            AND YEAR(winners.Date) = 2000
     #          GROUP BY Driver
     #          ORDER BY SUM(winners.Laps) DESC
     #          LIMIT 1;
     #          """)

     print(', '.join(str(row) for row in cursor.fetchall()))
