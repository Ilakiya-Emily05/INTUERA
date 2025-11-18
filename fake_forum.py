import streamlit as st
import random
import time
import json

st.set_page_config(
    page_title="DarkBazaar BlackSite",
    page_icon="🕷️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------- SIM DATA FOR SCRAPER ----------------------
fake_data = [
    {
        "username": random.choice(["zeroGhost", "blackHydra", "NovaRogue", "shadeByte"]),
        "cve": random.choice(["CVE-2025-1221", "CVE-2024-8819", "CVE-2023-9921", "None"]),
        "btc": random.randint(0, 5),
        "category": random.choice(["scam", "exploit", "malware", "cred-sale", "fraud"]),
        "sentiment": random.choice(["hostile", "neutral", "risky"]),
        "text": random.choice([
            "Selling premium logs batch.",
            "Fresh exploit pack ready.",
            "Leaking corporate vault backup.",
            "New infostealer variant compiled.",
            "BTC mixer request received."
        ]),
        "risk": random.randint(1, 10),
        "location": random.choice(["US", "IN", "RU", "BR", "CN"])
    }
    for _ in range(25)
]

# Expose JSON for your INTUERA scraper:
json_blob = json.dumps(fake_data)

st.markdown(
    f"<script id='darkbazaar-data' type='application/json'>{json_blob}</script>",
    unsafe_allow_html=True
)

# ---------------------- CSS DARK WEB UPGRADE ----------------------
dark_css = """
<style>
body { background: #000000; }

@keyframes glitch1 {
  0% { text-shadow: 3px 3px #ff003c; }
  50% { text-shadow: -3px -3px #00eaff; }
  100% { text-shadow: 3px 3px #ff003c; }
}

.glitch-header {
    font-size: 70px;
    font-family: monospace;
    text-align: center;
    color: #ff003c;
    margin-top: 10px;
    animation: glitch1 1s infinite;
}

@keyframes staticMove {
  0% {opacity: .15;}
  50% {opacity: .35;}
  100% {opacity: .15;}
}

.static-overlay {
    background: url('https://i.imgur.com/9v0ZC2Q.png');
    opacity: 0.18;
    width: 100%;
    height: 160px;
    animation: staticMove 2s infinite;
    mix-blend-mode: screen;
    margin-bottom: 20px;
}

.terminal-block {
    background: #050505;
    border-left: 4px solid #00eaff;
    padding: 18px;
    margin-bottom: 15px;
    color: #b7ffff;
    font-family: monospace;
    font-size: 15px;
}

.warning-box {
    background: #ff003c;
    color: black;
    padding: 20px;
    border-radius: 5px;
    text-align: center;
    font-family: monospace;
    font-size: 18px;
    animation: flashWarn .5s alternate infinite;
}

@keyframes flashWarn {
    from { background: #ff003c; }
    to { background: #ff7090; }
}

.fake-btn {
    width: 100%;
    padding: 12px;
    border-radius: 6px;
    background: black;
    border: 2px solid #ff003c;
    color: #ff7090;
    font-family: monospace;
    transition: .2s;
}

.fake-btn:hover {
    transform: scale(1.05);
    background: #1a0007;
}
</style>
"""
st.markdown(dark_css, unsafe_allow_html=True)

# ---------------------- HEADER ----------------------
st.markdown("<div class='glitch-header'>DARKBAZAAR BLACKSITE</div>", unsafe_allow_html=True)
st.markdown("<div class='static-overlay'></div>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align:center; color:#888; font-family:monospace;'>Tor Mirror v5 / Encrypted Simulation Node</h5>", unsafe_allow_html=True)

# ---------------------- FAKE ANTIVIRUS SCAN ----------------------
if st.button("⚠️ Trigger System Scan"):
    st.markdown("<div class='warning-box'>⚠️ WARNING: Suspicious activity detected. System integrity compromised.</div>", unsafe_allow_html=True)
    time.sleep(1)
    st.code("SCAN_STATUS: MALWARE_SIMULATED\nRISK_LEVEL: CRITICAL\nRECOMMENDATION: Disconnect immediately.", language="bash")

# ---------------------- FAKE OFFERS ----------------------
st.subheader("🎁 Underground Offers (Fake)")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Free Premium Logs"):
        st.markdown("<div class='warning-box'>⚠️ ALERT: Unauthorized Access Attempt Logged.</div>", unsafe_allow_html=True)

with col2:
    if st.button("Free Crypto Mixer Trial"):
        st.code("ERROR: CryptoMixer kernel refused. Node flagged.", language="bash")

with col3:
    if st.button("Get Free Zero-Day Pack"):
        st.markdown("<div class='warning-box'>🚨 SECURITY NOTICE: Zero-day exploit blocked.</div>", unsafe_allow_html=True)

# ---------------------- LIVE FEED ----------------------
st.subheader("💀 Live DarkFeed (Simulated)")

feed_placeholder = st.empty()

if st.button("Start Feed"):
    for i in range(20):
        msg = random.choice([
            "Tunneling into node 56... AUTH REFUSED",
            "New leak detected in synthetic vault.",
            "Fake credentials batch uploaded.",
            "Simulated brute-force attempt intercepted.",
            "Monitoring darknet traffic pattern anomalies..."
        ])
        feed_placeholder.markdown(f"<div class='terminal-block'>{msg}</div>", unsafe_allow_html=True)
        time.sleep(0.35)

# ---------------------- FOOTER ----------------------
st.markdown("<div style='text-align:center; margin-top:50px; color:#333;'>Simulation Only. No real darknet services are accessed.</div>", unsafe_allow_html=True)
