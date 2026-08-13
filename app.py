import streamlit as st

st.set_page_config(
    page_title="Will This Session Convert?",
    page_icon="🛒",
    layout="wide"
)

# Rocket Logo
st.image("images.png", width=280)

# Rocket Red Styling
st.markdown("""
<style>
.main-title {
    color: #E72F3D;
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 0px;
}

.subtitle {
    font-size: 25px;
    font-weight: 500;
    margin-top: 0px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="main-title">Will This Session Convert?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predicting Purchase Intent</div>',
    unsafe_allow_html=True
)

st.caption(
    "Will a purchase happen before the current user session ends?"
)
