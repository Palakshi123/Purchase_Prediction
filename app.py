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

st.markdown("## Dataset Overview")

st.caption(
    "One month of e-commerce behavioral data capturing customer interactions "
    "across the complete shopping journey."
)

# ============================================================
# CARD STYLING
# ============================================================

st.markdown("""
<style>

.metric-card {
    background-color: #F8F9FA;
    border: 1px solid #E8E8E8;
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 10px;
    min-height: 95px;
}

.metric-icon {
    font-size: 20px;
    margin-bottom: 5px;
}

.metric-value {
    font-size: 22px;
    font-weight: 700;
    color: #E72F3D;
}

.metric-label {
    font-size: 13px;
    color: #666666;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# ROW 1
# ============================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">📊</div>
        <div class="metric-value">42.45M</div>
        <div class="metric-label">Total Records</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">👥</div>
        <div class="metric-value">3.02M</div>
        <div class="metric-label">Unique Customers</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">🛒</div>
        <div class="metric-value">9.24M</div>
        <div class="metric-label">Unique Sessions</div>
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
# ROW 2
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
# ROW 3
# ============================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">🧭</div>
        <div class="metric-value">4</div>
        <div class="metric-label">Category Levels</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">⚠️</div>
        <div class="metric-value">30,220</div>
        <div class="metric-label">Duplicate Records · 0.07%</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">👆</div>
        <div class="metric-value">3 Event Types</div>
        <div class="metric-label">View · Cart · Purchase</div>
    </div>
    """, unsafe_allow_html=True)
