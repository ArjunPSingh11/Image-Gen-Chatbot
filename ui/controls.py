"""
Left panel: prompt input, style selector, image size, and generate button.
"""

import random
import datetime
import streamlit as st
from core.styles import STYLES, RANDOM_PROMPTS, IMAGE_SIZES, build_prompt, get_negative_prompt
from core.api import generate_image, image_to_bytes
from core.session import add_to_history


def render_prompt_controls():
    # ── Prompt input ──────────────────────────────────────────────────────────
    st.markdown('<p class="prompt-label">Your Prompt</p>', unsafe_allow_html=True)

    col_input, col_rand = st.columns([5, 1])
    with col_input:
        prompt = st.text_area(
            label="prompt_area",
            label_visibility="collapsed",
            placeholder="Describe the image you want to create…",
            height=110,
            key="user_prompt",
        )
    with col_rand:
        st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
        if st.button("🎲", help="Random prompt", use_container_width=True):
            st.session_state.user_prompt = random.choice(RANDOM_PROMPTS)
            st.rerun()

    # ── Negative prompt ───────────────────────────────────────────────────────
    with st.expander("➕ Negative prompt (optional)", expanded=False):
        negative_override = st.text_input(
            label="negative_prompt",
            label_visibility="collapsed",
            placeholder="Things to avoid in the image…",
            key="negative_prompt",
        )

    # ── Style selector ────────────────────────────────────────────────────────
    st.markdown('<p class="prompt-label" style="margin-top:1rem">Style</p>', unsafe_allow_html=True)
    style_names = list(STYLES.keys())
    style_icons = [f"{STYLES[s]['icon']} {s}" for s in style_names]

    selected_idx = st.radio(
        label="style_radio",
        label_visibility="collapsed",
        options=range(len(style_names)),
        format_func=lambda i: style_icons[i],
        horizontal=False,
        key="selected_style_idx",
    )
    selected_style = style_names[selected_idx]
    st.caption(STYLES[selected_style]["description"])

    # ── Image size ────────────────────────────────────────────────────────────
    st.markdown('<p class="prompt-label" style="margin-top:1rem">Image Size</p>', unsafe_allow_html=True)
    size_label = st.selectbox(
        label="size_select",
        label_visibility="collapsed",
        options=list(IMAGE_SIZES.keys()),
        key="image_size",
    )
    w, h = map(int, IMAGE_SIZES[size_label].split("x"))

    # ── Full prompt preview ───────────────────────────────────────────────────
    if prompt:
        full_prompt = build_prompt(prompt, selected_style)
        st.markdown('<p class="prompt-label" style="margin-top:1rem">Final Prompt Sent to API</p>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="full-prompt-box">{full_prompt}</div>',
            unsafe_allow_html=True,
        )

    # ── Generate button ───────────────────────────────────────────────────────
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    generate_clicked = st.button(
        "✨ Generate Image",
        use_container_width=True,
        type="primary",
        disabled=not bool(prompt and prompt.strip()),
    )

    if generate_clicked and prompt.strip():
        _run_generation(prompt, selected_style, w, h, negative_override)


def _run_generation(prompt: str, style: str, width: int, height: int, negative_override: str):
    full_prompt = build_prompt(prompt, style)
    negative = negative_override.strip() or get_negative_prompt(style)

    with st.spinner("🎨 Generating your image…"):
        try:
            image = generate_image(
                prompt=full_prompt,
                negative_prompt=negative,
                width=width,
                height=height,
            )

            if image:
                img_bytes = image_to_bytes(image)
                entry = {
                    "prompt": prompt,
                    "style": style,
                    "full_prompt": full_prompt,
                    "image": image,
                    "img_bytes": img_bytes,
                    "timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
                    "size": f"{width}×{height}",
                }
                add_to_history(entry)
                st.session_state.latest_image = entry
                st.rerun()

        except ValueError as e:
            st.error(f"🔑 API key issue: {e}")
        except RuntimeError as e:
            st.error(f"🚨 Generation failed: {e}")
        except Exception as e:
            st.error(f"⚠️ Unexpected error: {e}")
