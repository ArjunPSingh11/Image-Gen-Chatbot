from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from ui.layout import render_header, render_sidebar
from ui.controls import render_prompt_controls
from ui.gallery import render_gallery
from core.session import init_session_state

st.set_page_config(
    page_title="PixelMind – AI Image Studio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session_state()
render_header()

col_left, col_right = st.columns([1, 1.4], gap="large")

with col_left:
    render_prompt_controls()

with col_right:
    render_gallery()

render_sidebar()
