import streamlit as st
import random
import time

st.set_page_config(page_title="ABYSS NODE", layout="wide")

st.markdown("""
<style>
body {
    background-color: #000000;
    color: #b0b0b0;
    font-family: monospace;
    overflow-x: hidden;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 900;
    color: #8b0000;
    letter-spacing: 8px;
    margin-top: 20px;
    animation: flicker 2s infinite;
}

.subtitle {
    text-align: center;
    color: #444;
    font-size: 12px;
    margin-bottom: 30px;
}

.glitch-box {
    background: rgba(10,10,10,0.95);
    border: 1px solid #220000;
    padding: 14px;
    margin-bottom: 12px;
    box-shadow: 0 0 25px #ff000010;
}

.label {
    color: #ff2a2a;
    font-weight: 800;
}

.text {
    color: #999;
    font-size: 13px;
}

.warning {
    text-align: center;
    color: #ff0000;
    font-weight: 900;
    letter-spacing: 3px;
    margin: 20px 0;
    animation: flicker 1.2s infinite;
}

@keyframes flicker {
    0% { opacity: 1; }
    40% { opacity: 0.3; }
    50% { opacity: 0.1; }
    60% { opacity: 1; }
    100% { opacity: 0.6; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>ABYSS NODE INTERFACE</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>UNSTABLE SYSTEM / SIGNAL DECAY DETECTED</div>", unsafe_allow_html=True)

node = st.selectbox("SELECT SECTOR", ["SECTOR-01", "SECTOR-02", "SECTOR-03", "SECTOR-04"])

glitch_lines = [
    "signal lost... reconnecting failed",
    "memory fragment corrupted beyond recovery",
    "unknown presence detected in system layer",
    "data structure collapsing",
    "user identity unstable",
    "audio feed: distorted silence",
    "visual output degraded",
    "warning: internal breach expanding"
]

data = {
    "SECTOR-01": ["CORE MEMORY", "VISUAL LAYER", "TRACE FILE"],
    "SECTOR-02": ["NEURAL MAP", "BEHAVIOR TRACE", "SIGNAL PATH"],
    "SECTOR-03": ["SYSTEM LOG", "UNKNOWN FILE", "ARCHIVE"],
    "SECTOR-04": ["DELETED DATA", "BLACK BOX", "EMPTY NODE"]
}

st.markdown("<div class='warning'>DO NOT CONTINUE VIEWING</div>", unsafe_allow_html=True)

for item in data[node]:
    st.markdown("<div class='glitch-box'>", unsafe_allow_html=True)
    st.markdown(f"<div class='label'>[{item}]</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='text'>{random.choice(glitch_lines)}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='warning'>SYSTEM IS NO LONGER STABLE</div>", unsafe_allow_html=True)
