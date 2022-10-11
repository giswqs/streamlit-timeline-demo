import streamlit as st
from streamlit_timeline import st_timeline

st.set_page_config(page_title="Timeline", layout="wide")

st.header("Streamlit Timeline")
st.markdown("""
    Streamlit component for rendering [vis.js timeline](https://github.com/visjs/vis-timeline). Source code available on [GitHub](https://github.com/giswqs/streamlit-timeline).
""")


items = [
    {"id": 1, "content": "2022-10-20", "start": "2022-10-20"},
    {"id": 2, "content": "2022-10-09", "start": "2022-10-09"},
    {"id": 3, "content": "2022-10-18", "start": "2022-10-18"},
    {"id": 4, "content": "2022-10-16", "start": "2022-10-16"},
    {"id": 5, "content": "2022-10-25", "start": "2022-10-25"},
    {"id": 6, "content": "2022-10-27", "start": "2022-10-27"},
]

timeline = st_timeline(items, groups=[], options={}, height="300px")
st.subheader("Selected item")
st.write(timeline)
