import pymysql
from collections import defaultdict

# Параметры подключения
config = {
    'host': 'localhost',
    'user': 'RUSEL',
    'password': '102026102Rus',
    'database': 'online_shop'
}
# Подключаемся к MySQL
connection = pymysql.connect(**config)


def dataforvisual():
    count = 0
    sum = 0
    population = []
    avgvalue = []
    values = defaultdict(int)
    cities = defaultdict(int)
    try:
        with connection.cursor() as cursor:
            # 1. Открываем SQL-файл и читаем запрос
            with open('ltv.sql', 'r', encoding='utf-8') as file:
                sql_query = file.read().strip()  # убираем лишние пробелы
            # 2. Выполняем запрос
            cursor.execute(sql_query)
            # 3. Получаем результат (если SELECT)
            if sql_query.lower().startswith('select'):
                result = cursor.fetchall()
                for row in result:
                    values[row[1]] = int(row[3])
                    cities[row[1]] = row[0]

                return values, cities
            else:
                print("Запрос выполнен (не SELECT).")
    finally:
        connection.close()


def diffcounter():
    # Difference between 2017 and 2018 in total revenue and avg values minus failed transactions
    with connection.cursor() as cursor:
        with open("revenue.sql", "r", encoding="utf-8") as file:
            result = file.read()
            cursor.execute(result)
            if result.lower().startswith("select"):
                result = cursor.fetchall()
            gencounter = (result[2][1] / result[1][1])
            avgcounter = result[2][2] / result[1][2]
            print(
                f"revenue growth: {round((gencounter - 1) * 100, 1)}% \navg value growth: {round((avgcounter - 1) * 100, 1)}% ")
        file.close()


diffcounter()
values = dataforvisual()
sorted(values[0])
sorted(values[1])

connection = pymysql.connect(**config)
def reviews_reader():
    with connection.cursor() as cursor:
        with open("order_reviews.sql", "r", encoding="utf-8") as file:
            result = file.read()
            cursor.execute(result)
            result = cursor.fetchall()
            for row in result:
                print(row[4])
        file.close()
val = reviews_reader()
print(val)