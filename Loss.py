import streamlit as st
import pandas as pd
st.title("YOLOv8 Dashboard")
df = pd.read_csv(r"../runs/detect/train15/results.csv", index_col=0)

tab1, tab2, tab3 = st.tabs(["📈 Multiple Loss", "📈 Multiple Charts", "📈 Single Loss"])
with tab1:
    st.header("Multiple Loss in One Chart")
    st.line_chart(df)
with tab2:
    st.header("Multiple Charts in One Tab")
    st.image(r"../runs/detect/train15/results.png")
with tab3:
    st.header("Single Loss")
    option_lst = list(df.columns)
    option = st.selectbox(label="test", options=option_lst)
    st.line_chart(df, y=option)