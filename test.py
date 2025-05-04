import pymysql

config = {
    'host': 'localhost',
    'user': 'RUSEL',
    'password': '102026102Rus',
    'database': 'online_shop'
}

connection = pymysql.connect(**config)


def diffcounter():
    #Difference between 2017 and 2018 in total revenue and avg values minus failed transactions
    with connection.cursor() as cursor:
        with open("revenue.sql", "r", encoding="utf-8") as file:
            result = file.read()
            cursor.execute(result)
            if result.lower().startswith("select"):
                result = cursor.fetchall()
            gencounter = (result[2][1] / result[1][1])
            avgcounter = result[2][2] / result[1][2]
            print(f"revenue growth: {round((gencounter - 1)*100,1)}% \navg value growth: {round((avgcounter - 1)*100,1)}% ")
        file.close()

diffcounter()