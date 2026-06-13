import streamlit as st
import random
import time

st.set_page_config(page_title="/// SYSTEM FAILURE ///", layout="wide")

st.markdown("""
<style>
body {
    background-color: #000000;
    color: #d0d0d0;
    font-family: monospace;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: 900;
    color: #ff0000;
    letter-spacing: 6px;
    margin-top: 20px;
    animation: flicker 1.5s infinite;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 12px;
    margin-bottom: 20px;
}

.panel {
    background: rgba(10,10,10,0.9);
    border: 1px solid #330000;
    padding: 14px;
    margin-bottom: 12px;
    box-shadow: 0 0 20px #ff000022;
}

.label {
    color: #ff3b3b;
    font-weight: 800;
}

.value {
    color: #aaa;
    font-size: 13px;
}

.warning {
    color: #ff0000;
    font-weight: 900;
    letter-spacing: 3px;
    text-align: center;
    margin: 20px 0;
}

@keyframes flicker {
    0% { opacity: 1; }
    45% { opacity: 0.6; }
    50% { opacity: 0.2; }
    55% { opacity: 1; }
    100% { opacity: 0.7; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>SYSTEM CORRUPTION DETECTED</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>UNSTABLE MEMORY STRUCTURE / SIGNAL LOSS IN PROGRESS</div>", unsafe_allow_html=True)

nodes = ["NODE-01", "NODE-02", "NODE-03", "NODE-04"]

choice = st.selectbox("SELECT FRAGMENT", nodes)

def glitch_text():
    words = [
        "memory leak detected",
        "signal fading",
        "unknown process running",
        "data corruption spreading",
        "identity fragmentation",
        "system heartbeat irregular",
        "log file overwritten",
        "trace unverified"
    ]
    return random.choice(words)

data = {
    "NODE-01": ["IDENTITY CORE", "MEMORY SECTOR", "VISUAL FEED"],
    "NODE-02": ["BEHAVIOR PATTERN", "THOUGHT TRACE", "NEURAL MAP"],
    "NODE-03": ["SYSTEM LINK", "SIGNAL PATH", "DATA STREAM"],
    "NODE-04": ["ARCHIVE FILE", "DELETED MEMORY", "UNKNOWN ENTRY"]
}

st.markdown("<div class='warning'>WARNING: STABILITY BELOW CRITICAL LEVEL</div>", unsafe_allow_html=True)

for item in data[choice]:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown(f"<div class='label'>[ {item} ]</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='value'>STATUS: {glitch_text()}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='warning'>DO NOT TRUST SYSTEM OUTPUT</div>", unsafe_allow_html=True)
