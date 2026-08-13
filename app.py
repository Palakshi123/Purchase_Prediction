# ============================================================
# IMPORTS
# ============================================================

import streamlit as st
import pandas as pd


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
    "Assessment of missing values, recoverable product metadata, and duplicate records."
)


# ============================================================
# CALCULATE MISSING VALUES
# ============================================================

total_records = len(df)

missing_count = df.isnull().sum()
missing_pct = (missing_count / total_records) * 100

missing_table = (
    missing_count[missing_count > 0]
    .reset_index()
)

missing_table.columns = [
    "Column",
    "Missing Records"
]

missing_table["Missing %"] = (
    missing_table["Missing Records"] / total_records * 100
).round(2)

missing_table["Missing Records"] = (
    missing_table["Missing Records"]
    .map(lambda x: f"{x:,}")
)

missing_table["Missing %"] = (
    missing_table["Missing %"]
    .map(lambda x: f"{x:.2f}%")
)


# ============================================================
# RECOVERABLE BRAND ANALYSIS
# ============================================================

product_brand_lookup = (
    df.dropna(subset=["brand"])
    .groupby("product_id")["brand"]
    .agg(lambda x: x.mode().iloc[0])
)

missing_brand_mask = df["brand"].isna()

recoverable_brand_mask = (
    missing_brand_mask
    & df["product_id"].isin(product_brand_lookup.index)
)

missing_brand_records = missing_brand_mask.sum()

recoverable_brand_records = recoverable_brand_mask.sum()

recoverable_brand_pct = (
    recoverable_brand_records / missing_brand_records * 100
    if missing_brand_records > 0
    else 0
)


# ============================================================
# DUPLICATE ANALYSIS
# ============================================================

duplicate_count = df.duplicated().sum()

duplicate_percentage = (
    duplicate_count / total_records
) * 100

unique_records = total_records - duplicate_count


duplicate_table = pd.DataFrame({
    "Metric": [
        "Total Records",
        "Duplicate Records",
        "Unique Records"
    ],
    "Records": [
        f"{total_records:,}",
        f"{duplicate_count:,}",
        f"{unique_records:,}"
    ],
    "Percentage": [
        "100.00%",
        f"{duplicate_percentage:.2f}%",
        f"{100 - duplicate_percentage:.2f}%"
    ]
})


# ============================================================
# SIDE-BY-SIDE ANALYSIS
# ============================================================

left, right = st.columns(2)


# ============================================================
# LEFT — MISSING VALUE ANALYSIS
# ============================================================

with left:

    st.markdown(
        """
        <div style="
            font-size:15px;
            font-weight:700;
            color:#E72F3D;
            margin-bottom:8px;
        ">
        Missing Value Analysis
        </div>
        """,
        unsafe_allow_html=True
    )

    st.dataframe(
        missing_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        f"""
        <div style="
            font-size:12px;
            margin-top:10px;
            line-height:1.7;
        ">
        <b>Brand Recovery:</b><br>
        Missing Brand Records:
        <span style="color:#E72F3D; font-weight:700;">
        {missing_brand_records:,}
        </span><br>

        Recoverable Brand Records:
        <span style="color:#E72F3D; font-weight:700;">
        {recoverable_brand_records:,}
        </span><br>

        Recoverable:
        <span style="color:#E72F3D; font-weight:700;">
        {recoverable_brand_pct:.2f}%
        </span>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# RIGHT — DUPLICATE RECORD ANALYSIS
# ============================================================

with right:

    st.markdown(
        """
        <div style="
            font-size:15px;
            font-weight:700;
            color:#E72F3D;
            margin-bottom:8px;
        ">
        Duplicate Record Analysis
        </div>
        """,
        unsafe_allow_html=True
    )

    st.dataframe(
        duplicate_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        """
        <div style="
            font-size:12px;
            color:#666666;
            margin-top:10px;
            line-height:1.6;
        ">
        <b>Treatment:</b> Exact duplicate interaction records were removed
        before feature engineering and predictive modeling.
        </div>
        """,
        unsafe_allow_html=True
    )
