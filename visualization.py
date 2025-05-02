import streamlit as st
import pandas as pd
import numpy as np
import main

# Генерация данных
data = pd.DataFrame({
    'months': np.arange(25),
    'percents': main.digits
})

# Линейный график
st.line_chart(data, x='months', y='percents')

# Столбчатая диаграмма
st.bar_chart(data, x='months', y='percents')

# Диаграмма площадей
st.area_chart(data, x='months', y='percents')
