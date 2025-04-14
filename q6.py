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
    SELECT DISTINCT w1.`Grand Prix` AS GP1, w2.`Grand Prix` AS GP2, w1.Laps
    FROM winners as w1, winners as w2
    WHERE w1.Laps = w2.Laps
    AND w1.Laps > 120
    AND w1.`Grand Prix`< w2.`Grand Prix`
 """)

    print(', '.join(str(row) for row in cursor.fetchall()))
