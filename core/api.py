"""
Image generation via Hugging Face Inference API.
Supports FLUX.1-schnell (default) and is easy to swap for other models.
"""

import os
import io
import base64
import requests
from PIL import Image

HF_API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"
DEFAULT_MODEL = "black-forest-labs/FLUX.1-schnell"


def _get_token() -> str:
    """Retrieve the HuggingFace token from environment or Streamlit secrets."""
    # Try environment variable first (local .env)
    token = os.getenv("HF_TOKEN", "")
    if token:
        return token

    # Try Streamlit secrets (when deployed)
    try:
        import streamlit as st
        token = st.secrets.get("HF_TOKEN", "")
        return token
    except Exception:
        return ""


def generate_image(
    prompt: str,
    negative_prompt: str = "",
    width: int = 1024,
    height: int = 1024,
) -> Image.Image | None:
    """
    Call the HuggingFace Inference API and return a PIL Image.
    Returns None on failure (caller should surface the error).
    """
    token = _get_token()
    if not token:
        raise ValueError(
            "No HuggingFace token found. Add HF_TOKEN to your .env file or Streamlit secrets."
        )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "num_inference_steps": 4,  # FLUX.1-schnell is optimised for 4 steps
        },
    }

    response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=90)

    if response.status_code != 200:
        raise RuntimeError(
            f"API error {response.status_code}: {response.text[:300]}"
        )

    image = Image.open(io.BytesIO(response.content))
    return image


def image_to_bytes(image: Image.Image, fmt: str = "PNG") -> bytes:
    """Convert PIL Image to bytes for download."""
    buffer = io.BytesIO()
    image.save(buffer, format=fmt)
    return buffer.getvalue()
