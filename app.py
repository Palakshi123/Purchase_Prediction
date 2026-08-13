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
# EXPLORATORY DATA ANALYSIS
# ============================================================

st.markdown(
    """
    <div class="section-container">
        <div class="dataset-heading">
            Exploratory Data Analysis
        </div>
        <div class="section-caption">
            Univariate, bivariate, and multivariate exploration of customer activity, session behavior, and purchase patterns.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SMALL SPACE BEFORE TABS
# ============================================================

st.markdown(
    '<div style="height:12px;"></div>',
    unsafe_allow_html=True
)


# ============================================================
# EDA TABS
# ============================================================

tab1, tab2, tab3 = st.tabs([
    "📊 Univariate Analysis",
    "🔗 Bivariate Analysis",
    "🧠 Multivariate Analysis"
])


# ============================================================
# TAB 1 — UNIVARIATE ANALYSIS
# ============================================================

with tab1:

    st.markdown(
        '<div style="height:15px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subsection-heading">Customer Activity Distribution</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="cleaning-note">Analysis of individual customer interaction variables and their underlying distributions.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="height:18px;"></div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # ROW 1 — EVENT DISTRIBUTION + DAY OF WEEK
    # ========================================================

    uni1, uni2 = st.columns(2, gap="large")

    with uni1:

        st.markdown(
            '<div class="subsection-heading">Event Type Distribution</div>',
            unsafe_allow_html=True
        )

        st.image(
            "event_distribution.png",
            use_container_width=True
        )

        st.markdown(
            '<div class="cleaning-note"><b>Insight:</b> Views dominate customer interactions, while cart and purchase events represent only a small proportion of total activity.</div>',
            unsafe_allow_html=True
        )


    with uni2:

        st.markdown(
            '<div class="subsection-heading">Activity by Day of Week</div>',
            unsafe_allow_html=True
        )

        st.image(
            "day_of_week.png",
            use_container_width=True
        )

        st.markdown(
            '<div class="cleaning-note"><b>Insight:</b> Customer activity is strongest during the middle of the week, with Tuesday recording the highest interaction volume.</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # SPACE BETWEEN ROWS
    # ========================================================

    st.markdown(
        '<div style="height:25px;"></div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # ROW 2 — WEEKEND + TIME TO PURCHASE
    # ========================================================

    uni3, uni4 = st.columns(2, gap="large")

    with uni3:

        st.markdown(
            '<div class="subsection-heading">Weekend vs Weekday Activity</div>',
            unsafe_allow_html=True
        )

        st.image(
            "weekend_weekday.png",
            use_container_width=True
        )

        st.markdown(
            '<div class="cleaning-note"><b>Insight:</b> Most customer interactions occur on weekdays, indicating stronger shopping activity during the working week.</div>',
            unsafe_allow_html=True
        )


    with uni4:

        st.markdown(
            '<div class="subsection-heading">Time to First Purchase</div>',
            unsafe_allow_html=True
        )

        st.image(
            "time_first_purchase.png",
            use_container_width=True
        )

        st.markdown(
            '<div class="cleaning-note"><b>Insight:</b> First purchases are heavily concentrated near the beginning of a session, with frequency declining rapidly as session time increases.</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # SPACE BETWEEN ROWS
    # ========================================================

    st.markdown(
        '<div style="height:25px;"></div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # ROW 3 — EVENTS BEFORE PURCHASE
    # ========================================================

    uni5, uni6 = st.columns(2, gap="large")

    with uni5:

        st.markdown(
            '<div class="subsection-heading">Events Before First Purchase</div>',
            unsafe_allow_html=True
        )

        st.image(
            "events_before_purchase.png",
            use_container_width=True
        )

        st.markdown(
            '<div class="cleaning-note"><b>Insight:</b> Purchasing sessions typically require only a small number of interactions before conversion, while long pre-purchase journeys are less common.</div>',
            unsafe_allow_html=True
        )


    with uni6:

        st.markdown(
            '<div style="height:45px;"></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="target-box"><div class="target-name">📊 Univariate Summary</div><div class="target-description">Customer behavior is strongly view-dominated, activity is higher during weekdays, and purchasing behavior is concentrated early in the customer session. These distributions indicate substantial behavioral differences across the shopping journey.</div></div>',
            unsafe_allow_html=True
        )


# ============================================================
# TAB 2 — BIVARIATE ANALYSIS
# ============================================================

with tab2:

    st.markdown(
        '<div style="height:15px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subsection-heading">Purchase Relationship Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="cleaning-note">Analysis of relationships between customer characteristics, interaction behavior, and purchase outcomes.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="height:18px;"></div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # ROW 1 — PURCHASE SESSIONS + PRICE
    # ========================================================

    bi1, bi2 = st.columns(2, gap="large")

    with bi1:

        st.markdown(
            '<div class="subsection-heading">Purchase vs No-Purchase Sessions</div>',
            unsafe_allow_html=True
        )

        st.image(
            "purchase_sessions.png",
            use_container_width=True
        )

        st.markdown(
            '<div class="cleaning-note"><b>Insight:</b> Only 6.78% of sessions result in a purchase, confirming a strongly imbalanced prediction problem.</div>',
            unsafe_allow_html=True
        )


    with bi2:

        st.markdown(
            '<div class="subsection-heading">Price Distribution by Event Type</div>',
            unsafe_allow_html=True
        )

        st.image(
            "price_event_type.png",
            use_container_width=True
        )

        st.markdown(
            '<div class="cleaning-note"><b>Insight:</b> Cart interactions tend to involve somewhat higher-priced products, while substantial price variability exists across all event types.</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # SPACE BETWEEN ROWS
    # ========================================================

    st.markdown(
        '<div style="height:25px;"></div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # ROW 2 — REPEAT CUSTOMER CONVERSION
    # ========================================================

    bi3, bi4 = st.columns(2, gap="large")

    with bi3:

        st.markdown(
            '<div class="subsection-heading">Repeat vs One-Session User Conversion</div>',
            unsafe_allow_html=True
        )

        st.image(
            "repeat_conversion.png",
            use_container_width=True
        )

        st.markdown(
            '<div class="cleaning-note"><b>Insight:</b> Repeat users convert at 16.72% compared with 4.79% for one-session users, demonstrating a strong relationship between repeat engagement and purchase behavior.</div>',
            unsafe_allow_html=True
        )


    with bi4:

        st.markdown(
            '<div style="height:45px;"></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="target-box"><div class="target-name">🔗 Bivariate Summary</div><div class="target-description">Purchase behavior is highly imbalanced, while repeat customer engagement shows a substantially stronger relationship with conversion. Product price also varies across interaction stages, suggesting that customer behavior and product characteristics jointly influence purchase outcomes.</div></div>',
            unsafe_allow_html=True
        )


# ============================================================
# TAB 3 — MULTIVARIATE ANALYSIS
# ============================================================

with tab3:

    st.markdown(
        '<div style="height:15px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subsection-heading">Combined Behavioral Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="cleaning-note">Analysis of multiple behavioral signals simultaneously to understand how combinations of customer actions differentiate purchasing and non-purchasing sessions.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="height:18px;"></div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # SESSION BEHAVIOR
    # ========================================================

    multi1, multi2 = st.columns([1.5, 1], gap="large")

    with multi1:

        st.markdown(
            '<div class="subsection-heading">Average Session Behavior: Purchase vs No Purchase</div>',
            unsafe_allow_html=True
        )

        st.image(
            "session_behavior.png",
            use_container_width=True
        )


    with multi2:

        st.markdown(
            '<div style="height:45px;"></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="target-box"><div class="target-name">🧠 Multivariate Insight</div><div class="target-description">Purchasing sessions demonstrate stronger combined engagement. Average views increase from 4.44 to 5.61, while average cart activity rises dramatically from 0.05 to 0.78. The interaction between browsing depth and cart behavior therefore provides a much stronger purchase-intent signal than either behavior considered independently.</div></div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # FINAL EDA TAKEAWAY
    # ========================================================

    st.markdown(
        '<div style="height:20px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="target-box"><div class="target-name">🎯 Modeling Takeaway</div><div class="target-description">EDA indicates that purchase prediction should emphasize behavioral progression rather than isolated events. Cart activity, repeated engagement, interaction depth, session timing, and customer history provide meaningful signals for distinguishing high-intent sessions from the majority of non-purchasing sessions.</div></div>',
        unsafe_allow_html=True
    )
