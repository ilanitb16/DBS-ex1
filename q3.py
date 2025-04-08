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
    SELECT Driver,
    (SELECT MIN(MINUTE(STR_TO_DATE(Time, '%i:%s.%f')))  
       FROM fastest_laps
        WHERE fastest_laps.Driver = drivers.Driver ) AS min_time
    FROM drivers, winners
    WHERE winners.Winner = drivers.Driver 
      AND YEAR(winners.Date) = 2000
    GROUP BY Driver
    ORDER BY SUM(winners.Laps) DESC
    LIMIT 1;
    """)

    print(', '.join(str(row) for row in cursor.fetchall()))
