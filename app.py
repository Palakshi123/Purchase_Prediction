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
# GLOBAL CSS
# ============================================================

st.markdown("""
<style>

.block-container {
    padding-top: 1.8rem;
    padding-bottom: 2rem;
    max-width: 1450px;
}

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

.dataset-heading {
    font-size: 22px;
    font-weight: 700;
    color: #E72F3D;
    margin-top: 18px;
    margin-bottom: 0;
}

.subsection-heading {
    font-size: 15px;
    font-weight: 700;
    color: #E72F3D;
    margin-top: 8px;
    margin-bottom: 7px;
}

.metric-card {
    padding: 5px 3px;
    min-height: 52px;
    text-align: center;
}

.metric-icon {
    font-size: 13px;
}

.metric-value {
    font-size: 15px;
    font-weight: 700;
    color: #E72F3D;
    margin-left: 3px;
}

.metric-label {
    font-size: 10px;
    color: #777777;
    margin-top: 3px;
}

.feature-group-label {
    display: inline-block;
    font-size: 10px;
    font-weight: 700;
    color: #E72F3D;
    background-color: rgba(231,47,61,0.07);
    border-radius: 12px;
    padding: 3px 8px;
    margin-bottom: 8px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# REUSABLE UI FUNCTIONS
# ============================================================

def section_title(title, subtitle):

    st.markdown(
        f'<div class="dataset-heading">{title}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<p style="font-size:14px; color:#777777; margin:3px 0 14px 0;">{subtitle}</p>',
        unsafe_allow_html=True
    )


def subsection(title):

    st.markdown(
        f'<div class="subsection-heading">{title}</div>',
        unsafe_allow_html=True
    )


def section_space():

    st.write("")
    st.write("")


def metric_cards(cards, columns):

    cols = st.columns(columns)

    for col, (icon, value, label) in zip(cols, cards):

        with col:

            st.markdown(
                f"""
<div class="metric-card">
<span class="metric-icon">{icon}</span>
<span class="metric-value">{value}</span>
<div class="metric-label">{label}</div>
</div>
""",
                unsafe_allow_html=True
            )


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

section_title(
    "Dataset Information",
    "One month of e-commerce behavioral data capturing View, Cart, and Purchase interactions."
)


cards_row1 = [
    ("📊", "42.45M", "Total Records"),
    ("👥", "3.02M", "Unique Customers"),
    ("🛒", "9.24M", "Unique Sessions"),
    ("📦", "166,794", "Unique Products"),
    ("🏷️", "3,444", "Unique Brands"),
    ("🗂️", "126", "Unique Categories")
]

metric_cards(cards_row1, 6)


cards_row2 = [
    ("🔢", "9", "Initial Features"),
    ("📅", "1 Month", "Dataset Period"),
    ("🧭", "4", "Category Levels"),
    ("👆", "3", "Event Types · View · Cart · Purchase")
]

metric_cards(cards_row2, 4)

section_space()


# ============================================================
# MISSING VALUE & DUPLICATE RECORD ANALYSIS
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

    st.caption(
        "Recovery Strategy: Missing brand values were recovered where a "
        "reliable brand mapping existed for the same Product ID, restoring "
        "172,423 records (2.82%)."
    )


with right:

    subsection("Duplicate Record Analysis")

    st.dataframe(
        duplicate_table,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "Duplicate Treatment: 30,220 exact duplicate interaction records "
        "(0.07%) were removed before downstream analysis."
    )

    subsection("Missing Value Treatment")

    st.dataframe(
        treatment_table,
        use_container_width=True,
        hide_index=True
    )


section_space()


# ============================================================
# FEATURE ENGINEERING
# ============================================================

section_title(
    "Feature Engineering",
    "Created behavioral, temporal, session, and purchase-intent signals from raw customer interactions."
)


feature_summary = [
    ("🧩", "24", "Predictor Features"),
    ("🕒", "4", "Temporal Features"),
    ("👆", "7", "Behavioral Features"),
    ("⚡", "9", "Session Features"),
    ("🎯", "4", "Purchase Intent Features")
]

metric_cards(feature_summary, 5)

st.write("")


# ============================================================
# FEATURE TABLES
# ============================================================

feature_col1, feature_col2 = st.columns(
    2,
    gap="large"
)


with feature_col1:

    subsection("🕒 Temporal Features")

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


    subsection("👆 Behavioral Features")

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


with feature_col2:

    subsection("⚡ Session & Intensity Features")

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


    subsection("🎯 Purchase Intent Features")

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

st.info(
    """
**🎯 Target Variable — `purchase_later`**

Binary target indicating whether a purchase occurs later within the same
user session. The model uses customer behavior observed up to the current
interaction to predict future purchase intent.
"""
)


section_space()


# ============================================================
# EXPLORATORY DATA ANALYSIS
# ============================================================

section_title(
    "Exploratory Data Analysis",
    "Explore customer behavior, purchase patterns, session activity, and temporal trends."
)


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


image_path = (
    IMAGE_DIR /
    eda_visualizations[selected_visualization]
)


if image_path.exists():

    left, center, right = st.columns(
        [1.5, 2, 1.5]
    )

    with center:

        st.markdown(
            f"#### {selected_visualization}"
        )

        st.image(
            str(image_path),
            width=450
        )

else:

    st.warning(
        f"Visualization not found: {image_path.name}"
    )


# ============================================================
# BUSINESS INSIGHT
# ============================================================

st.markdown("#### 💡 Business Insight")

st.info(
    business_insights[selected_visualization]
)


section_space()


# ============================================================
# TEXT ENRICHMENT & LLM INTEGRATION
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
# TEXT ENRICHMENT PIPELINE
# ============================================================

st.write("")

subsection("Text Enrichment Pipeline")

pipeline_image = (
    IMAGE_DIR /
    "text_enrichment_pipeline.png"
)


if pipeline_image.exists():

    left, center, right = st.columns(
        [1, 3, 1]
    )

    with center:

        st.image(
            str(pipeline_image),
            width=650
        )

else:

    st.warning(
        f"Pipeline image not found: {pipeline_image}"
    )


# ============================================================
# LLM SELECTION STRATEGY
# ============================================================

st.write("")

subsection("LLM Selection Strategy")

local_col, cloud_col, selected_col = st.columns(
    3,
    gap="large"
)


# ------------------------------------------------------------
# LOCAL SMALL LLM
# ------------------------------------------------------------

with local_col:

    st.markdown("##### Local Small LLM")

    st.markdown(
        """
- No API cost
- Full local control
- Limited by device RAM / compute
- Slower generation at scale
- Smaller models may reduce output quality
"""
    )


# ------------------------------------------------------------
# LARGE CLOUD LLM
# ------------------------------------------------------------

with cloud_col:

    st.markdown("##### Large Cloud LLM")

    st.markdown(
        """
- Strong generation quality
- Advanced reasoning capability
- Higher API / token cost
- More capability than required
- Lower cost-efficiency at scale
"""
    )


# ------------------------------------------------------------
# SELECTED OPENAI APPROACH
# ------------------------------------------------------------

with selected_col:

    st.markdown("##### ✓ Selected — OpenAI API")

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
# MODEL SELECTION DECISION
# ============================================================

st.success(
    """
**✓ Model Selection Decision**

A lightweight OpenAI API model was selected because product-description
generation requires reliable text generation rather than complex reasoning.

**Best trade-off:** Cost · Quality · Speed · Scalability
"""
)


# ============================================================
# EXAMPLE ENRICHMENT
# ============================================================

st.write("")

subsection("Example Enrichment")


with st.container(border=True):

    metadata_col, description_col = st.columns(
        2,
        gap="large"
    )


    with metadata_col:

        st.markdown("##### Structured Product Metadata")

        st.markdown(
            """
**Product ID:** 1004856  
**Category:** electronics.smartphone  
**Brand:** Samsung
"""
        )


    with description_col:

        st.markdown("##### LLM-Generated Description")

        st.write(
            "Samsung smartphone in the consumer electronics category, "
            "designed for mobile communication and everyday digital use."
        )


# ============================================================
# FROM TEXT TO MODEL FEATURES
# ============================================================

st.write("")

subsection("From Text to Model Features")

description_col, tfidf_col, model_col = st.columns(
    3,
    gap="large"
)


# ------------------------------------------------------------
# DESCRIPTION
# ------------------------------------------------------------

with description_col:

    st.markdown("##### 01 · Description")

    st.markdown(
        """
- Semantic product representation
- Human-readable product context
- Combines multiple metadata fields
"""
    )


# ------------------------------------------------------------
# TF-IDF
# ------------------------------------------------------------

with tfidf_col:

    st.markdown("##### 02 · TF-IDF")

    st.markdown(
        """
- Converts text into numerical vectors
- Captures informative product terms
- Produces ML-compatible features
"""
    )


# ------------------------------------------------------------
# MODEL INPUT
# ------------------------------------------------------------

with model_col:

    st.markdown("##### 03 · Model Input")

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


section_space()
