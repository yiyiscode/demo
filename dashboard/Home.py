pip install plotly==5.18.0
import streamlit as st
import pandas as pd
st.title("YOLOv8 Dashboard")
col1, col2= st.columns([1, 2])

with col1:
    number = st.number_input('Number', min_value=0, step=1, value=10)
    st.success('Train NO '+ str(number), icon="✅")
    st.warning('TRAIN SET 150 Images')
    st.info('VAL SET  21 Images')
    st.error('TEST SET  21 Images')

with col2:
    col2_1, col2_2, col2_3= st.columns([1, 1, 1])
    with col2_1:
        st.metric(label="TRAIN SET", value="78 %", delta="-3 %")
    with col2_2:
        st.metric(label="VAL SET", value="11 %", delta="-2 %")
    with col2_3:
        st.metric(label="TEST SET", value="11 %", delta="7 %")
    st.success('Data Augmentations', icon="📖")
    st.info('''
                Flip: Horizontal \\
                90° Rotate: Clockwise, Counter-Clockwise \\
                Crop: 0% Minimum Zoom, 20% Maximum Zoom \\
                Saturation: Between -25% and +25% \\
                Exposure: Between -25% and +25%''')

df = pd.DataFrame(
    [
    {"No.": "1", "Model": "YOLOv8n","Images": 92, "Precision":0.25, "Data Augmentations": False, "Performance":None},
    {"No.": "2", "Model": "YOLOv8n","Images": 124, "Precision":0.54, "Data Augmentations": True, "Performance":"↗️"},
    {"No.": "3", "Model": "YOLOv8n","Images": 192, "Precision":0.54, "Data Augmentations": True, "Performance":"➡️"},
    {"No.": "4", "Model": "YOLOv8x","Images": 92, "Precision":0.25, "Data Augmentations": False, "Performance":None},
    {"No.": "5", "Model": "YOLOv8x","Images": 124, "Precision":0.54, "Data Augmentations": True, "Performance":"↗️"},
    {"No.": "6", "Model": "YOLOv8x","Images": 192, "Precision":0.54, "Data Augmentations": True, "Performance":"➡️"},
]
)
edited_df = st.data_editor(df, num_rows="dynamic")

    # favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["No."]
    # st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


