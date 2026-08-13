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
# DATASET OVERVIEW — COMPACT
# ============================================================

st.divider()

st.markdown("## Dataset Overview")

st.caption(
    "One month of e-commerce behavioral data capturing View, Cart, and Purchase interactions."
)

# ============================================================
# COMPACT CARD STYLING
# ============================================================

st.markdown("""
<style>

.metric-card {
    background-color: #F8F9FA;
    border: 1px solid #E8E8E8;
    border-radius: 8px;
    padding: 8px 10px;
    min-height: 72px;
    text-align: center;
}

.metric-icon {
    font-size: 15px;
    display: inline;
}

.metric-value {
    font-size: 17px;
    font-weight: 700;
    color: #E72F3D;
    display: inline;
    margin-left: 4px;
}

.metric-label {
    font-size: 11px;
    color: #666666;
    margin-top: 3px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# ROW 1
# ============================================================

c1, c2, c3, c4, c5, c6 = st.columns(6)

cards_row1 = [
    ("📊", "42.45M", "Total Records"),
    ("👥", "3.02M", "Unique Customers"),
    ("🛒", "9.24M", "Unique Sessions"),
    ("📦", "166,794", "Unique Products"),
    ("🏷️", "3,444", "Unique Brands"),
    ("🗂️", "126", "Unique Categories")
]

for col, (icon, value, label) in zip(
    [c1, c2, c3, c4, c5, c6],
    cards_row1
):
    with col:
        st.markdown(
            f"""
            <div class="metric-card">
                <div>
                    <span class="metric-icon">{icon}</span>
                    <span class="metric-value">{value}</span>
                </div>
                <div class="metric-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# ROW 2
# ============================================================

c1, c2, c3, c4, c5 = st.columns(5)

cards_row2 = [
    ("🔢", "9", "Initial Features"),
    ("📅", "1 Month", "Dataset Period"),
    ("🧭", "4", "Category Levels"),
    ("⚠️", "30,220", "Duplicates · 0.07%"),
    ("👆", "3", "Event Types · View · Cart · Purchase")
]

for col, (icon, value, label) in zip(
    [c1, c2, c3, c4, c5],
    cards_row2
):
    with col:
        st.markdown(
            f"""
            <div class="metric-card">
                <div>
                    <span class="metric-icon">{icon}</span>
                    <span class="metric-value">{value}</span>
                </div>
                <div class="metric-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
