import streamlit as st
from gorq import Gorq
st.set_page_config(page_title = " Placement Practice",layout='centered')
st.title("AI Interview Assistant")
st.caption("Practice and Prepare for your Placement here")
try:
  client = Gorq(api_key = st.secrets"GORQ_API_KEY")
except (Keyerror, FileNotFoundError):
  st.error("API Key is missing. Add it in Advanced settings")
  st.stop()
