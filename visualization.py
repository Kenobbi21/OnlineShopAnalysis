import streamlit as st
import pandas as pd
import numpy as np
import main

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
st.area_chart(data, x='population', y='avgvalue')
