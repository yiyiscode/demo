pip install plotly==5.18.0
import streamlit as st
import plotly.express as px
import pandas as pd
st.title("Information")
st.info('Now showing the No3. YOLOv8n model', icon="ℹ️")
df = pd.DataFrame(
    [
        {"Class": "Pomacea canaliculata", "Amount": 129},
        {"Class": "Pomacea canaliculata's egg", "Amount": 42},
        {"Class": "Mixed", "Amount": 21},
    ]
)
tab1, tab2 = st.tabs(["⏺️ Pie Chart", "📊 Histogram"])
with tab1:
    fig = px.pie(df, values='Amount', names='Class', color_discrete_sequence=px.colors.qualitative.T10)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    fig1 = px.histogram(df, x="Class", y="Amount",
                        color='Class', height=600, 
                        color_discrete_sequence=px.colors.qualitative.T10)
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)