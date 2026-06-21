"""
Style definitions and prompt engineering for image generation.
Each style appends specific modifiers to the user's raw prompt.
"""

STYLES: dict[str, dict] = {
    "Photorealistic": {
        "icon": "📷",
        "suffix": "photorealistic, DSLR quality, sharp focus, natural lighting, 8k resolution",
        "negative": "cartoon, painting, sketch, blurry, low quality",
        "description": "Lifelike, camera-quality images",
    },
    "Cyberpunk": {
        "icon": "🌆",
        "suffix": "cyberpunk aesthetic, neon lights, rain-slicked streets, dark futuristic city, blade runner vibes, cinematic",
        "negative": "bright daylight, nature, rural, vintage",
        "description": "Neon-drenched dystopian future",
    },
    "Anime": {
        "icon": "✨",
        "suffix": "anime style, studio ghibli inspired, detailed, vibrant colors, clean linework, cel-shaded",
        "negative": "photorealistic, 3d render, ugly, blurry",
        "description": "Japanese animation aesthetic",
    },
    "Oil Painting": {
        "icon": "🖼️",
        "suffix": "oil painting, impressionist brushstrokes, rich textures, masterwork, museum quality, Renaissance lighting",
        "negative": "digital art, photo, sketch, flat design",
        "description": "Classical fine art style",
    },
    "Watercolor": {
        "icon": "💧",
        "suffix": "watercolor illustration, soft edges, translucent washes, dreamy, pastel tones, hand-painted",
        "negative": "photorealistic, sharp edges, digital, 3d",
        "description": "Soft, painterly illustration",
    },
    "Fantasy": {
        "icon": "🧙",
        "suffix": "epic fantasy art, magical atmosphere, dramatic lighting, detailed world-building, concept art style",
        "negative": "modern, realistic, urban, mundane",
        "description": "Magical realms and epic scenes",
    },
    "Minimalist": {
        "icon": "◻️",
        "suffix": "minimalist design, clean composition, limited color palette, negative space, modern graphic design",
        "negative": "cluttered, busy, detailed, photorealistic",
        "description": "Clean and stripped-back visuals",
    },
    "Retro / Vintage": {
        "icon": "📼",
        "suffix": "retro aesthetic, vintage 1970s style, film grain, muted colors, nostalgic, analogue photography",
        "negative": "modern, digital, sharp, vibrant",
        "description": "Nostalgic old-school look",
    },
}

RANDOM_PROMPTS = [
    "A crow sitting on a neon sign in a monsoon rainstorm",
    "An ancient temple hidden inside a giant banyan tree",
    "A tea stall on the surface of the moon",
    "A futuristic Delhi Metro station in 2150",
    "A tiger reading a newspaper in a Mumbai café",
    "A floating market at sunset in Kerala",
    "An astronaut lost in the Thar Desert at dusk",
    "A robot playing a sitar at a classical music festival",
    "A baby elephant wearing a graduation cap",
    "A lighthouse made entirely of books in a stormy sea",
]

IMAGE_SIZES = {
    "Square (1:1)": "1024x1024",
    "Landscape (16:9)": "1280x720",
    "Portrait (9:16)": "720x1280",
}


def build_prompt(user_prompt: str, style_name: str) -> str:
    """Combine user prompt with style-specific modifiers."""
    style = STYLES.get(style_name, {})
    suffix = style.get("suffix", "")
    return f"{user_prompt.strip()}, {suffix}" if suffix else user_prompt.strip()


def get_negative_prompt(style_name: str) -> str:
    """Return the negative prompt for a given style."""
    return STYLES.get(style_name, {}).get("negative", "")
