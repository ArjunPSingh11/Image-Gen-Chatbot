"""
Right panel: displays the most recently generated image and a scrollable gallery.
"""

import streamlit as st
from core.api import image_to_bytes


def render_gallery():
    history = st.session_state.get("history", [])

    if not history:
        # Empty state
        st.markdown(
            """
            <div style="
                border: 2px dashed #2a2a35;
                border-radius: 12px;
                padding: 4rem 2rem;
                text-align: center;
                color: #6b6b78;
            ">
                <div style="font-size:3rem">🖼️</div>
                <div style="margin-top:1rem; font-size:1rem; font-weight:500">
                    Your image will appear here
                </div>
                <div style="margin-top:0.5rem; font-size:0.82rem">
                    Enter a prompt and choose a style to get started.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    latest = history[0]

    # ── Latest image ──────────────────────────────────────────────────────────
    st.markdown('<p class="prompt-label">Latest Generation</p>', unsafe_allow_html=True)
    st.image(latest["image"], use_container_width=True)

    col_meta, col_dl = st.columns([3, 1])
    with col_meta:
        st.markdown(
            f"""
            <span class="badge">{latest['style']}</span>
            <span class="history-meta"> &nbsp;{latest['size']} &nbsp;·&nbsp; {latest['timestamp']}</span>
            """,
            unsafe_allow_html=True,
        )
    with col_dl:
        st.download_button(
            label="⬇️ Download",
            data=latest["img_bytes"],
            file_name=f"pixelmind_{latest['style'].lower().replace(' ','_')}_{latest['timestamp'].replace(':','')}.png",
            mime="image/png",
            use_container_width=True,
        )

    # ── History gallery ───────────────────────────────────────────────────────
    if len(history) > 1:
        st.divider()
        st.markdown('<p class="prompt-label">Gallery</p>', unsafe_allow_html=True)

        # Responsive 3-column grid for older images
        older = history[1:]
        cols = st.columns(3)
        for i, item in enumerate(older):
            with cols[i % 3]:
                st.image(item["image"], use_container_width=True)
                st.markdown(
                    f"""
                    <div class="history-meta" style="text-align:center">
                        <span class="badge">{item['style']}</span><br>
                        {item['timestamp']}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.download_button(
                    label="⬇️",
                    data=item["img_bytes"],
                    file_name=f"pixelmind_{i+2}_{item['style'].lower().replace(' ','_')}.png",
                    mime="image/png",
                    use_container_width=True,
                    key=f"dl_{i}",
                )
