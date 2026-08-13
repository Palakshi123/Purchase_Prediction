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
# GLOBAL STYLING
# ============================================================

st.markdown("""
<style>

/* ------------------------------------------------------------
   MAIN PAGE
------------------------------------------------------------ */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}


/* ------------------------------------------------------------
   DASHBOARD HEADER
------------------------------------------------------------ */

.dashboard-title {
    font-size: 30px;
    font-weight: 700;
    color: #1F1F1F;
    margin-bottom: 2px;
}

.dashboard-subtitle {
    font-size: 14px;
    color: #6B6B6B;
    margin-bottom: 4px;
}

.dashboard-accent {
    width: 65px;
    height: 4px;
    background-color: #E72F3D;
    border-radius: 4px;
    margin-top: 10px;
    margin-bottom: 12px;
}


/* ------------------------------------------------------------
   DATASET INFORMATION HEADING
------------------------------------------------------------ */

.dataset-heading {
    font-size: 24px;
    font-weight: 700;
    color: #E72F3D;
    margin-top: 5px;
    margin-bottom: 2px;
}


/* ------------------------------------------------------------
   DATASET KPI INFORMATION
------------------------------------------------------------ */

.metric-card {
    background: transparent;
    border: none;
    padding: 4px 2px;
    min-height: 55px;
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
# DASHBOARD HEADER
# ============================================================

st.markdown("""
<div class="dashboard-title">
    🛒 E-Commerce Purchase Prediction
</div>

<div class="dashboard-subtitle">
    Customer Behavior Analytics & Machine Learning Dashboard
</div>

<div class="dashboard-accent"></div>
""", unsafe_allow_html=True)

st.caption(
    "Predicting purchase intent from customer browsing, cart, product, and session behavior."
)


# ============================================================
# DATASET INFORMATION
# ============================================================

st.divider()

st.markdown(
    '<div class="dataset-heading">Dataset Information</div>',
    unsafe_allow_html=True
)

st.caption(
    "One month of e-commerce behavioral data capturing View, Cart, and Purchase interactions."
)


# ============================================================
# ROW 1 — DATASET INFORMATION
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
# ROW 2 — DATASET INFORMATION
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

# ============================================================
# DATA QUALITY & CLEANING
# ============================================================

st.divider()

st.markdown(
    '<div class="dataset-heading">Data Quality & Cleaning</div>',
    unsafe_allow_html=True
)

st.caption(
    "Missing-value treatment, metadata recovery, and duplicate record analysis."
)


# ============================================================
# ROW 1 — MISSING VALUE HANDLING
# ============================================================

st.markdown(
    '<div style="font-size:13px; font-weight:600; margin-top:8px; margin-bottom:5px;">Missing Value Handling</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

missing_cards = [
    ("🏷️", "Product ID Mode", "Brand Recovery"),
    ("🗂️", "Product ID Mode", "Category Recovery"),
    ("♻️", "~85%", "Metadata Coverage"),
    ("🔍", "Validated", "Remaining Missing Values")
]

for col, (icon, value, label) in zip(
    [c1, c2, c3, c4],
    missing_cards
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
# ROW 2 — DUPLICATE RECORD ANALYSIS
# ============================================================

st.markdown(
    '<div style="font-size:13px; font-weight:600; margin-top:8px; margin-bottom:5px;">Duplicate Record Analysis</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

duplicate_cards = [
    ("⚠️", "30,220", "Duplicate Records"),
    ("📉", "0.07%", "Duplicate Rate"),
    ("✅", "Removed", "Duplicate Treatment")
]

for col, (icon, value, label) in zip(
    [c1, c2, c3],
    duplicate_cards
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
# CLEANING METHODOLOGY
# ============================================================

st.markdown(
    """
    <div style="
        font-size:11px;
        color:#666666;
        margin-top:8px;
        line-height:1.6;
    ">
    <b>Cleaning Strategy:</b>
    Missing brand and category metadata were recovered using the most frequent
    known value for the same Product ID, preserving product-level consistency
    while minimizing unnecessary row removal. Exact duplicate interaction
    records were identified and removed before downstream analysis.
    </div>
    """,
    unsafe_allow_html=True
)
