import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv
import os
from streamlit_autorefresh import st_autorefresh

load_dotenv()
BLYNK_TOKEN = os.environ.get('BLYNK_TOKEN')
url = f"https://blynk.cloud/external/api/get?token={BLYNK_TOKEN}&v0&v1"

st_autorefresh(interval=5000)
st.title('Pico_W 專案')

res = requests.get(url)
if res.status_code == 200:
    result = res.json()
    light = result['v0']
    vr = result['v1']

    st.header('光線:')
    st.info(light)
    st.header('溫度:')
    st.info(vr)
else:
    st.write("連線失敗,請等一下再試")