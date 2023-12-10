import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["F1", "Precision", "Precision/Recall", "Recall"])
tab1.image(r"runs/detect/train15/F1_curve.png")
tab2.image(r"runs/detect/train15/P_curve.png")
tab3.image(r"runs/detect/train15/PR_curve.png")
tab4.image(r"runs/detect/train15/R_curve.png")
