from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PVT data QC", layout="wide")

here = Path(__file__).parent
candidates = [here / "pvt-qc.html", here / "pvt-qc" / "pvt-qc.html"]
page = next((p for p in candidates if p.exists()), None)

if page is None:
    st.error("pvt-qc.html not found. Put it next to streamlit_app.py or in a pvt-qc/ folder.")
    st.stop()

components.html(page.read_text(encoding="utf-8"), height=2400, scrolling=True)
