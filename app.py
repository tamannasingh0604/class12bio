"""
Sexual Reproduction in Flowering Plants
Class 12 Biology Chapter 1 — NEET + Boards Study Guide

Streamlit App — Entry Point
Run with: streamlit run app.py
"""

import streamlit as st
from pathlib import Path

# ── Page config (must be first Streamlit call) ──────────────────────────────
st.set_page_config(
    page_title="Bio Ch.1 | Sexual Reproduction in Flowering Plants",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Import page modules ──────────────────────────────────────────────────────
from pages_content import (
    page_intro,
    page_flower,
    page_stamen,
    page_pistil,
    page_pollination,
    page_fertilisation,
    page_seed,
    page_apomixis,
    page_revision,
)
from components import inject_global_css, render_hero, render_footer
from modal_data import TERMS_JS

# ── Global CSS (fonts, colours, cards, modal, MCQ styles) ───────────────────
inject_global_css()

# ── Hero banner ─────────────────────────────────────────────────────────────
render_hero()

# ── Sidebar navigation ──────────────────────────────────────────────────────
PAGES = {
    "🌿  Introduction":          page_intro,
    "🌸  The Flower":            page_flower,
    "🌾  Stamen & Pollen":       page_stamen,
    "🌼  Pistil & Ovule":        page_pistil,
    "🐝  Pollination":           page_pollination,
    "⚗️  Fertilisation":          page_fertilisation,
    "🌱  Seed & Embryo":         page_seed,
    "🔬  Apomixis":              page_apomixis,
    "📋  Quick Revision":        page_revision,
}

with st.sidebar:
    st.markdown("## 📚 Topics")
    st.markdown("---")
    selection = st.radio(
        label="Navigate",
        options=list(PAGES.keys()),
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown(
        """
        <div style='font-size:0.75rem;color:#4b6857;line-height:1.6'>
        📖 NCERT Class 12 Biology<br>
        🏫 Allen Module (NEET UG)<br>
        ✏️ CBSE Board PYQs<br><br>
        <em>Click any <u>green underlined</u><br>term to expand full notes.</em>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Render selected page ─────────────────────────────────────────────────────
PAGES[selection]()

# ── Inject modal JS (term popup system) — runs once per page ─────────────────
st.components.v1.html(TERMS_JS, height=0, scrolling=False)

# ── Footer ───────────────────────────────────────────────────────────────────
render_footer()
