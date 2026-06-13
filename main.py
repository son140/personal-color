import streamlit as st

st.set_page_config(page_title="SYSTEM INTERFACE", layout="wide")

st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #050505, #000000);
    color: #00ff9d;
    font-family: monospace;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #00ff9d;
    letter-spacing: 6px;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    color: #888;
    font-size: 12px;
    margin-bottom: 30px;
}

.panel {
    background: rgba(0,0,0,0.7);
    border: 1px solid #00ff9d;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 0 20px #00ff9d33;
}

.label {
    color: #00ff9d;
    font-weight: 700;
}

.value {
    color: #aaa;
    font-size: 13px;
}

.warning {
    color: #ff3b3b;
    font-weight: 800;
    letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>SYSTEM INTERFACE</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>ACCESSING PERSONAL PROFILE DATABASE</div>", unsafe_allow_html=True)

mode = st.selectbox("SELECT NODE", ["NODE A", "NODE B", "NODE C", "NODE D"])

data = {
    "NODE A": [
        {"name": "IDENTITY TRACE", "status": "ACTIVE", "desc": "USER SIGNAL DETECTED IN NETWORK"},
        {"name": "MEMORY FRAGMENT", "status": "CORRUPTED", "desc": "PARTIAL DATA LOSS DETECTED"},
        {"name": "LOCATION PING", "status": "UNKNOWN", "desc": "SIGNAL MASKED"}
    ],
    "NODE B": [
        {"name": "BEHAVIOR MODEL", "status": "ANALYZING", "desc": "PATTERN RECOGNITION IN PROGRESS"},
        {"name": "EMOTION INDEX", "status": "UNSTABLE", "desc": "FLUCTUATION DETECTED"}
    ],
    "NODE C": [
        {"name": "SYSTEM LINK", "status": "ESTABLISHED", "desc": "CONNECTION STABLE"},
        {"name": "DATA FLOW", "status": "OVERCLOCKED", "desc": "WARNING: HIGH LOAD"}
    ],
    "NODE D": [
        {"name": "CORE FILE", "status": "LOCKED", "desc": "ACCESS DENIED"},
        {"name": "TRACE LOG", "status": "DELETED", "desc": "NO RECORD FOUND"}
    ]
}

st.markdown(f"### {mode}")

st.markdown("<div class='warning'>WARNING: UNAUTHORIZED ACCESS MAY BE LOGGED</div>", unsafe_allow_html=True)

for item in data[mode]:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown(f"<div class='label'>▶ {item['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='value'>STATUS: {item['status']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='value'>{item['desc']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
