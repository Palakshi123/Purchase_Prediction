# ============================================================
# IMPORTS
# ============================================================

import streamlit as st
import pandas as pd
from pathlib import Path


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="E-Commerce Purchase Prediction",
    page_icon="🛒",
    layout="wide"
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"


# ============================================================
# GLOBAL STYLE
# ============================================================

st.markdown("""
<style>

/* ----------------------------------------------------------
   PAGE
---------------------------------------------------------- */

.block-container {
    padding-top: 1.8rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}


/* ----------------------------------------------------------
   GLOBAL TYPOGRAPHY
---------------------------------------------------------- */

html, body, [class*="css"] {
    font-family: "Source Sans Pro", sans-serif;
}

p, li {
    font-size: 14px !important;
    line-height: 1.65 !important;
}


/* ----------------------------------------------------------
   MAIN DASHBOARD HEADER
---------------------------------------------------------- */

.dashboard-title {
    font-size: 30px;
    font-weight: 700;
    color: #1F1F1F;
    line-height: 1.2;
}

.dashboard-subtitle {
    font-size: 15px;
    color: #666666;
    margin-top: 5px;
}

.dashboard-description {
    font-size: 14px;
    color: #777777;
    margin-top: 10px;
}

.dashboard-accent {
    width: 65px;
    height: 4px;
    background: #E72F3D;
    border-radius: 5px;
    margin-top: 12px;
}


/* ----------------------------------------------------------
   SECTION TYPOGRAPHY
---------------------------------------------------------- */

.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #E72F3D;
    margin-top: 26px;
    margin-bottom: 2px;
    line-height: 1.3;
}

.section-subtitle {
    font-size: 14px;
    color: #777777;
    line-height: 1.6;
    margin-bottom: 18px;
}

.subsection-title {
    font-size: 16px;
    font-weight: 700;
    color: #E72F3D;
    margin-top: 16px;
    margin-bottom: 8px;
}


/* ----------------------------------------------------------
   KPI CARDS
---------------------------------------------------------- */

.metric-card {
    text-align: center;
    padding: 8px 3px;
    min-height: 65px;
}

.metric-icon {
    font-size: 14px;
}

.metric-value {
    font-size: 17px;
    font-weight: 700;
    color: #E72F3D;
    margin-left: 4px;
}

.metric-label {
    font-size: 12px;
    color: #777777;
    margin-top: 5px;
}


/* ----------------------------------------------------------
   FEATURE PILLS
---------------------------------------------------------- */

.feature-pill {
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    color: #E72F3D;
    background: rgba(231,47,61,0.07);
    border-radius: 15px;
    padding: 4px 9px;
    margin-bottom: 8px;
}


/* ----------------------------------------------------------
   STREAMLIT COMPONENT CONSISTENCY
---------------------------------------------------------- */

/* selectbox label */
div[data-testid="stSelectbox"] label p {
    font-size: 14px !important;
    font-weight: 600 !important;
}

/* selectbox value */
div[data-baseweb="select"] {
    font-size: 14px !important;
}

/* dataframe */
div[data-testid="stDataFrame"] {
    font-size: 13px !important;
}

/* bordered containers */
div[data-testid="stVerticalBlockBorderWrapper"] p {
    font-size: 14px !important;
}

/* alerts */
div[data-testid="stAlert"] p {
    font-size: 14px !important;
    line-height: 1.6 !important;
}


/* ----------------------------------------------------------
   SPACING
---------------------------------------------------------- */

.section-space {
    height: 24px;
}

.small-space {
    height: 10px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# REUSABLE COMPONENTS
# ============================================================

def section_title(title, subtitle):
    st.markdown(
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="section-subtitle">{subtitle}</div>',
        unsafe_allow_html=True
    )


def subsection(title):
    st.markdown(
        f'<div class="subsection-title">{title}</div>',
        unsafe_allow_html=True
    )


def pill(text):
    st.markdown(
        f'<span class="feature-pill">{text}</span>',
        unsafe_allow_html=True
    )


def space():
    st.markdown(
        '<div class="section-space"></div>',
        unsafe_allow_html=True
    )


def metric_cards(cards):
    cols = st.columns(len(cards))

    for col, (icon, value, label) in zip(cols, cards):
        with col:
            st.markdown(
                f'<div class="metric-card">'
                f'<span class="metric-icon">{icon}</span>'
                f'<span class="metric-value">{value}</span>'
                f'<div class="metric-label">{label}</div>'
                f'</div>',
                unsafe_allow_html=True
            )


# ============================================================
# HEADER
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

section_title(
    "Dataset Information",
    "One month of e-commerce behavioral data capturing View, Cart, and Purchase interactions."
)


metric_cards([
    ("📊", "42.45M", "Total Records"),
    ("👥", "3.02M", "Unique Customers"),
    ("🛒", "9.24M", "Unique Sessions"),
    ("📦", "166,794", "Unique Products"),
    ("🏷️", "3,444", "Unique Brands"),
    ("🗂️", "126", "Unique Categories")
])


metric_cards([
    ("🔢", "9", "Initial Features"),
    ("📅", "1 Month", "Dataset Period"),
    ("🧭", "4", "Category Levels"),
    ("👆", "3", "Event Types · View · Cart · Purchase")
])


space()


# ============================================================
# DATA QUALITY
# ============================================================

section_title(
    "Missing Value & Duplicate Records Analysis",
    "Assessment of missing values, recoverable product metadata, and duplicate records."
)


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


left, right = st.columns(2, gap="large")


with left:

    subsection("Missing Value Analysis")

    st.dataframe(
        missing_table,
        use_container_width=True,
        hide_index=True
    )

    subsection("Brand Metadata Recovery")

    st.dataframe(
        brand_recovery_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        "**Recovery Strategy:** Missing brand values were recovered where "
        "a reliable brand mapping existed for the same Product ID, restoring "
        "**172,423 records (2.82%)**."
    )


with right:

    subsection("Duplicate Record Analysis")

    st.dataframe(
        duplicate_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        "**Duplicate Treatment:** 30,220 exact duplicate interaction "
        "records (**0.07%**) were removed before downstream analysis."
    )

    subsection("Missing Value Treatment")

    st.dataframe(
        treatment_table,
        use_container_width=True,
        hide_index=True
    )


space()


# ============================================================
# FEATURE ENGINEERING
# ============================================================

section_title(
    "Feature Engineering",
    "Created behavioral, temporal, session, and purchase-intent signals from raw customer interactions."
)


metric_cards([
    ("🧩", "24", "Predictor Features"),
    ("🕒", "4", "Temporal Features"),
    ("👆", "7", "Behavioral Features"),
    ("⚡", "9", "Session Features"),
    ("🎯", "4", "Purchase Intent Features")
])


left, right = st.columns(2, gap="large")


# ============================================================
# TEMPORAL + BEHAVIORAL
# ============================================================

with left:

    subsection("🕒 Temporal Features")
    pill("4 retained features")

    temporal_features = pd.DataFrame({
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
        temporal_features,
        use_container_width=True,
        hide_index=True
    )


    subsection("👆 Behavioral Features")
    pill("7 retained features")

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
# SESSION + PURCHASE INTENT
# ============================================================

with right:

    subsection("⚡ Session & Intensity Features")
    pill("9 retained features")

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


    subsection("🎯 Purchase Intent Features")
    pill("4 retained features")

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


st.info(
    """
**🎯 Target Variable — `purchase_later`**

Binary target indicating whether a purchase occurs later within the same
user session. Customer behavior observed up to the current interaction is
used to predict future purchase intent.
"""
)


space()


# ============================================================
# EXPLORATORY DATA ANALYSIS
# ============================================================

section_title(
    "Exploratory Data Analysis",
    "Explore customer behavior, purchase patterns, session activity, and temporal trends."
)


eda_visualizations = {
    "Event Distribution": "event_distribution.png",
    "Purchase vs No-Purchase Sessions": "purchase_sessions.png",
    "Repeat Customer Conversion": "repeat_conversion.png",
    "Customer Activity by Day of Week": "day_of_week.png",
    "Weekend vs Weekday Behavior": "weekend_weekday.png",
    "Price by Event Type": "price_event_type.png",
    "Session Behavior": "session_behavior.png",
    "Events Before Purchase": "events_before_purchase.png",
    "Time to First Purchase": "time_first_purchase.png"
}


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


selected_visualization = st.selectbox(
    "Select an analysis",
    list(eda_visualizations.keys())
)


image_path = IMAGE_DIR / eda_visualizations[selected_visualization]


if image_path.exists():

    left, center, right = st.columns([1, 2, 1])

    with center:

        subsection(selected_visualization)

        st.image(
            str(image_path),
            width=500
        )

else:

    st.warning(
        f"Visualization not found: {image_path.name}"
    )


subsection("💡 Business Insight")

st.info(
    business_insights[selected_visualization]
)


space()


# ============================================================
# TEXT ENRICHMENT
# ============================================================

section_title(
    "Text Enrichment & LLM Integration",
    "Generating semantic product descriptions from structured metadata to introduce richer product context into the modeling pipeline."
)


# ============================================================
# WHY TEXT ENRICHMENT
# ============================================================

subsection("Why Text Enrichment?")

st.markdown(
    """
- **product_id** and **category_id** are high-cardinality identifiers with limited semantic meaning.
- **category_code** provides category context, while **brand** identifies the manufacturer, but neither fully describes the product.
- Product descriptions combine available metadata into a richer **semantic representation** of each product.
- Generated descriptions can then be converted into numerical features for downstream machine-learning experiments.
"""
)


# ============================================================
# PIPELINE
# ============================================================

subsection("Text Enrichment Pipeline")

pipeline_image = IMAGE_DIR / "text_enrichment_pipeline.png"


if pipeline_image.exists():

    left, center, right = st.columns([1, 2.5, 1])

    with center:

        st.image(
            str(pipeline_image),
            width=600
        )

else:

    st.warning(
        f"Pipeline image not found: {pipeline_image.name}"
    )


# ============================================================
# LLM SELECTION
# ============================================================

subsection("LLM Selection Strategy")

local_col, cloud_col, openai_col = st.columns(
    3,
    gap="large"
)


with local_col:

    pill("LOCAL SMALL LLM")

    st.markdown(
        """
- No API cost
- Full local control
- Limited by device RAM / compute
- Slower generation at scale
- Smaller models may reduce output quality
"""
    )


with cloud_col:

    pill("LARGE CLOUD LLM")

    st.markdown(
        """
- Strong generation quality
- Advanced reasoning capability
- Higher API / token cost
- More capability than required
- Lower cost-efficiency at scale
"""
    )


with openai_col:

    pill("✓ SELECTED — OPENAI API")

    st.markdown(
        """
- Lightweight model
- Cost-efficient inference
- Sufficient generation quality
- No local compute dependency
- Easy batch automation and scaling
"""
    )


# ============================================================
# MODEL DECISION
# ============================================================

st.success(
    """
**✓ Model Selection Decision**

A lightweight OpenAI API model was selected because product-description
generation requires reliable text generation rather than complex reasoning,
providing a practical balance of **cost, quality, speed, and scalability**.
"""
)


# ============================================================
# EXAMPLE ENRICHMENT
# ============================================================

subsection("Example Enrichment")


with st.container(border=True):

    metadata_col, description_col = st.columns(
        2,
        gap="large"
    )


    with metadata_col:

        pill("STRUCTURED PRODUCT METADATA")

        st.markdown(
            """
**Product ID:** 1004856  
**Category:** electronics.smartphone  
**Brand:** Samsung
"""
        )


    with description_col:

        pill("LLM-GENERATED DESCRIPTION")

        st.markdown(
            """
Samsung smartphone in the consumer electronics category,
designed for mobile communication and everyday digital use.
"""
        )


# ============================================================
# TEXT → MODEL
# ============================================================

subsection("From Text to Model Features")

description_col, tfidf_col, model_col = st.columns(
    3,
    gap="large"
)


with description_col:

    pill("01 · DESCRIPTION")

    st.markdown(
        """
- Semantic product representation
- Human-readable product context
- Combines multiple metadata fields
"""
    )


with tfidf_col:

    pill("02 · TF-IDF")

    st.markdown(
        """
- Converts text into numerical vectors
- Captures informative product terms
- Produces ML-compatible features
"""
    )


with model_col:

    pill("03 · MODEL INPUT")

    st.markdown(
        """
- Combined with behavioral features
- Combined with session features
- Evaluated during model experimentation
"""
    )


# ============================================================
# KEY TAKEAWAY
# ============================================================

st.info(
    """
**💡 Key Takeaway**

LLM enrichment transforms high-cardinality product identifiers into semantic
product representations, while TF-IDF converts this context into numerical
features that can be evaluated alongside behavioral and session signals.
"""
)


space()
