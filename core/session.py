"""
Centralised session state initialisation.
All mutable state lives here so it is easy to reason about.
"""

import streamlit as st


def init_session_state():
    defaults = {
        "history": [],          # list of dicts: {prompt, style, full_prompt, image, timestamp}
        "theme": "dark",        # "dark" | "light"
        "generating": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def add_to_history(entry: dict):
    """Prepend a new generation entry to history (newest first)."""
    st.session_state.history.insert(0, entry)


def clear_history():
    st.session_state.history = []
