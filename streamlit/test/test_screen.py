import streamlit as st
from PIL import Image

st.title("스트림릿에서 화면 분할 사용 예")

# 1) 2개로 세로 단 분할
[col1, col2] = st.columns(2)
with col1:
    st.subheader("유튜브 비디오1")
    url_col1 = "https://www.youtube.com/watch?v=4NdCF-NrFlY"
    st.video(url_col1)
with col2:
    st.subheader("유튜브 비디오2")
    url_col2 = "https://www.youtube.com/watch?v=4NdCF-NrFlY"
    st.video(url_col2)

# 2) 3개로 세로 단 분할
columns = st.columns([1.1, 1.0, 0.9])

for k in range(len(columns)):
    with columns[k]:
        st.subheader(f"test..{k+1}")
