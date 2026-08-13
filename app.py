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
        '<div class="rocket-title">Will The Session Convert into Purchase?</div>',
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

# ============================================================
# DATASET OVERVIEW
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">Dataset Overview</div>',
    unsafe_allow_html=True
)

st.caption(
    "One month of e-commerce behavioral data capturing customer "
    "interactions across the complete shopping journey."
)


# ============================================================
# DATASET METRICS — ROW 1
# ============================================================

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">📊</div>
        <div class="metric-value">42.45M</div>
        <div class="metric-label">Total Records</div>
        <div class="metric-detail">42,448,764 interactions</div>
    </div>
    """, unsafe_allow_html=True)


with c2:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">👥</div>
        <div class="metric-value">3.02M</div>
        <div class="metric-label">Unique Customers</div>
        <div class="metric-detail">3,022,290 customers</div>
    </div>
    """, unsafe_allow_html=True)


with c3:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">🛒</div>
        <div class="metric-value">9.24M</div>
        <div class="metric-label">Unique Sessions</div>
        <div class="metric-detail">9,244,421 sessions</div>
    </div>
    """, unsafe_allow_html=True)


with c4:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">📦</div>
        <div class="metric-value">166,794</div>
        <div class="metric-label">Unique Products</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# DATASET METRICS — ROW 2
# ============================================================

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">🏷️</div>
        <div class="metric-value">3,444</div>
        <div class="metric-label">Unique Brands</div>
    </div>
    """, unsafe_allow_html=True)


with c2:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">🗂️</div>
        <div class="metric-value">126</div>
        <div class="metric-label">Unique Categories</div>
    </div>
    """, unsafe_allow_html=True)


with c3:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">🔢</div>
        <div class="metric-value">9</div>
        <div class="metric-label">Initial Features</div>
    </div>
    """, unsafe_allow_html=True)


with c4:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">📅</div>
        <div class="metric-value">1 Month</div>
        <div class="metric-label">Dataset Period</div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# DATASET METRICS — ROW 3
# ============================================================

c1, c2, c3 = st.columns(3)


with c1:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">🧭</div>
        <div class="metric-value">4</div>
        <div class="metric-label">Category Levels</div>
        <div class="metric-detail">Hierarchical product categories</div>
    </div>
    """, unsafe_allow_html=True)


with c2:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">⚠️</div>
        <div class="metric-value">30,220</div>
        <div class="metric-label">Duplicate Records</div>
        <div class="metric-detail">0.07% of total records</div>
    </div>
    """, unsafe_allow_html=True)


with c3:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">👆</div>
        <div class="metric-value">3</div>
        <div class="metric-label">Unique Event Types</div>
        <div class="metric-detail">View · Cart · Purchase</div>
    </div>
    """, unsafe_allow_html=True)
