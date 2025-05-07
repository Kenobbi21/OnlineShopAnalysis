import streamlit as st
import pandas as pd
import numpy as np
import main
import matplotlib.pyplot as plt

def drawer():
    # Генерация данных
    data = pd.DataFrame({
        'population': main.values[0].keys(),
        'avgvalue': main.values[0].values()
    })

    # Линейный график
    st.line_chart(data, x='population', y='avgvalue')

    # Столбчатая диаграмма
    st.bar_chart(data, x='population', y='avgvalue')

    # Диаграмма площадей

def circle_drawer(category_counts):
    st.title('Analysis of complaints by category')
    st.markdown('Complaint Distribution Pie Chart')
    df = pd.DataFrame({
        'Category': category_counts.keys(),
        'Count': category_counts.values()
    })
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    wedges, texts, autotexts = ax.pie(
        df['Count'],
        labels=df['Category'],
        colors=colors[:len(df)],
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=0.85,
        textprops={'fontsize': 10}
    )
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontsize(10)

        # Добавление круга в центре (donut chart)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)

    # Заголовок и легенда
    ax.set_title('Distribution of complaints by categories', pad=20)
    ax.axis('equal')  # Круговая диаграмма будет круглой

    # Отображение в Streamlit
    st.pyplot(fig)

circle_drawer(main.category_counts)