import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv
import os
from streamlit_autorefresh import st_autorefresh

load_dotenv()
BLYNK_TOKEN = os.environ.get('BLYNK_TOKEN')
url = f"https://blynk.cloud/external/api/get?token={BLYNK_TOKEN}&v0&v1"

print(url)

res = requests.get(url)
if res.ok:
    result = res.json()
    light = result['v0']
    vr = result['v1']

    st.title('Pico_W 專案')
    st.header(f':red[光線]: {light}  :blue[溫度]: {vr}')

    st.header('光線:')

    st.header('溫度:')

