"""
Layout components: header and sidebar.
"""

import streamlit as st
from ui.styles import inject_css
from core.session import clear_history


def render_header():
    inject_css(st.session_state.get("theme", "dark"))
    st.markdown(
        """
        <div style="padding: 1.5rem 0 1rem;">
            <p class="pixel-header">PixelMind</p>
            <p class="pixel-tagline">AI Image Studio &nbsp;·&nbsp; Powered by FLUX</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()


def render_sidebar():
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        st.divider()

        # Theme toggle
        current = st.session_state.get("theme", "dark")
        label = "☀️ Switch to Light" if current == "dark" else "🌙 Switch to Dark"
        if st.button(label, use_container_width=True):
            st.session_state.theme = "light" if current == "dark" else "dark"
            st.rerun()

        st.divider()
        st.markdown("### 📜 Prompt History")
        history = st.session_state.get("history", [])
        if not history:
            st.caption("No images generated yet.")
        else:
            st.caption(f"{len(history)} image(s) this session")
            if st.button("🗑️ Clear History", use_container_width=True):
                clear_history()
                st.rerun()

            for i, item in enumerate(history):
                with st.expander(f"#{len(history) - i}  {item['style']}", expanded=False):
                    st.caption(item["prompt"])
                    st.markdown(
                        f'<span class="badge">{item["style"]}</span>',
                        unsafe_allow_html=True,
                    )

        st.divider()
        st.markdown(
            """
            <div style="font-size:0.75rem; color:#6b6b78; line-height:1.6;">
            <b>How to get your API key:</b><br>
            1. Sign up at <a href="https://huggingface.co" target="_blank" style="color:#a855f7">huggingface.co</a><br>
            2. Go to Settings → Access Tokens<br>
            3. Create a token with <b>read</b> access<br>
            4. Paste it in <code>.env</code> as <code>HF_TOKEN=...</code>
            </div>
            """,
            unsafe_allow_html=True,
        )
