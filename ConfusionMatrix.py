import streamlit as st

tab1, tab2 = st.tabs(["Confusion Matrix", "NormalizedConfusion Matrix"])
tab1.image(r"../runs/detect/train15/confusion_matrix.png")
tab2.image(r"../runs/detect/train15/confusion_matrix_normalized.png")