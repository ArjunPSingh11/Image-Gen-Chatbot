"""
Custom CSS injected into Streamlit.
Two themes: dark (default) and light.
"""

DARK_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

html, body, [data-testid="stApp"] {
    background-color: #0d0d0f !important;
    color: #e8e6e3 !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

[data-testid="stSidebar"] {
    background-color: #131316 !important;
    border-right: 1px solid #2a2a30 !important;
}

.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #a855f7) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.03em !important;
    padding: 0.6rem 1.4rem !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 20px rgba(124, 58, 237, 0.4) !important;
}

.stTextArea textarea, .stTextInput input {
    background-color: #1a1a1f !important;
    border: 1px solid #2a2a35 !important;
    border-radius: 8px !important;
    color: #e8e6e3 !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 2px rgba(124, 58, 237, 0.2) !important;
}

.stRadio > div {
    gap: 0.5rem !important;
}

.stRadio label {
    background: #1a1a1f !important;
    border: 1px solid #2a2a35 !important;
    border-radius: 8px !important;
    padding: 0.5rem 0.9rem !important;
    cursor: pointer !important;
    transition: border-color 0.15s !important;
}

.stRadio label:hover {
    border-color: #7c3aed !important;
}

.pixel-header {
    font-family: 'Space Mono', monospace;
    font-size: 2.4rem;
    font-weight: 700;
    background: linear-gradient(135deg, #a855f7 0%, #7c3aed 50%, #6366f1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.02em;
    margin: 0;
}

.pixel-tagline {
    color: #6b6b78;
    font-size: 0.9rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-top: 0.25rem;
}

.prompt-label {
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #7c3aed;
    margin-bottom: 0.3rem;
}

.full-prompt-box {
    background: #1a1a1f;
    border: 1px solid #2a2a35;
    border-left: 3px solid #7c3aed;
    border-radius: 6px;
    padding: 0.75rem 1rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.78rem;
    color: #9d9daa;
    margin: 0.5rem 0 1rem;
    word-break: break-word;
}

.history-card {
    background: #1a1a1f;
    border: 1px solid #2a2a35;
    border-radius: 10px;
    padding: 0.75rem;
    margin-bottom: 0.75rem;
}

.history-meta {
    font-size: 0.72rem;
    color: #6b6b78;
    font-family: 'Space Mono', monospace;
    margin-top: 0.35rem;
}

.badge {
    display: inline-block;
    background: rgba(124, 58, 237, 0.15);
    color: #a855f7;
    border: 1px solid rgba(168, 85, 247, 0.3);
    border-radius: 4px;
    padding: 0.1rem 0.5rem;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.06em;
}

div[data-testid="stImage"] img {
    border-radius: 10px !important;
    border: 1px solid #2a2a35 !important;
}

.stSelectbox > div > div {
    background: #1a1a1f !important;
    border-color: #2a2a35 !important;
    color: #e8e6e3 !important;
}

hr {
    border-color: #2a2a35 !important;
}
</style>
"""

LIGHT_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

html, body, [data-testid="stApp"] {
    background-color: #f7f5ff !important;
    color: #1a1225 !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

[data-testid="stSidebar"] {
    background-color: #ede9fe !important;
    border-right: 1px solid #c4b5fd !important;
}

.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #a855f7) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

.stTextArea textarea, .stTextInput input {
    background-color: #ffffff !important;
    border: 1px solid #c4b5fd !important;
    border-radius: 8px !important;
    color: #1a1225 !important;
}

.pixel-header {
    font-family: 'Space Mono', monospace;
    font-size: 2.4rem;
    font-weight: 700;
    background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.02em;
    margin: 0;
}

.pixel-tagline {
    color: #9d9daa;
    font-size: 0.9rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-top: 0.25rem;
}

.prompt-label {
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #7c3aed;
    margin-bottom: 0.3rem;
}

.full-prompt-box {
    background: #fff;
    border: 1px solid #c4b5fd;
    border-left: 3px solid #7c3aed;
    border-radius: 6px;
    padding: 0.75rem 1rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.78rem;
    color: #6d28d9;
    margin: 0.5rem 0 1rem;
    word-break: break-word;
}

.history-card {
    background: #fff;
    border: 1px solid #c4b5fd;
    border-radius: 10px;
    padding: 0.75rem;
    margin-bottom: 0.75rem;
}

.history-meta {
    font-size: 0.72rem;
    color: #9d9daa;
    font-family: 'Space Mono', monospace;
    margin-top: 0.35rem;
}

.badge {
    display: inline-block;
    background: rgba(124, 58, 237, 0.1);
    color: #7c3aed;
    border: 1px solid rgba(124, 58, 237, 0.25);
    border-radius: 4px;
    padding: 0.1rem 0.5rem;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.06em;
}
</style>
"""


def inject_css(theme: str = "dark"):
    import streamlit as st
    css = DARK_CSS if theme == "dark" else LIGHT_CSS
    st.markdown(css, unsafe_allow_html=True)
