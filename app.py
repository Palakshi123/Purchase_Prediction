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

/* PAGE */

.block-container {
    padding-top: 1.6rem;
    padding-bottom: 3rem;
    padding-left: 3rem;
    padding-right: 3rem;
    max-width: 100%;
}


/* GLOBAL TYPOGRAPHY */

html, body, [class*="css"] {
    font-family: "Source Sans Pro", sans-serif;
}

p, li {
    font-size: 13px !important;
    line-height: 1.55 !important;
}


/* DASHBOARD HEADER */

.dashboard-title {
    font-size: 26px;
    font-weight: 700;
    color: #1F1F1F;
    line-height: 1.2;
    margin: 0;
}

.dashboard-subtitle {
    font-size: 14px;
    font-weight: 500;
    color: #555555;
    margin-top: 4px;
}

.dashboard-description {
    font-size: 13px;
    color: #777777;
    margin-top: 7px;
}

.dashboard-accent {
    width: 65px;
    height: 4px;
    background-color: #E72F3D;
    border-radius: 5px;
    margin-top: 10px;
    margin-bottom: 5px;
}


/* SECTION TITLES */

.section-title {
    font-size: 20px;
    font-weight: 700;
    color: #E72F3D;
    line-height: 1.25;
    margin-top: 26px;
    margin-bottom: 3px;
}

.section-subtitle {
    font-size: 12.5px;
    color: #777777;
    line-height: 1.5;
    margin-top: 0;
    margin-bottom: 16px;
}


/* SUBSECTION TITLES */

.subsection-title {
    font-size: 15px;
    font-weight: 700;
    color: #E72F3D;
    line-height: 1.3;
    margin-top: 16px;
    margin-bottom: 8px;
}


/* CONTENT HEADINGS */

.content-heading {
    font-size: 14px;
    font-weight: 700;
    color: #333333;
    margin-top: 5px;
    margin-bottom: 6px;
}


/* KPI CARDS */

.metric-card {
    text-align: center;
    padding: 6px 3px;
    min-height: 58px;
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
    font-size: 11px;
    color: #777777;
    margin-top: 3px;
}


/* FEATURE PILLS */

.feature-pill {
    display: inline-block;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.2px;
    color: #E72F3D;
    background-color: rgba(231, 47, 61, 0.07);
    border-radius: 14px;
    padding: 4px 9px;
    margin-bottom: 7px;
}


/* DATAFRAMES */

div[data-testid="stDataFrame"] {
    font-size: 12px !important;
}


/* SELECTBOX */

div[data-testid="stSelectbox"] label p {
    font-size: 13px !important;
    font-weight: 600 !important;
}

div[data-baseweb="select"] {
    font-size: 13px !important;
}


/* ALERTS */

div[data-testid="stAlert"] p,
div[data-testid="stAlert"] li {
    font-size: 13px !important;
    line-height: 1.5 !important;
}


/* BORDERED CONTAINERS */

div[data-testid="stVerticalBlockBorderWrapper"] p {
    font-size: 13px !important;
    line-height: 1.5 !important;
}


/* SPACING */

.section-space {
    height: 22px;
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
# DASHBOARD HEADER
# ============================================================

st.markdown(
    '<div class="dashboard-title">🛒 E-Commerce Purchase Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Customer Behavior Analytics & Machine Learning Dashboard'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-accent"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-description">'
    'Predicting purchase intent from customer browsing, cart, product, '
    'and session behavior.'
    '</div>',
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
    "Generating predictive behavioral signals and transforming categorical features into model-ready representations."
)


# ============================================================
# 01 — FEATURE GENERATION
# ============================================================

subsection("01 · Feature Generation")

st.markdown(
    """
    Behavioral, temporal, session, and purchase-intent features were created
    using customer activity observed up to the current interaction.
    """
)

metric_cards([
    ("🧩", "24", "Generated Features"),
    ("🕒", "4", "Temporal"),
    ("👆", "7", "Behavioral"),
    ("⚡", "9", "Session"),
    ("🎯", "4", "Purchase Intent")
])


# ============================================================
# 02 — FEATURE ENCODING
# ============================================================

space()

subsection("02 · Feature Encoding — Linear Model")

st.markdown(
    """
    Categorical features were encoded based on cardinality to create
    efficient numerical inputs for the linear model.
    """
)

encoding_col1, encoding_col2 = st.columns(
    2,
    gap="large"
)


with encoding_col1:

    pill("FREQUENCY ENCODING")

    st.markdown(
        '<div class="content-heading">brand · 2,618 categories</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
- High-cardinality categorical feature
- Avoids creating thousands of sparse columns
- Represents brand prevalence with one numerical feature
"""
    )


with encoding_col2:

    pill("ONE-HOT ENCODING")

    st.markdown(
        '<div class="content-heading">Lower-Cardinality Features</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
- `event_type` — **3**
- `day_of_week` — **6**
- `category_level_1` — **14**
- `category_level_2` — **57**
- `category_level_3` — **82**
- `category_level_4` — **2**
- `previous_event` — **3**
"""
    )

    st.markdown(
        """
        One-hot encoding creates independent binary indicators without
        imposing an artificial ordinal relationship.
        """
    )


# ============================================================
# TARGET VARIABLE
# ============================================================

st.info(
    """
**🎯 Target Variable — `purchase_later`**

Binary target indicating whether a purchase occurs later within the same
user session. Customer behavior observed up to the current interaction
is used to predict future purchase intent.
"""
)

space()


# ============================================================
# EXPLORATORY DATA ANALYSIS
# ============================================================

section_title(
    "Univariate/Bivariate/Multivariate Data Visualization",
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
# TEXT ENRICHMENT & LLM INTEGRATION
# ============================================================

section_title(
    "Product Description Generation — Text Generation + Enrichment",
    "Generating semantic product descriptions from structured metadata to introduce richer product context into the modeling pipeline."
)


# ============================================================
# WHY TEXT ENRICHMENT
# ============================================================

subsection("Why Product Description Generation using LLM API?")

st.markdown(
    """
- **Product ID** and **Category ID** are internal identifiers and could not be reliably matched with external product databases.
- **Open-source datasets** provided similar metadata such as ID, category, and brand but lacked product-level descriptions.
- Therefore, an **LLM API** was used to generate standardized product descriptions from the available metadata.
"""
)


# ============================================================
# TEXT ENRICHMENT PIPELINE
# ============================================================

subsection("Text Enrichment Pipeline")

pipeline_image = IMAGE_DIR / "text_enrichment_pipeline.png"

if pipeline_image.exists():

    left, center, right = st.columns(
        [0.5, 3, 0.5]
    )

    with center:

        st.image(
            str(pipeline_image),
            width=900
        )

else:

    st.warning(
        f"Pipeline image not found: {pipeline_image.name}"
    )


# ============================================================
# LLM SELECTION STRATEGY
# ============================================================

subsection("LLM API Selection Strategy")

local_col, cloud_col, openai_col = st.columns(
    3,
    gap="large"
)


with local_col:

    pill("LOCAL SMALL LLM")

    st.markdown(
        """
- No API cost
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
- Higher API / token cost
- More capability than required
"""
    )


with openai_col:

    pill("OPENAI API")

    st.markdown(
        """
- Lightweight model
- Cost-efficient inference
- Sufficient generation quality
- No local compute dependency
- Fast text generation
"""
    )


st.success(
    """
**✓ Model Selection Decision**

An OpenAI API model was selected because it provided a practical balance
of **cost, quality, speed, and scalability**.
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

space()


# ============================================================
# PREDICTIVE MODELING
# ============================================================

section_title(
    "Machine Learning Modeling",
    "Robust machine learning models to predict purchase intent while preventing data leakage and ensuring reliable evaluation on unseen customer sessions"
)


# ============================================================
# TRAIN / VALIDATION / TEST SPLIT
# ============================================================

subsection("Train / Validation / Test Split")

st.markdown(
    """
    Data was split **chronologically at the user-session level** using each
    session's start time, ensuring that an entire session belongs to only
    one dataset.
    """
)

st.markdown(
    '<div class="small-space"></div>',
    unsafe_allow_html=True
)


# ============================================================
# SPLIT KPI
# ============================================================

metric_cards([
    ("🧠", "70%", "Training Sessions"),
    ("⚙️", "15%", "Validation Sessions"),
    ("🧪", "15%", "Test Sessions")
])


# ============================================================
# SPLIT SUMMARY
# ============================================================

subsection("Split Summary")

split_summary = pd.DataFrame({
    "Dataset": [
        "Training",
        "Validation",
        "Test"
    ],
    "Sessions": [
        "958,551",
        "205,405",
        "205,404"
    ],
    "Rows": [
        "4,412,736",
        "1,017,454",
        "999,551"
    ],
    "Purchase Rate": [
        "7.73%",
        "8.49%",
        "7.71%"
    ],
    "Purpose": [
        "Model training",
        "Model tuning & selection",
        "Final unseen evaluation"
    ]
})

st.dataframe(
    split_summary,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# WHY THIS SPLIT
# ============================================================

subsection("Why This Split?")

st.markdown(
    """
- **No session overlap** — all events from the same user session remain in one split.
- **Prevents data leakage** — session information cannot appear across training and evaluation sets.
- **Preserves chronology** — models train on earlier sessions and are evaluated on later sessions.
- **Production-like evaluation** — reflects predicting purchase intent for future customer sessions.
- **Consistent evaluation** — all models use the same leakage-free validation and test sets.
"""
)

# ============================================================
# LOGISTIC REGRESSION — BASELINE
# ============================================================

space()

subsection("Logistic Regression — Baseline Model")

st.markdown(
    """
    Logistic Regression was implemented as the baseline linear classifier
    using mini-batch training and class-balanced learning.
    """
)


# ============================================================
# MODEL CONFIGURATION
# ============================================================

config_col1, config_col2, config_col3, config_col4 = st.columns(
    4,
    gap="large"
)

with config_col1:
    pill("MODEL")
    st.markdown(
        '<div class="content-heading">SGD Logistic Regression</div>',
        unsafe_allow_html=True
    )

with config_col2:
    pill("REGULARIZATION")
    st.markdown(
        '<div class="content-heading">L2</div>',
        unsafe_allow_html=True
    )

with config_col3:
    pill("CLASS BALANCE")
    st.markdown(
        '<div class="content-heading">Balanced Weights</div>',
        unsafe_allow_html=True
    )

with config_col4:
    pill("TRAINING")
    st.markdown(
        '<div class="content-heading">100K Mini-Batches</div>',
        unsafe_allow_html=True
    )


# ============================================================
# MODEL DETAILS
# ============================================================

st.markdown(
    '<div class="small-space"></div>',
    unsafe_allow_html=True
)

model_details = pd.DataFrame({
    "Parameter": [
        "Loss",
        "Penalty",
        "Alpha",
        "Class Weight — No Purchase",
        "Class Weight — Purchase",
        "Batch Size"
    ],
    "Value": [
        "Log Loss",
        "L2",
        "0.0001",
        "0.5411",
        "6.5884",
        "100,000"
    ]
})

st.dataframe(
    model_details,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# TEST PERFORMANCE
# ============================================================

subsection("Test Performance")

metric_cards([
    ("📊", "46.82%", "Accuracy"),
    ("🎯", "10.12%", "Precision"),
    ("🔎", "76.31%", "Recall"),
    ("⚖️", "17.87%", "F1 Score"),
    ("📈", "0.6874", "ROC-AUC"),
    ("📉", "0.2232", "PR-AUC")
])


# ============================================================
# BASELINE RESULT
# ============================================================

st.info(
    """
**Baseline Result:** The model captured **76.31% of future purchases**, but
with **10.12% precision**, establishing the initial precision–recall benchmark
for comparison with nonlinear models.
"""
)
