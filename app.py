# ============================================================
# IMPORTS
# ============================================================

import streamlit as st
import pandas as pd
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
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
# GLOBAL STYLING
# ============================================================

st.markdown("""
<style>

/* MAIN PAGE */

.block-container {
    padding-top: 1.8rem;
    padding-bottom: 2rem;
    max-width: 1450px;
}


/* DASHBOARD HEADER */

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


/* MAJOR SECTION */

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
    line-height: 1.6;
}


/* SPACING */

.section-spacer {
    height: 26px;
}

.kpi-table-spacer {
    height: 35px;
}


/* KPI INFORMATION */

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


/* SUBSECTION HEADINGS */

.subsection-heading {
    font-size: 15px;
    font-weight: 700;
    color: #E72F3D;
    margin-bottom: 7px;
}


/* BODY TEXT */

.cleaning-note {
    font-size: 12px;
    color: #666666;
    margin-top: 8px;
    line-height: 1.6;
}

.large-body-text {
    font-size: 14px;
    color: #555555;
    line-height: 1.8;
    margin-top: 6px;
}


/* FEATURE LABEL */

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


/* TARGET / INSIGHT BOX */

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
    font-size: 12px;
    margin-top: 3px;
    line-height: 1.6;
}


/* EXAMPLE BOX */

.example-box {
    border: 1px solid rgba(231, 47, 61, 0.30);
    border-left: 4px solid #E72F3D;
    border-radius: 8px;
    padding: 18px 22px;
    margin-top: 7px;
    background-color: rgba(231, 47, 61, 0.025);
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
        <div class="dataset-heading">
            Dataset Information
        </div>

        <div class="section-caption">
            One month of e-commerce behavioral data capturing
            View, Cart, and Purchase interactions.
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
            f"""
            <div class="metric-card">
                <span class="metric-icon">{icon}</span>
                <span class="metric-value">{value}</span>
                <div class="metric-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


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
            Assessment of missing values, recoverable product metadata,
            and duplicate records.
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
# DATA QUALITY — TWO COLUMNS
# ============================================================

left, right = st.columns(2, gap="large")


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
        """
        <div class="cleaning-note">
            <b>Recovery Strategy:</b>
            Missing brand values were recovered where a reliable brand
            mapping existed for the same Product ID. This restored
            <b>172,423 records (2.82%)</b> without introducing synthetic
            brand information.
        </div>
        """,
        unsafe_allow_html=True
    )


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
        """
        <div class="cleaning-note">
            <b>Duplicate Treatment:</b>
            30,220 exact duplicate interaction records were identified,
            representing <b>0.07%</b> of the dataset, and removed before
            downstream analysis.
        </div>
        """,
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
            Created behavioral, temporal, session, and purchase-intent
            signals from raw customer interactions.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FEATURE KPI SUMMARY
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
            f"""
            <div class="metric-card">
                <span class="metric-icon">{icon}</span>
                <span class="metric-value">{value}</span>
                <div class="metric-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


st.markdown(
    '<div class="kpi-table-spacer"></div>',
    unsafe_allow_html=True
)


# ============================================================
# FEATURE TABLES
# ============================================================

feature_col1, feature_col2 = st.columns(
    2,
    gap="large"
)


# ============================================================
# LEFT — TEMPORAL & BEHAVIORAL
# ============================================================

with feature_col1:

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
    """
    <div class="target-box">

        <div class="target-name">
            🎯 Target Variable — purchase_later
        </div>

        <div class="target-description">
            Binary target indicating whether a purchase occurs later within
            the same user session. The model uses customer behavior observed
            up to the current interaction to predict future purchase intent.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


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
            Explore customer behavior, purchase patterns, session activity,
            and temporal trends by selecting a visualization below.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# EDA VISUALIZATIONS
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
# EDA DROPDOWN
# ============================================================

selected_visualization = st.selectbox(
    "Select an analysis",
    options=list(eda_visualizations.keys())
)

selected_file = eda_visualizations[
    selected_visualization
]

image_path = IMAGE_DIR / selected_file


# ============================================================
# DISPLAY VISUALIZATION
# ============================================================

if image_path.exists():

    left, center, right = st.columns(
        [1.5, 2, 1.5]
    )

    with center:

        st.markdown(
            f"""
            <div class="subsection-heading"
                 style="text-align:center;">
                {selected_visualization}
            </div>
            """,
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
    <div class="target-box"
         style="margin-top:8px;">

        <div class="target-name">
            💡 Business Insight
        </div>

        <div class="target-description"
             style="font-size:13px;">
            {business_insights[selected_visualization]}
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="section-spacer"></div>',
    unsafe_allow_html=True
)


# ============================================================
# TEXT ENRICHMENT & LLM INTEGRATION
# ============================================================

pipeline_image = (
    IMAGE_DIR /
    "text_enrichment_pipeline.png"
)


# ============================================================
# SECTION HEADER
# ============================================================

st.markdown(
    """
    <div class="section-container">

        <div class="dataset-heading">
            Text Enrichment & LLM Integration
        </div>

        <div class="section-caption"
             style="
                font-size:15px;
                line-height:1.6;
                margin-top:5px;
             ">
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
    """
    <div class="subsection-heading"
         style="margin-top:20px;">
        Why Text Enrichment?
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="large-body-text"
         style="margin-bottom:22px;">

        • <b>product_id</b> and <b>category_id</b> are high-cardinality
        identifiers with limited semantic meaning.<br>

        • <b>category_code</b> provides category context, while
        <b>brand</b> identifies the manufacturer, but neither fully
        describes the product.<br>

        • Product descriptions combine available metadata into a richer
        <b>semantic representation</b> of each product.<br>

        • Generated text can then be transformed into numerical features
        for downstream machine-learning experiments.

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TEXT ENRICHMENT PIPELINE
# ============================================================

st.markdown(
    '<div class="subsection-heading">Text Enrichment Pipeline</div>',
    unsafe_allow_html=True
)

if pipeline_image.exists():

    pipe_left, pipe_center, pipe_right = st.columns(
        [1, 3, 1]
    )

    with pipe_center:

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

st.markdown(
    """
    <div class="subsection-heading"
         style="margin-top:22px;">
        LLM Selection Strategy
    </div>
    """,
    unsafe_allow_html=True
)

local_col, large_col, selected_col = st.columns(
    3,
    gap="large"
)


# ============================================================
# LOCAL SMALL LLM
# ============================================================

with local_col:

    st.markdown(
        '<div class="feature-group-label">LOCAL SMALL LLM</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="large-body-text">
            • No API cost<br>
            • Full local control<br>
            • Limited by device RAM / compute<br>
            • Slower generation at scale<br>
            • Smaller model may reduce output quality
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# LARGE CLOUD LLM
# ============================================================

with large_col:

    st.markdown(
        '<div class="feature-group-label">LARGE CLOUD LLM</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="large-body-text">
            • Strong generation quality<br>
            • Advanced reasoning capability<br>
            • Higher API / token cost<br>
            • More capability than required<br>
            • Lower cost-efficiency at scale
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SELECTED — OPENAI API
# ============================================================

with selected_col:

    st.markdown(
        '<div class="feature-group-label">✓ SELECTED — OPENAI API</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="large-body-text">
            • Lightweight model<br>
            • Cost-efficient inference<br>
            • Sufficient generation quality<br>
            • No local compute dependency<br>
            • Easy batch automation & scaling
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# MODEL SELECTION DECISION
# ============================================================

st.markdown(
    """
    <div class="target-box"
         style="margin-top:22px;">

        <div class="target-name">
            ✓ Model Selection Decision
        </div>

        <div class="target-description"
             style="
                font-size:14px;
                line-height:1.7;
             ">

            A lightweight <b>OpenAI API model</b> was selected because
            product-description generation requires reliable text generation
            rather than complex reasoning, providing the best balance of
            <b>cost, quality, speed, and scalability</b>.

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# EXAMPLE ENRICHMENT
# ============================================================

st.markdown(
    """
    <div class="subsection-heading"
         style="margin-top:25px;">
        Example Enrichment
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="example-box">

        <div style="
            display:grid;
            grid-template-columns:1fr 1fr;
            gap:55px;
        ">

            <div>

                <div class="feature-group-label">
                    STRUCTURED PRODUCT METADATA
                </div>

                <div class="large-body-text">
                    <b>Product ID:</b> 1004856<br>
                    <b>Category:</b> electronics.smartphone<br>
                    <b>Brand:</b> Samsung
                </div>

            </div>


            <div>

                <div class="feature-group-label">
                    LLM-GENERATED DESCRIPTION
                </div>

                <div class="large-body-text">
                    Samsung smartphone in the consumer electronics category,
                    designed for mobile communication and everyday digital use.
                </div>

            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FROM TEXT TO MODEL FEATURES
# ============================================================

st.markdown(
    """
    <div class="subsection-heading"
         style="margin-top:25px;">
        From Text to Model Features
    </div>
    """,
    unsafe_allow_html=True
)

description_col, tfidf_col, model_col = st.columns(
    3,
    gap="large"
)


# ============================================================
# STEP 1 — DESCRIPTION
# ============================================================

with description_col:

    st.markdown(
        '<div class="feature-group-label">01 · DESCRIPTION</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="large-body-text">
            • Semantic product representation<br>
            • Human-readable product context<br>
            • Combines multiple metadata fields
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# STEP 2 — TF-IDF
# ============================================================

with tfidf_col:

    st.markdown(
        '<div class="feature-group-label">02 · TF-IDF</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="large-body-text">
            • Converts text into numerical vectors<br>
            • Captures informative product terms<br>
            • Produces ML-compatible features
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# STEP 3 — MODEL INPUT
# ============================================================

with model_col:

    st.markdown(
        '<div class="feature-group-label">03 · MODEL INPUT</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="large-body-text">
            • Combined with behavioral features<br>
            • Combined with session features<br>
            • Evaluated during model experimentation
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# KEY TAKEAWAY
# ============================================================

st.markdown(
    """
    <div class="target-box"
         style="margin-top:24px;">

        <div class="target-name">
            💡 Key Takeaway
        </div>

        <div class="target-description"
             style="
                font-size:14px;
                line-height:1.7;
             ">

            LLM enrichment transforms high-cardinality product identifiers
            into <b>semantic product representations</b>, while TF-IDF converts
            this context into numerical features that can be evaluated alongside
            behavioral and session signals.

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SECTION SPACING
# ============================================================

st.markdown(
    '<div class="section-spacer"></div>',
    unsafe_allow_html=True
)
