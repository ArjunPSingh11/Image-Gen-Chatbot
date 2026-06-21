# PixelMind – AI Image Studio 🎨

A clean, deployable **AI image generation chatbot** built with Python and Streamlit. Type a prompt, pick a style, and generate stunning AI images powered by the [FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) model via the HuggingFace Inference API.

---

## What it does

- **Text-to-image generation** using FLUX.1-schnell (state-of-the-art open model)
- **8 distinct visual styles**: Photorealistic, Cyberpunk, Anime, Oil Painting, Watercolor, Fantasy, Minimalist, Retro
- **Style-conditioned prompts** — your prompt is automatically enhanced with style-specific modifiers before hitting the API
- **Gallery view** — all images generated in a session are shown in a scrollable grid
- **Download button** for every generated image
- **Negative prompt support** — tell the model what to avoid
- **Image size selector** — Square, Landscape, or Portrait
- **Random prompt generator** — click 🎲 for inspiration
- **Dark / Light theme toggle**
- **Prompt history** in the sidebar

---

## Project structure

```
image-gen-chatbot/
├── app.py                  # Entry point — wires layout together
├── core/
│   ├── api.py              # HuggingFace API calls
│   ├── styles.py           # Style definitions & prompt engineering
│   └── session.py          # Streamlit session state management
├── ui/
│   ├── layout.py           # Header + sidebar
│   ├── controls.py         # Prompt input, style picker, generate button
│   ├── gallery.py          # Image display + download
│   └── styles.py           # Custom CSS (dark + light themes)
├── .streamlit/
│   └── secrets.toml.example
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Running locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/image-gen-chatbot.git
cd image-gen-chatbot
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key (see below)

### 5. Run the app
```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Adding your HuggingFace API key

### Local development

1. Duplicate `.env.example` and rename it `.env`
2. Paste your token:
```
HF_TOKEN=hf_your_token_here
```

**How to get a free token:**
1. Create an account at [huggingface.co](https://huggingface.co)
2. Go to **Settings → Access Tokens**
3. Click **New token** → choose **Read** access
4. Copy the token — it starts with `hf_`

You get free monthly inference credits. No billing setup needed for FLUX.1-schnell.

---

## Deploying to Streamlit Community Cloud (free)

1. Push your code to a **public GitHub repo** (make sure `.env` is in `.gitignore`)
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
3. Click **New app** → select your repo → set main file to `app.py`
4. Open **Advanced settings → Secrets** and paste:
```toml
HF_TOKEN = "hf_your_token_here"
```
5. Click **Deploy** — your app is live in ~60 seconds

### Other deployment options

| Platform | Notes |
|----------|-------|
| [Render](https://render.com) | Free tier available; set env var `HF_TOKEN` in dashboard |
| [Railway](https://railway.app) | Simple GitHub deploy; add env var in project settings |

---

## Known limitation

**Session-only history** — generated images are stored in Streamlit's in-memory session state and are lost when the browser tab is closed or the server restarts. To persist images across sessions you would need to add a database (e.g. SQLite) or cloud storage (e.g. Supabase, AWS S3).

---

## Built with

- [Streamlit](https://streamlit.io) — UI framework
- [HuggingFace Inference API](https://huggingface.co/docs/inference-providers) — model hosting
- [FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) — image generation model
- [Pillow](https://pillow.readthedocs.io) — image handling
- [python-dotenv](https://pypi.org/project/python-dotenv/) — local secrets management
