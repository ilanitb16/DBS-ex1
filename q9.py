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

     # This query lists each nationality along with the average points (PTS) scored by its drivers,
     # the best (minimum) lap time by its drivers, and the latest race win date by its drivers — but only for
     # nationalities that have at least one lap time and one win.

     # We were told to avoid NULL values, hence the last part of the query.
     
     cursor.execute("""
     SELECT drivers.Nationality, 
     
         (SELECT AVG(d2.PTS)
          FROM drivers d2
          WHERE d2.Nationality = drivers.Nationality) AS avg_pts,
     
         (SELECT MIN(f.Time) AS min_time
          FROM fastest_laps f, drivers d2
          WHERE f.Driver = d2.Driver 
            AND d2.Nationality = drivers.Nationality
         ) AS min_time,
     
         (SELECT MAX(w.Date)
          FROM winners w, drivers d3
          WHERE w.Winner = d3.Driver 
            AND d3.Nationality = drivers.Nationality
         ) AS latest
     
     FROM drivers
     GROUP BY drivers.Nationality
     HAVING min_time IS NOT NULL
     AND latest IS NOT NULL;
      """)

     print(', '.join(str(row) for row in cursor.fetchall()))