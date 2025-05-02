import pandas as pd
from sqlalchemy import create_engine
import os

# Настройки подключения к MySQL
db_config = {
    'host': 'localhost',
    'user': 'RUSEL',
    'password': '102026102Rus',
    'database': 'online_shop'
}

# Создание подключения
engine = create_engine(
    f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")
# Путь к папке с CSV-файлами
data_folder = "D:/dataset/archive"

# Список файлов для загрузки
files = [
    (os.path.join(data_folder,'olist_customers_dataset.csv'), 'customers'),
    (os.path.join(data_folder,'olist_orders_dataset.csv'), 'orders'),
    (os.path.join(data_folder,'olist_order_items_dataset.csv'), 'order_items'),
    (os.path.join(data_folder,'olist_order_payments_dataset.csv'), 'order_payments'),
    (os.path.join(data_folder,'olist_order_reviews_dataset.csv'), 'order_reviews'),
    (os.path.join(data_folder,'olist_products_dataset.csv'), 'products')
]
# Загрузка каждого файла в соответствующую таблицу
for file, table in files:
    print(f"Loading {file} into {table}...")
    df = pd.read_csv(file)

    # Преобразование дат, если необходимо
    date_columns = [col for col in df.columns if 'date' in col.lower() or 'timestamp' in col.lower()]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    # Загрузка в MySQL
    df.to_sql(table, con=engine, if_exists='append', index=False, chunksize=1000)
    print(f"Successfully loaded {len(df)} records into {table}")

print("All data loaded successfully!")
