import pymysql

# Параметры подключения
config = {
    'host': 'localhost',
    'user': 'RUSEL',
    'password': '102026102Rus',
    'database': 'online_shop'
}

# Подключаемся к MySQL
connection = pymysql.connect(**config)
count = 0
sum = 0
digits = []
try:
    with connection.cursor() as cursor:
        # 1. Открываем SQL-файл и читаем запрос
        with open('prcnt.sql', 'r', encoding='utf-8') as file:
            sql_query = file.read().strip()  # убираем лишние пробелы

        # 2. Выполняем запрос
        cursor.execute(sql_query)

        # 3. Получаем результат (если SELECT)
        if sql_query.lower().startswith('select'):
            result = cursor.fetchall()
            for row in result:
                #print(row[2])
                sum += row[2]
                count += 1
                digits.append(float(row[2]))
            print(count)
            print(sum/count)
        else:
            print("Запрос выполнен (не SELECT).")

    # Фиксируем изменения (если INSERT/UPDATE/DELETE)
    connection.commit()
finally:
    connection.close()