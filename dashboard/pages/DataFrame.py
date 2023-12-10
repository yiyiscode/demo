import streamlit as st
import pandas as pd
st.title("Results")

df = pd.read_csv(r"../runs/detect/train15/results.csv", index_col=0)
st.dataframe(df.style.highlight_min(axis=0))