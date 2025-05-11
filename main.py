import pymysql
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from collections import defaultdict
from googletrans import Translator
from textblob import TextBlob
import asyncio
import time
import re

# Параметры подключения
config = {
    'host': 'localhost',
    'user': 'RUSEL',
    'password': '102026102Rus',
    'database': 'online_shop'
}


# Подключаемся к MySQL


def dataforvisual():
    connection = pymysql.connect(**config)
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
    connection = pymysql.connect(**config)
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
    connection.close()


def reviews_reader():
    connection = pymysql.connect(**config)
    with connection.cursor() as cursor:
        with open("order_reviews.sql", "r", encoding="utf-8") as file:
            result = file.read()
            cursor.execute(result)
            result = cursor.fetchall()
            reviews = []
            for row in result:
                reviews.append(row[4])
            connection.close()
            return reviews


async def translate_reviews(reviews, src_lang='pt', dest_lang='en'):
    translator = Translator()
    with open("en_review.txt", "w", encoding="utf-8") as file:
        for text in reviews:
            try:
                if len(text) > 1:
                    translation = await translator.translate(text, src=src_lang, dest=dest_lang)
                    file.write(translation.text + "\n")
            except:
                file.write("")  # в случае ошибки - пустая строка
        file.close()


def detect_category(text):
    category_keywords = {
        'delivery': ['delivery', 'late', 'ship', 'arrive', 'courier', 'package', 'shipping'],
        'quality': ['quality', 'broken', 'defective', 'damage', 'faulty', 'poor'],
        'service': ['service', 'rude', 'customer support', 'manager', 'response', 'complaint'],
        'price': ['price', 'expensive', 'cost', 'refund', 'payment', 'charge']
    }
    text = text.lower()
    for category, keywords in category_keywords.items():
        if any(keyword in text for keyword in keywords):
            return category
    return 'other'


def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity


def count_complains():
    with open("en_review.txt", "r", encoding="utf-8") as file:
        reviews = file.read().strip()
        reviews = reviews.split("\n")
        category_counts = defaultdict(int)
        # Диагностика тональности категории
        # sentiment_scores = defaultdict(list)
        for i in reviews:
            if i.strip():
                category = detect_category(i)
                category_counts[category] += 1
                # sentiment = analyze_sentiment(i)
                # sentiment_scores[category].append(sentiment)
    return category_counts


def complains_viz_data():
    data = count_complains()
    complains_result = count_complains()
    complains_sum = sum(complains_result.values())
    percantage = defaultdict(float)
    for key, value in data.items():
        percantage[key] = round(float(value / complains_sum) * 100, 2)
    return dict(percantage)


def AB_test():
    engine = create_engine(f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}/{config['database']}")
    with open("orders.sql", "r", encoding="utf-8") as file:
        data = file.read()
        df = pd.read_sql(data,engine)
        customers = df["customer_id"]
        group_a = np.random.choice(customers, size=len(customers) // 2, replace=False)
        group_b = np.array([c for c in customers if c not in group_a])
        orders_count = df['orders_order_id'].nunique()
        views = orders_count * 50
        conversion = (orders_count / views) * 100
        orders_a = df[df['customer_id'].isin(group_a)]
        orders_b_count = int(len(orders_a) * 1.1)
        views_a = views / 2
        views_b = views / 2
        conv_a = (len(orders_a) / views_a) * 100# ~0.2%
        conv_b = (orders_b_count / views_b) * 100# ~0.22% (+10%)
        print(conv_a)
        print(conv_b)


# diffcounter()
# values = dataforvisual()
# sorted(values[0])
# sorted(values[1])
# reviews = reviews_reader()
# start_time = time.time()
# reviews = asyncio.run(translate_reviews(reviews, src_lang='pt', dest_lang='en'))
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time)

# category_counts = complains_viz_data()
# print("Done")
# print(category_counts.keys)
start_time = time.time()
AB_test()
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)