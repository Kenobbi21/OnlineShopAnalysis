import streamlit
import os
print(os.path.dirname(streamlit.__file__))
print(os.path.join(os.path.dirname(streamlit.__file__), "..", "..", "Scripts", "streamlit.exe"))