# ============================================================
# IMPORTS
# ============================================================

import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="E-Commerce Purchase Prediction",
    page_icon="🛒",
    layout="wide"
)


# ============================================================
# DATASET INFORMATION — COMPACT
# ============================================================

st.divider()

st.markdown("## Dataset Information")

st.caption(
    "One month of e-commerce behavioral data capturing View, Cart, and Purchase interactions."
)


# ============================================================
# CLEAN KPI STYLING
# ============================================================

st.markdown("""
<style>

.metric-card {
    background: transparent;
    border: none;
    padding: 5px 4px;
    min-height: 58px;
    text-align: center;
}

.metric-icon {
    font-size: 13px;
    display: inline;
}

.metric-value {
    font-size: 15px;
    font-weight: 700;
    color: #E72F3D;
    display: inline;
    margin-left: 3px;
}

.metric-label {
    font-size: 10px;
    color: #777777;
    margin-top: 2px;
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
