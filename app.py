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
    margin-bottom: 8px;
}


/* ------------------------------------------------------------
   SECTION HEADER
------------------------------------------------------------ */

.section-container {
    margin-top: 12px;
    margin-bottom: 6px;
}

.dataset-heading {
    font-size: 22px;
    font-weight: 700;
    color: #E72F3D;
    margin: 0;
    padding: 0;
}

.section-caption {
    font-size: 12px;
    color: #777777;
    margin-top: 2px;
    margin-bottom: 4px;
}


/* ------------------------------------------------------------
   SPACE BETWEEN MAJOR SECTIONS
------------------------------------------------------------ */

.section-spacer {
    height: 24px;
}


/* ------------------------------------------------------------
   KPI INFORMATION
------------------------------------------------------------ */

.metric-card {
    background: transparent;
    border: none;
    padding: 3px 2px;
    min-height: 50px;
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


/* ------------------------------------------------------------
   SUBSECTION HEADINGS
------------------------------------------------------------ */

.subsection-heading {
    font-size: 15px;
    font-weight: 700;
    color: #E72F3D;
    margin-bottom: 6px;
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

st.caption(
    "Predicting purchase intent from customer browsing, cart, product, and session behavior."
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
            f'<div class="metric-card"><span class="metric-icon">{icon}</span><span class="metric-value">{value}</span><div class="metric-label">{label}</div></div>',
            unsafe_allow_html=True
        )


# ============================================================
# ROW 2 — DATASET INFORMATION
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
# SPACE BETWEEN MAJOR SECTIONS
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
# MISSING VALUE DATA
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


# ============================================================
# BRAND RECOVERY DATA
# ============================================================

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


# ============================================================
# DUPLICATE RECORD DATA
# ============================================================

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


# ============================================================
# MISSING VALUE TREATMENT DATA
# ============================================================

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

left, right = st.columns(2)


# ============================================================
# LEFT — MISSING VALUE ANALYSIS
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


    # ========================================================
    # BRAND METADATA RECOVERY
    # ========================================================

    st.markdown(
        '<div class="subsection-heading" style="margin-top:12px;">Brand Metadata Recovery</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        brand_recovery_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="cleaning-note"><b>Recovery Strategy:</b> Missing brand values were recovered where a reliable brand mapping existed for the same Product ID. This restored <b>172,423 records (2.82%)</b> without assigning synthetic brand information.</div>',
        unsafe_allow_html=True
    )


# ============================================================
# RIGHT — DUPLICATE RECORD ANALYSIS
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
        '<div class="cleaning-note"><b>Duplicate Treatment:</b> 30,220 exact duplicate interaction records were identified, representing only <b>0.07%</b> of the dataset. These records were removed before downstream analysis.</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # MISSING VALUE TREATMENT
    # ========================================================

    st.markdown(
        '<div class="subsection-heading" style="margin-top:12px;">Missing Value Treatment</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        treatment_table,
        use_container_width=True,
        hide_index=True
    )

# ============================================================
# SPACE BETWEEN MAJOR SECTIONS
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
            Derived temporal, behavioral, session, and purchase-intent features from raw customer interaction data.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FEATURE ENGINEERING TABLES
# ============================================================

feature_col1, feature_col2 = st.columns(2)


# ============================================================
# LEFT — TEMPORAL & BEHAVIORAL FEATURES
# ============================================================

with feature_col1:

    # --------------------------------------------------------
    # EVENT TIME FEATURES
    # --------------------------------------------------------

    st.markdown(
        '<div class="subsection-heading">🕒 Event Time Features</div>',
        unsafe_allow_html=True
    )

    time_features = pd.DataFrame({
        "Feature": [
            "year",
            "month / month_name",
            "day / date",
            "hour / minute",
            "day_of_week",
            "is_weekend",
            "week_of_year",
            "is_evening"
        ],
        "Purpose": [
            "Year-level activity",
            "Monthly behavior patterns",
            "Daily interaction trends",
            "Time-of-day behavior",
            "Weekday behavior",
            "Weekend activity indicator",
            "Weekly behavioral patterns",
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
        '<div class="subsection-heading" style="margin-top:12px;">👆 Behavioral Features</div>',
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
            "Cumulative product views",
            "Cumulative cart actions",
            "Cart conversion tendency",
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
# RIGHT — SESSION & PURCHASE INTENT FEATURES
# ============================================================

with feature_col2:

    # --------------------------------------------------------
    # SESSION FEATURES
    # --------------------------------------------------------

    st.markdown(
        '<div class="subsection-heading">⚡ Session & Intensity Features</div>',
        unsafe_allow_html=True
    )

    session_features = pd.DataFrame({
        "Feature": [
            "session_start",
            "elapsed_seconds",
            "previous_event",
            "seconds_since_previous_event",
            "session_activity_rate",
            "cart_intensity",
            "engagement_intensity"
        ],
        "Purpose": [
            "Session starting timestamp",
            "Time elapsed within session",
            "Previous customer action",
            "Time between interactions",
            "Interaction speed",
            "Cart activity concentration",
            "Weighted engagement level"
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
        '<div class="subsection-heading" style="margin-top:12px;">🎯 Purchase Intent Features</div>',
        unsafe_allow_html=True
    )

    intent_features = pd.DataFrame({
        "Feature": [
            "repeat_product_view",
            "previous_event_cart",
            "view_after_cart",
            "fast_session",
            "high_intent_no_cart"
        ],
        "Purpose": [
            "Repeated product consideration",
            "Recent cart intent",
            "Post-cart browsing behavior",
            "High-speed session indicator",
            "High views without cart action"
        ]
    })

    st.dataframe(
        intent_features,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# TARGET CREATION
# ============================================================

st.markdown(
    '<div class="subsection-heading" style="margin-top:14px;">🎯 Target Variable</div>',
    unsafe_allow_html=True
)

target_table = pd.DataFrame({
    "Target": [
        "purchase_later"
    ],
    "Definition": [
        "1 if a purchase occurs later within the same user session; otherwise 0"
    ],
    "Prediction Goal": [
        "Predict future purchase intent using behavior observed up to the current interaction"
    ]
})

st.dataframe(
    target_table,
    use_container_width=True,
    hide_index=True
)
