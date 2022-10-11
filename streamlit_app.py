import streamlit as st
from streamlit_timeline import st_timeline

st.set_page_config(page_title="Timeline", layout="wide")

st.title("Streamlit Timeline")
st.markdown(
    """
    Streamlit component for rendering [vis.js timeline](https://github.com/visjs/vis-timeline). 
    Check out the GitHub repositories [streamlit-timeline](https://github.com/giswqs/streamlit-timeline) and 
    [streamlit-timeline-demo](https://github.com/giswqs/streamlit-timeline-demo). For JavaScript examples, 
    check out the vis.js timeline [examples](https://visjs.github.io/vis-timeline/examples/timeline/) and 
    [documentation](https://visjs.github.io/vis-timeline/docs/timeline/).
"""
)

st.header("Basic Example")

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

st.header("With groups")

items = [
    {
        "id": 1,
        "content": "editable",
        "editable": True,
        "start": "2022-08-23",
        "group": 1,
    },
    {
        "id": 2,
        "content": "editable",
        "editable": True,
        "start": "2022-08-23T23:00:00",
        "group": 2,
    },
    {
        "id": 3,
        "content": "Read-only",
        "editable": False,
        "start": "2022-08-24T16:00:00",
        "group": 1,
    },
    {
        "id": 4,
        "content": "Read-only",
        "editable": False,
        "start": "2022-08-26",
        "end": "2022-09-02",
        "group": 2,
    },
    {
        "id": 5,
        "content": "editable",
        "editable": True,
        "start": "2022-08-28",
        "group": 1,
    },
    {
        "id": 6,
        "content": "Read-only",
        "editable": False,
        "start": "2022-08-29",
        "group": 2,
    },
    {
        "id": 7,
        "content": "editable",
        "editable": True,
        "start": "2022-08-31",
        "end": "2022-09-03",
        "group": 1,
    },
    {
        "id": 8,
        "content": "Read-only",
        "editable": False,
        "start": "2022-09-04T12:00:00",
        "group": 2,
    },
    {"id": 9, "content": "Default", "start": "2022-09-04", "group": 1},
    {"id": 10, "content": "Default", "start": "2022-08-24", "group": 2},
]


groups = [
    {"id": 1, "content": "group 1", "style": "color: black; background-color: cyan;"},
    {"id": 2, "content": "group 2", "style": "color: black; background-color: pink;"},
]

timeline = st_timeline(items, groups=groups, options={}, height="300px")
st.subheader("Selected item")
st.write(timeline)
