import streamlit as st

st.set_page_config(
    page_title="Will This Session Convert?",
    page_icon="🛒",
    layout="wide"
)

# ============================================================
# STYLING
# ============================================================

st.markdown("""
<style>

.rocket-title {
    color: #E72F3D;
    font-size: 46px;
    font-weight: 700;
    line-height: 1.1;
    margin-top: 20px;
}

.rocket-subtitle {
    font-size: 24px;
    font-weight: 500;
    margin-top: 8px;
}

.description {
    font-size: 16px;
    color: #666666;
    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

left, right = st.columns([3, 1])


# LEFT — TITLE
with left:

    st.markdown(
        '<div class="rocket-title">Will This Session Convert?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="rocket-subtitle">Predicting Purchase Intent</div>',
        unsafe_allow_html=True
    )


# RIGHT — ROCKET LOGO
with right:

    st.image(
        "images.png",
        width=250
    )
