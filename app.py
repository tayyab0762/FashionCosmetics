import streamlit as st
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Fashion Cosmetics – Luxury Beauty Store | Lahore, Pakistan",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Helpers ───────────────────────────────────────────────────────────────────
DIST_INDEX = os.path.join(os.path.dirname(__file__), "dist", "index.html")


def load_built_app() -> str | None:
    """Return the contents of dist/index.html if it exists (pre-built React app)."""
    if os.path.exists(DIST_INDEX):
        with open(DIST_INDEX, "r", encoding="utf-8") as f:
            return f.read()
    return None


# ── Main ──────────────────────────────────────────────────────────────────────
html_content = load_built_app()

if html_content:
    # ------------------------------------------------------------------ #
    # Option A – Serve the compiled React/Vite bundle via an iframe.      #
    # Run `npm run build` locally first; commit the `dist/` folder.       #
    # ------------------------------------------------------------------ #
    st.components.v1.html(html_content, height=900, scrolling=True)

else:
    # ------------------------------------------------------------------ #
    # Option B – Fallback Streamlit UI shown when dist/ isn't present.    #
    # Useful for quick Streamlit Cloud previews without a build step.     #
    # ------------------------------------------------------------------ #
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap');

        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

        .hero-title {
            font-family: 'Playfair Display', serif;
            font-size: 3.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #c9a96e 0%, #f5e6c8 50%, #c9a96e 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.2;
        }
        .tagline {
            font-size: 1.1rem;
            color: #9c8576;
            letter-spacing: 0.15em;
            text-transform: uppercase;
        }
        .badge {
            display: inline-block;
            padding: 6px 18px;
            border: 1px solid #c9a96e;
            border-radius: 50px;
            color: #c9a96e;
            font-size: 0.78rem;
            letter-spacing: 0.1em;
            margin: 4px;
        }
        .card {
            background: #1a1410;
            border: 1px solid #2e2018;
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
        }
        .card-title { font-family: 'Playfair Display', serif; font-size: 1.2rem; color: #f5e6c8; }
        .card-sub   { font-size: 0.85rem; color: #9c8576; margin-top: 4px; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Hero
    col_l, col_r = st.columns([2, 1])
    with col_l:
        st.markdown('<p class="tagline">Lahore · Pakistan · Est. 2024</p>', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Fashion<br>Cosmetics</h1>', unsafe_allow_html=True)
        st.markdown(
            "Premium beauty & cosmetics — skincare, makeup, fragrances and more. "
            "Cash on Delivery available across Pakistan.",
            unsafe_allow_html=False,
        )
        st.markdown(
            '<span class="badge">💄 Makeup</span>'
            '<span class="badge">✨ Skincare</span>'
            '<span class="badge">🌸 Fragrances</span>'
            '<span class="badge">🚚 COD</span>',
            unsafe_allow_html=True,
        )
    with col_r:
        st.image(
            "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400&q=80",
            caption="Premium Beauty",
            use_container_width=True,
        )

    st.divider()

    # Category cards
    st.subheader("Shop by Category")
    cats = [
        ("💄", "Makeup", "Foundation · Lipstick · Eyes"),
        ("🧴", "Skincare", "Serums · Moisturisers · SPF"),
        ("🌸", "Fragrances", "Perfumes · Body Mists"),
        ("🛁", "Bath & Body", "Scrubs · Lotions · Oils"),
    ]
    cols = st.columns(len(cats))
    for col, (icon, name, sub) in zip(cols, cats):
        with col:
            st.markdown(
                f'<div class="card"><div style="font-size:2rem">{icon}</div>'
                f'<p class="card-title">{name}</p>'
                f'<p class="card-sub">{sub}</p></div>',
                unsafe_allow_html=True,
            )

    st.divider()

    # Build instructions
    with st.expander("ℹ️  Developer note – serve the full React app"):
        st.code(
            """# 1. Install Node dependencies
npm install

# 2. Build the React/Vite app
npm run build          # outputs to ./dist/

# 3. Commit dist/ to your repo, then deploy on Streamlit Cloud.
#    app.py will automatically detect dist/index.html and render it.

# Local preview
streamlit run app.py
""",
            language="bash",
        )
        st.info(
            "Streamlit Cloud will serve the compiled React bundle inside an iframe. "
            "Make sure `dist/` is committed and not in `.gitignore`."
        )
