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
    padding-top: 1.8rem;
    padding-bottom: 2rem;
    max-width: 1450px;
}


/* ------------------------------------------------------------
   DASHBOARD HEADER
------------------------------------------------------------ */

.dashboard-title {
    font-size: 30px;
    font-weight: 700;
    color: #1F1F1F;
    margin: 0;
}

.dashboard-subtitle {
    font-size: 14px;
    color: #6B6B6B;
    margin-top: 2px;
}

.dashboard-description {
    font-size: 12px;
    color: #777777;
    margin-top: 5px;
}

.dashboard-accent {
    width: 65px;
    height: 4px;
    background-color: #E72F3D;
    border-radius: 5px;
    margin-top: 9px;
    margin-bottom: 5px;
}


/* ------------------------------------------------------------
   MAJOR SECTION
------------------------------------------------------------ */

.section-container {
    margin-top: 12px;
    margin-bottom: 8px;
}

.dataset-heading {
    font-size: 22px;
    font-weight: 700;
    color: #E72F3D;
    margin: 0;
}

.section-caption {
    font-size: 12px;
    color: #777777;
    margin-top: 2px;
}


/* ------------------------------------------------------------
   SPACING
------------------------------------------------------------ */

.section-spacer {
    height: 26px;
}

.kpi-table-spacer {
    height: 35px;
}


/* ------------------------------------------------------------
   KPI INFORMATION
------------------------------------------------------------ */

.metric-card {
    background: transparent;
    border: none;
    padding: 5px 3px;
    min-height: 52px;
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
    margin-top: 3px;
}


/* ------------------------------------------------------------
   SUBSECTION HEADINGS
------------------------------------------------------------ */

.subsection-heading {
    font-size: 15px;
    font-weight: 700;
    color: #E72F3D;
    margin-bottom: 7px;
}


/* ------------------------------------------------------------
   CLEANING NOTES
------------------------------------------------------------ */

.cleaning-note {
    font-size: 11px;
    color: #666666;
    margin-top: 8px;
    line-height: 1.6;
}


/* ------------------------------------------------------------
   FEATURE GROUP LABEL
------------------------------------------------------------ */

.feature-group-label {
    display: inline-block;
    font-size: 10px;
    font-weight: 600;
    color: #E72F3D;
    background-color: rgba(231, 47, 61, 0.07);
    border-radius: 12px;
    padding: 3px 8px;
    margin-bottom: 8px;
}


/* ------------------------------------------------------------
   TARGET VARIABLE
------------------------------------------------------------ */

.target-box {
    background-color: rgba(231, 47, 61, 0.04);
    border-left: 3px solid #E72F3D;
    border-radius: 5px;
    padding: 10px 14px;
    margin-top: 18px;
}

.target-name {
    color: #E72F3D;
    font-size: 14px;
    font-weight: 700;
}

.target-description {
    color: #666666;
    font-size: 11px;
    margin-top: 3px;
    line-height: 1.5;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DASHBOARD HEADER
# ============================================================

st.markdown(
    '<div class="dashboard-title">🛒 E-Commerce Purchase Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">Customer Behavior Analytics & Machine Learning Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-accent"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-description">Predicting purchase intent from customer browsing, cart, product, and session behavior.</div>',
    unsafe_allow_html=True
)


# ============================================================
# DATASET INFORMATION
# ============================================================

st.markdown(
    """
    <div class="section-container">
        <div class="dataset-heading">Dataset Information</div>
        <div class="section-caption">
            One month of e-commerce behavioral data capturing View, Cart, and Purchase interactions.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATASET KPI — ROW 1
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
            f'<div class="metric-card"><span class="metric-icon">{icon}</span><span class="metric-value">{value}</span><div class="metric-label">{label}</div></div>',
            unsafe_allow_html=True
        )


# ============================================================
# DATASET KPI — ROW 2
# ============================================================

c1, c2, c3, c4 = st.columns(4)

cards_row2 = [
    ("🔢", "9", "Initial Features"),
    ("📅", "1 Month", "Dataset Period"),
    ("🧭", "4", "Category Levels"),
    ("👆", "3", "Event Types · View · Cart · Purchase")
]

for col, (icon, value, label) in zip(
    [c1, c2, c3, c4],
    cards_row2
):
    with col:
        st.markdown(
            f'<div class="metric-card"><span class="metric-icon">{icon}</span><span class="metric-value">{value}</span><div class="metric-label">{label}</div></div>',
            unsafe_allow_html=True
        )


# ============================================================
# SPACE BETWEEN SECTIONS
# ============================================================

st.markdown(
    '<div class="section-spacer"></div>',
    unsafe_allow_html=True
)


# ============================================================
# MISSING VALUE & DUPLICATE RECORDS ANALYSIS
# ============================================================

st.markdown(
    """
    <div class="section-container">
        <div class="dataset-heading">
            Missing Value & Duplicate Records Analysis
        </div>
        <div class="section-caption">
            Assessment of missing values, recoverable product metadata, and duplicate records.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATA QUALITY TABLES
# ============================================================

missing_table = pd.DataFrame({
    "Column": [
        "category_code",
        "brand",
        "user_session"
    ],
    "Missing Records": [
        "13,515,609",
        "6,117,080",
        "2"
    ],
    "Missing %": [
        "31.84%",
        "14.41%",
        "0.00%"
    ]
})


brand_recovery_table = pd.DataFrame({
    "Metric": [
        "Missing Before Recovery",
        "Recovered Brand Values",
        "Remaining Missing",
        "Recovery Rate"
    ],
    "Value": [
        "6,117,080",
        "172,423",
        "5,944,657",
        "2.82%"
    ]
})


duplicate_table = pd.DataFrame({
    "Metric": [
        "Duplicate Records",
        "Duplicate Rate",
        "Treatment"
    ],
    "Value": [
        "30,220",
        "0.07%",
        "Removed"
    ]
})


treatment_table = pd.DataFrame({
    "Data Issue": [
        "Brand",
        "Category Code",
        "User Session"
    ],
    "Treatment": [
        "Recover using Product ID",
        "Retain / handle downstream",
        "Remove 2 records"
    ]
})


# ============================================================
# SIDE-BY-SIDE DATA QUALITY ANALYSIS
# ============================================================

left, right = st.columns(2, gap="large")


# ============================================================
# LEFT — MISSING VALUES
# ============================================================

with left:

    st.markdown(
        '<div class="subsection-heading">Missing Value Analysis</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        missing_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="subsection-heading" style="margin-top:14px;">Brand Metadata Recovery</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        brand_recovery_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="cleaning-note"><b>Recovery Strategy:</b> Missing brand values were recovered where a reliable brand mapping existed for the same Product ID. This restored <b>172,423 records (2.82%)</b> without introducing synthetic brand information.</div>',
        unsafe_allow_html=True
    )


# ============================================================
# RIGHT — DUPLICATES
# ============================================================

with right:

    st.markdown(
        '<div class="subsection-heading">Duplicate Record Analysis</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        duplicate_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="cleaning-note"><b>Duplicate Treatment:</b> 30,220 exact duplicate interaction records were identified, representing <b>0.07%</b> of the dataset, and removed before downstream analysis.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subsection-heading" style="margin-top:14px;">Missing Value Treatment</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        treatment_table,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# SPACE BETWEEN SECTIONS
# ============================================================

st.markdown(
    '<div class="section-spacer"></div>',
    unsafe_allow_html=True
)


# ============================================================
# FEATURE ENGINEERING
# ============================================================

st.markdown(
    """
    <div class="section-container">
        <div class="dataset-heading">
            Feature Engineering
        </div>
        <div class="section-caption">
            Created behavioral, temporal, session, and purchase-intent signals from raw customer interactions.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FEATURE ENGINEERING KPI SUMMARY
# ============================================================

c1, c2, c3, c4, c5 = st.columns(5)

feature_summary = [
    ("🧩", "24", "Predictor Features"),
    ("🕒", "4", "Temporal Features"),
    ("👆", "7", "Behavioral Features"),
    ("⚡", "9", "Session Features"),
    ("🎯", "4", "Purchase Intent Features")
]

for col, (icon, value, label) in zip(
    [c1, c2, c3, c4, c5],
    feature_summary
):
    with col:
        st.markdown(
            f'<div class="metric-card"><span class="metric-icon">{icon}</span><span class="metric-value">{value}</span><div class="metric-label">{label}</div></div>',
            unsafe_allow_html=True
        )


# ============================================================
# LARGER SPACE BETWEEN KPI AND TABLES
# ============================================================

st.markdown(
    '<div class="kpi-table-spacer"></div>',
    unsafe_allow_html=True
)


# ============================================================
# FEATURE TABLES
# ============================================================

feature_col1, feature_col2 = st.columns(2, gap="large")


# ============================================================
# LEFT — TEMPORAL & BEHAVIORAL
# ============================================================

with feature_col1:

    # --------------------------------------------------------
    # TEMPORAL FEATURES
    # --------------------------------------------------------

    st.markdown(
        '<div class="subsection-heading">🕒 Temporal Features</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="feature-group-label">4 retained features</div>',
        unsafe_allow_html=True
    )

    time_features = pd.DataFrame({
        "Feature": [
            "hour",
            "day_of_week",
            "is_weekend",
            "is_evening"
        ],
        "Purpose": [
            "Hourly shopping behavior",
            "Day-specific behavioral patterns",
            "Weekend activity indicator",
            "Evening shopping indicator"
        ]
    })

    st.dataframe(
        time_features,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # BEHAVIORAL FEATURES
    # --------------------------------------------------------

    st.markdown(
        '<div class="subsection-heading" style="margin-top:18px;">👆 Behavioral Features</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="feature-group-label">7 retained features</div>',
        unsafe_allow_html=True
    )

    behavioral_features = pd.DataFrame({
        "Feature": [
            "events_so_far",
            "views_so_far",
            "carts_so_far",
            "cart_to_view_ratio",
            "product_views_so_far",
            "category_events_so_far",
            "brand_events_so_far"
        ],
        "Purpose": [
            "Session activity depth",
            "Cumulative views",
            "Cumulative cart actions",
            "Cart-to-view conversion tendency",
            "Repeated product interest",
            "Category engagement",
            "Brand engagement"
        ]
    })

    st.dataframe(
        behavioral_features,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# RIGHT — SESSION & PURCHASE INTENT
# ============================================================

with feature_col2:

    # --------------------------------------------------------
    # SESSION FEATURES
    # --------------------------------------------------------

    st.markdown(
        '<div class="subsection-heading">⚡ Session & Intensity Features</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="feature-group-label">9 retained features</div>',
        unsafe_allow_html=True
    )

    session_features = pd.DataFrame({
        "Feature": [
            "session_start",
            "elapsed_seconds",
            "previous_event",
            "previous_event_time",
            "seconds_since_previous_event",
            "session_activity_rate",
            "cart_intensity",
            "engagement_intensity",
            "fast_session"
        ],
        "Purpose": [
            "Session starting timestamp",
            "Elapsed session duration",
            "Previous customer action",
            "Previous interaction timestamp",
            "Time between interactions",
            "Interaction speed",
            "Cart activity concentration",
            "Weighted engagement intensity",
            "Fast-session indicator"
        ]
    })

    st.dataframe(
        session_features,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # PURCHASE INTENT FEATURES
    # --------------------------------------------------------

    st.markdown(
        '<div class="subsection-heading" style="margin-top:18px;">🎯 Purchase Intent Features</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="feature-group-label">4 retained features</div>',
        unsafe_allow_html=True
    )

    intent_features = pd.DataFrame({
        "Feature": [
            "repeat_product_view",
            "previous_event_cart",
            "view_after_cart",
            "high_intent_no_cart"
        ],
        "Purpose": [
            "Repeated product consideration",
            "Recent cart intent",
            "Post-cart browsing behavior",
            "High views without cart action"
        ]
    })

    st.dataframe(
        intent_features,
        use_container_width=True,
        hide_index=True
    )

# ============================================================
# TARGET VARIABLE
# ============================================================

st.markdown(
    '<div class="target-box"><div class="target-name">🎯 Target Variable — purchase_later</div><div class="target-description">Binary target indicating whether a purchase occurs later within the same user session. The model uses customer behavior observed up to the current interaction to predict future purchase intent.</div></div>',
    unsafe_allow_html=True
)

# ============================================================
# SPACE BETWEEN SECTIONS
# ============================================================

st.markdown(
    '<div class="section-spacer"></div>',
    unsafe_allow_html=True
)


# ============================================================
# UNIVARIATE / BIVARIATE / MULTIVARIATE ANALYSIS
# ============================================================

from pathlib import Path

st.divider()

st.markdown("## 📊 Univariate, Bivariate & Multivariate Analysis")

st.caption(
    "Exploratory visualizations uncovering customer behavior, purchase patterns, "
    "session dynamics, product engagement, and relationships between key features."
)

st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# IMAGE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"


# ============================================================
# IMAGE DISPLAY FUNCTION
# ============================================================

def show_eda_image(filename, caption=None):

    image_path = IMAGE_DIR / filename

    if image_path.exists():

        st.image(
            str(image_path),
            use_container_width=True
        )

        if caption:
            st.caption(caption)

    else:
        st.warning(f"Visualization not found: {filename}")

    st.markdown("<br><br>", unsafe_allow_html=True)


# ============================================================
# UNIVARIATE ANALYSIS
# ============================================================

st.markdown("### 🔹 Univariate Analysis")

st.caption(
    "Understanding the distribution and individual behavior of key variables."
)

st.markdown("<br>", unsafe_allow_html=True)

show_eda_image(
    "event_distribution.png",
    "Distribution of customer interaction events across the dataset."
)

show_eda_image(
    "price_distribution.png",
    "Distribution of product prices across customer interactions."
)


# ============================================================
# BIVARIATE ANALYSIS
# ============================================================

st.markdown("### 🔹 Bivariate Analysis")

st.caption(
    "Examining relationships between customer behavior and purchase outcomes."
)

st.markdown("<br>", unsafe_allow_html=True)

show_eda_image(
    "session_distribution.png",
    "Comparison of purchase and non-purchase sessions."
)

show_eda_image(
    "conversion_funnel.png",
    "Customer progression through the View → Cart → Purchase funnel."
)

show_eda_image(
    "session_duration.png",
    "Comparison of session duration between purchase and non-purchase sessions."
)

show_eda_image(
    "repeat_customer_conversion.png",
    "Purchase conversion behavior for repeat and one-session customers."
)


# ============================================================
# MULTIVARIATE ANALYSIS
# ============================================================

st.markdown("### 🔹 Multivariate Analysis")

st.caption(
    "Exploring interactions among multiple behavioral and session-level features."
)

st.markdown("<br>", unsafe_allow_html=True)

show_eda_image(
    "correlation_heatmap.png",
    "Correlation structure across engineered behavioral features."
)

show_eda_image(
    "purchase_behavior.png",
    "Combined behavioral patterns associated with future purchase intent."
)
