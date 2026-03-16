import streamlit as st

from tab_home import render_home
from tab_designing import render_designing
from tab_about import render_about

st.set_page_config(
    page_title="DNA Data Storage Tool",
    page_icon="DDSS_logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
/* Page shell */
div.block-container {
    padding-top: 6.4rem;
    padding-bottom: 1.2rem;
    padding-left: 1.4rem;
    padding-right: 1.4rem;
    max-width: 1480px;
}
header[data-testid="stHeader"] {height: 0.01rem;}
h1, h2, h3 {margin-top: 0.1rem; margin-bottom: 0.45rem;}
p {margin-bottom: 0.35rem;}
section[data-testid="stSidebar"] {border-right: 1px solid rgba(60, 72, 88, 0.10);}
section[data-testid="stSidebar"] .block-container {padding-top: 0.9rem;}
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 14px;
    border: 1px solid rgba(77, 99, 120, 0.16);
    background: linear-gradient(180deg, rgba(248,250,252,0.98), rgba(242,246,250,0.98));
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
}
div[data-testid="stVerticalBlockBorderWrapper"] > div {padding-top: 0.5rem; padding-bottom: 0.55rem;}
div[data-baseweb="input"] input, textarea {border-radius: 10px !important;}
div[data-baseweb="select"] > div {border-radius: 10px !important;}
button[kind="primary"], button[kind="secondary"] {
    border-radius: 12px !important;
    padding-top: 0.48rem !important;
    padding-bottom: 0.48rem !important;
}
.stTabs [data-baseweb="tab-list"] {gap: 0.35rem;}
.stTabs [data-baseweb="tab"] {border-radius: 12px; padding: 8px 12px;}
div[role="radiogroup"] {
    display: flex;
    flex-wrap: nowrap;
    gap: 0.4rem;
    margin-top: 2.8rem;
    margin-bottom: 0.4rem;
}
div[role="radiogroup"] > label {
    padding: 8px 14px;
    border-radius: 12px;
    border: 1px solid rgba(77, 99, 120, 0.18);
    font-size: 15px;
    font-weight: 700;
    background: rgba(243, 247, 250, 0.96);
    min-width: fit-content;
}
div[role="radiogroup"] > label:hover {border-color: rgba(44, 123, 229, 0.55);}
div[role="radiogroup"] > label:has(input:checked) {
    border: 2px solid rgba(44, 123, 229, 0.95);
    background: rgba(44, 123, 229, 0.10);
}
div[data-testid="stAlert"] {border-radius: 14px;}
div[data-testid="stPlotlyChart"] {border-radius: 14px; overflow: hidden;}
hr {margin: 0.55rem 0 0.75rem 0; opacity: 0.28;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    try:
        st.image("DDSS_logo.png", width=280)
    except Exception:
        pass

    st.title("DNA Storage Lab")
    st.info("System Version: 1.0.0-Stable")
    st.divider()

    st.subheader("🖥️ System Status")
    st.success("Server Status: Online")
    st.write("**Core Engine:** Connected")
    st.write("**Worker Node:** Active")
    st.divider()

    st.subheader("📚 Resources")
    st.button("📖 User Manual", width="stretch")
    st.button("❓ Help Center", width="stretch")
    st.button("🛠️ API Documentation", width="stretch")
    st.divider()

    st.subheader("⚙️ Control Panel")
    st.selectbox("Computing Tier", ["Standard Local", "High-Performance Cloud", "Hybrid Engine"], index=0)
    st.checkbox("Enable Detailed Logs", value=True)
    st.checkbox("Auto-Optimization", value=False)
    st.divider()

    st.markdown("""
        <div style="text-align: center; color: #888; font-size: 13px;">
            <strong>© 2025 DNA Data Storage Lab.</strong><br>
            Sungkyunkwan University.<br>
            All Rights Reserved.
        </div>
    """, unsafe_allow_html=True)

PAGES = {
    "Homepage": render_home,
    "Design": render_designing,
    "About Us": render_about,
}

if "main_page" not in st.session_state:
    st.session_state["main_page"] = "Design"

st.markdown("<div style='height:5.8rem;'></div>", unsafe_allow_html=True)

page = st.radio(
    "Main navigation",
    options=list(PAGES.keys()),
    key="main_page",
    horizontal=True,
    label_visibility="collapsed",
)

PAGES[page]()
