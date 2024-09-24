import requests
from bs4 import BeautifulSoup
import re
import streamlit as st

@st.cache_data
def fetch_webpage_content(url):
    if not url.startswith(("http://", "https://")):
        st.error("Invalid URL scheme. Please ensure the URL starts with 'http://' or 'https://'.")
        return ""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text(separator="\n")
            text = re.sub(r'^\s*$\n', '', text, flags=re.MULTILINE)
            return text
        else:
            st.error(f"Failed to fetch the webpage. Status code: {response.status_code}")
            return ""
    except Exception as e:
        st.error(f"An error occurred while fetching the webpage: {e}")
        return ""