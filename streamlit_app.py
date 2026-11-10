from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PVT data QC", layout="wide")

html = (Path(__file__).parent / "pvt-qc" / "pvt-qc.html").read_text(encoding="utf-8")
components.html(html, height=2400, scrolling=True)
