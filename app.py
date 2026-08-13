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
# EXPLORATORY DATA ANALYSIS — VISUALIZATIONS
# ============================================================

from pathlib import Path

st.markdown(
    """
    <div class="section-container">
        <div class="dataset-heading">
            Exploratory Data Analysis
        </div>
        <div class="section-caption">
            Explore customer behavior, purchase patterns, session activity,
            and temporal trends by selecting a visualization below.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# IMAGE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"


# ============================================================
# VISUALIZATION OPTIONS
# ============================================================

eda_visualizations = {

    "Event Distribution":
        "event_distribution.png",

    "Purchase vs No-Purchase Sessions":
        "purchase_sessions.png",

    "Repeat Customer Conversion":
        "repeat_conversion.png",

    "Customer Activity by Day of Week":
        "day_of_week.png",

    "Weekend vs Weekday Behavior":
        "weekend_weekday.png",

    "Price by Event Type":
        "price_event_type.png",

    "Session Behavior":
        "session_behavior.png",

    "Events Before Purchase":
        "events_before_purchase.png",

    "Time to First Purchase":
        "time_first_purchase.png"
}


# ============================================================
# BUSINESS INSIGHTS
# ============================================================

business_insights = {

    "Event Distribution":
        "Product views dominate customer activity, while purchases represent a much smaller share of interactions.",

    "Purchase vs No-Purchase Sessions":
        "Most customer sessions do not result in a purchase, highlighting a significant conversion opportunity.",

    "Repeat Customer Conversion":
        "Repeat customers demonstrate stronger purchase intent than one-session customers.",

    "Customer Activity by Day of Week":
        "Tuesday records the highest purchase activity, making it a key day for targeted promotions.",

    "Weekend vs Weekday Behavior":
        "Weekday activity is higher than weekend activity, indicating stronger customer engagement during the workweek.",

    "Price by Event Type":
        "Purchased products are concentrated within a narrower price range than products customers only view.",

    "Session Behavior":
        "Customers who purchase demonstrate higher session engagement than customers who leave without purchasing.",

    "Events Before Purchase":
        "Purchase likelihood increases as customers interact with more events during a session.",

    "Time to First Purchase":
        "Most purchases occur relatively early in the session, suggesting that purchase intent develops quickly."
}


# ============================================================
# VISUALIZATION DROPDOWN
# ============================================================

selected_visualization = st.selectbox(
    "Select an analysis",
    options=list(eda_visualizations.keys())
)

selected_file = eda_visualizations[selected_visualization]
image_path = IMAGE_DIR / selected_file


# ============================================================
# VISUALIZATION + BUSINESS INSIGHT
# ============================================================

if image_path.exists():

    left, center, right = st.columns([1.5, 2, 1.5])

    with center:

        st.markdown(
            f'<div class="subsection-heading" style="text-align:center;">'
            f'{selected_visualization}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.image(
            str(image_path),
            width=450
        )

else:

    st.warning(
        f"Visualization not found: {selected_file}"
    )


# ============================================================
# BUSINESS INSIGHT
# ============================================================

st.markdown(
    f"""
    <div class="target-box" style="margin-top:8px;">
        <div class="target-name">
            💡 Business Insight
        </div>
        <div class="target-description">
            {business_insights[selected_visualization]}
        </div>
    </div>
    """,
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
# TEXT ENRICHMENT & LLM INTEGRATION
# ============================================================

st.markdown(
    """
    <div class="section-container">
        <div class="dataset-heading">
            Text Enrichment & LLM Integration
        </div>
        <div class="section-caption">
            Generating semantic product descriptions from structured metadata
            to introduce richer product context into the modeling pipeline.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# WHY TEXT ENRICHMENT
# ============================================================

st.markdown(
    '<div class="subsection-heading" style="margin-top:18px;">Why Text Enrichment?</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="
        font-size:13px;
        color:#555555;
        line-height:1.8;
        margin-top:5px;
        margin-bottom:20px;
    ">
        • <b>product_id</b> and <b>category_id</b> are high-cardinality identifiers with little inherent semantic meaning.<br>
        • <b>category_code</b> provides product-category context but does not fully describe the individual product.<br>
        • <b>brand</b> identifies the manufacturer but provides limited information about product characteristics.<br>
        • Product descriptions combine available structured metadata into a richer natural-language representation.<br>
        • Generated descriptions can be transformed into numerical semantic features for machine-learning experiments.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TEXT ENRICHMENT PIPELINE
# ============================================================

st.markdown(
    '<div class="subsection-heading" style="margin-top:18px;">Text Enrichment Pipeline</div>',
    unsafe_allow_html=True
)

pipeline_image = IMAGE_DIR / "text_enrichment_pipeline.png"

if pipeline_image.exists():

    pipeline_left, pipeline_center, pipeline_right = st.columns(
        [0.3, 4.4, 0.3]
    )

    with pipeline_center:

        st.image(
            str(pipeline_image),
            use_container_width=True
        )

else:

    st.warning(
        "Text enrichment pipeline image not found."
    )


# ============================================================
# LLM APPROACH — OPTIONS CONSIDERED
# ============================================================

st.markdown(
    '<div class="subsection-heading" style="margin-top:22px;">LLM Approach — Options Considered</div>',
    unsafe_allow_html=True
)

llm_col1, llm_col2, llm_col3 = st.columns(
    3,
    gap="large"
)


# ============================================================
# OPTION 1 — LOCAL SMALL LLM
# ============================================================

with llm_col1:

    st.markdown(
        '<div class="feature-group-label">LOCAL SMALL LLM</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            font-size:12px;
            color:#555555;
            line-height:1.8;
        ">
            • Download and run an open-source LLM locally<br>
            • No per-request API cost<br>
            • Greater control over local inference<br>
            • Limited by available RAM and compute<br>
            • Smaller models may reduce description quality<br>
            • Large-scale generation can be slower
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# OPTION 2 — LARGE CLOUD LLM
# ============================================================

with llm_col2:

    st.markdown(
        '<div class="feature-group-label">LARGE CLOUD LLM</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            font-size:12px;
            color:#555555;
            line-height:1.8;
        ">
            • Strong language-generation capability<br>
            • Better suited for complex reasoning tasks<br>
            • Higher API cost at large scale<br>
            • Higher token consumption<br>
            • More capability than required for this task<br>
            • Lower cost-efficiency for simple descriptions
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# OPTION 3 — OPENAI API
# ============================================================

with llm_col3:

    st.markdown(
        '<div class="feature-group-label">✓ SELECTED — OPENAI API</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            font-size:12px;
            color:#555555;
            line-height:1.8;
        ">
            • Lightweight and cost-efficient model<br>
            • Sufficient quality for product descriptions<br>
            • No local compute dependency<br>
            • Easy API-based integration<br>
            • Supports automated batch generation<br>
            • Strong cost–quality–scalability trade-off
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FINAL SELECTION
# ============================================================

st.markdown(
    """
    <div class="target-box" style="margin-top:20px;">

        <div class="target-name">
            ✓ Final Selection
        </div>

        <div class="target-description" style="
            font-size:12px;
            line-height:1.8;
        ">
            • Product description generation is primarily a structured text-generation task rather than a complex reasoning problem.<br>
            • A large premium LLM would increase cost without providing proportional value for this use case.<br>
            • A small local LLM avoids API costs but introduces local compute, memory, and generation-speed constraints.<br>
            • A lightweight OpenAI API model provided the best balance of <b>cost, quality, scalability, and inference speed</b>.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# EXAMPLE ENRICHMENT
# ============================================================

st.markdown(
    '<div class="subsection-heading" style="margin-top:22px;">Example Enrichment</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="
        border:1px solid rgba(231,47,61,0.35);
        border-left:3px solid #E72F3D;
        border-radius:7px;
        padding:16px 20px;
        margin-top:5px;
        margin-bottom:18px;
        background-color:rgba(231,47,61,0.025);
    ">

        <div style="
            display:grid;
            grid-template-columns:1fr 1fr;
            gap:40px;
        ">

            <div>

                <div style="
                    font-size:11px;
                    font-weight:700;
                    color:#E72F3D;
                    margin-bottom:10px;
                ">
                    STRUCTURED PRODUCT METADATA
                </div>

                <div style="
                    font-size:13px;
                    color:#555555;
                    line-height:1.8;
                ">
                    • <b>Product ID:</b> 1004856<br>
                    • <b>Category:</b> electronics.smartphone<br>
                    • <b>Brand:</b> Samsung
                </div>

            </div>


            <div>

                <div style="
                    font-size:11px;
                    font-weight:700;
                    color:#E72F3D;
                    margin-bottom:10px;
                ">
                    LLM-GENERATED DESCRIPTION
                </div>

                <div style="
                    font-size:13px;
                    color:#555555;
                    line-height:1.8;
                ">
                    • Samsung smartphone in the consumer electronics category,
                    designed for mobile communication and everyday digital use.
                </div>

            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TEXT FEATURE ENGINEERING
# ============================================================

st.markdown(
    '<div class="subsection-heading" style="margin-top:20px;">Text Feature Engineering</div>',
    unsafe_allow_html=True
)

text_col1, text_col2, text_col3 = st.columns(
    3,
    gap="large"
)


# ============================================================
# GENERATED DESCRIPTION
# ============================================================

with text_col1:

    st.markdown(
        '<div class="feature-group-label">GENERATED DESCRIPTION</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            font-size:12px;
            color:#555555;
            line-height:1.8;
        ">
            • Introduces semantic product information<br>
            • Combines multiple metadata attributes<br>
            • Creates a human-readable product representation<br>
            • Adds context unavailable from IDs alone
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# TF-IDF
# ============================================================

with text_col2:

    st.markdown(
        '<div class="feature-group-label">TF-IDF VECTORIZATION</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            font-size:12px;
            color:#555555;
            line-height:1.8;
        ">
            • Converts descriptions into numerical vectors<br>
            • Measures informative terms across products<br>
            • Reduces reliance on raw text<br>
            • Produces ML-compatible text features
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# MODEL FEATURES
# ============================================================

with text_col3:

    st.markdown(
        '<div class="feature-group-label">MODEL FEATURES</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            font-size:12px;
            color:#555555;
            line-height:1.8;
        ">
            • Text features combined with behavioral signals<br>
            • Evaluated with temporal and session features<br>
            • Adds product-level semantic context<br>
            • Supports downstream model experimentation
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# KEY TAKEAWAY
# ============================================================

st.markdown(
    """
    <div class="target-box" style="margin-top:22px;">

        <div class="target-name">
            💡 Key Takeaway
        </div>

        <div class="target-description" style="
            font-size:12px;
            line-height:1.8;
        ">
            • Raw Product ID and Category ID identify products but contain limited semantic information.<br>
            • LLM-generated descriptions convert structured metadata into meaningful product context.<br>
            • TF-IDF transforms this context into numerical features that can be evaluated alongside behavioral and session signals.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SPACE BETWEEN SECTIONS
# ============================================================

st.markdown(
    '<div class="section-spacer"></div>',
    unsafe_allow_html=True
)
