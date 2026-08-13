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
# LOGISTIC REGRESSION — BASELINE MODEL
# ============================================================

space()

subsection("Logistic Regression — Baseline Model")

st.markdown(
    """
    Logistic Regression was implemented as the baseline linear classifier
    using standardized numerical features, class-balanced learning,
    L2 regularization, and mini-batch training.
    """
)


# ============================================================
# MODEL CONFIGURATION
# ============================================================

config_col1, config_col2, config_col3, config_col4, config_col5 = st.columns(
    5,
    gap="large"
)

with config_col1:

    pill("MODEL")

    st.markdown(
        '<div class="content-heading">SGD Logistic Regression</div>',
        unsafe_allow_html=True
    )


with config_col2:

    pill("SCALING")

    st.markdown(
        '<div class="content-heading">StandardScaler</div>',
        unsafe_allow_html=True
    )


with config_col3:

    pill("REGULARIZATION")

    st.markdown(
        '<div class="content-heading">L2</div>',
        unsafe_allow_html=True
    )


with config_col4:

    pill("CLASS BALANCE")

    st.markdown(
        '<div class="content-heading">Balanced Weights</div>',
        unsafe_allow_html=True
    )


with config_col5:

    pill("TRAINING")

    st.markdown(
        '<div class="content-heading">100K Mini-Batches</div>',
        unsafe_allow_html=True
    )


# ============================================================
# STANDARDIZATION
# ============================================================

st.markdown(
    '<div class="small-space"></div>',
    unsafe_allow_html=True
)


# ============================================================
# TEST PERFORMANCE
# ============================================================

space()

subsection("Test Performance")

metric_cards([
    ("📊", "71.36%", "Accuracy"),
    ("🎯", "14.20%", "Precision"),
    ("🔎", "53.80%", "Recall"),
    ("⚖️", "22.47%", "F1 Score"),
    ("📈", "0.6901", "ROC-AUC"),
    ("📉", "0.2264", "PR-AUC")
])


# ============================================================
# MODEL PERFORMANCE ANALYSIS
# ============================================================

space()

subsection("Model Performance Analysis")

performance_col1, performance_col2 = st.columns(
    2,
    gap="large"
)


# ============================================================
# ROC CURVE
# ============================================================

with performance_col1:

    pill("ROC CURVE")

    st.markdown(
        '<div class="content-heading">AUROC · 0.6901</div>',
        unsafe_allow_html=True
    )

    roc_image = IMAGE_DIR / "lr-roc-curve.png"

    if roc_image.exists():

        st.image(
            str(roc_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {roc_image.name}"
        )

    st.markdown(
        """
        Evaluates the model's ability to distinguish purchase from
        non-purchase outcomes across classification thresholds.
        """
    )


# ============================================================
# CONFUSION MATRIX
# ============================================================

with performance_col2:

    pill("CONFUSION MATRIX")

    st.markdown(
        '<div class="content-heading">Classification Performance</div>',
        unsafe_allow_html=True
    )

    confusion_image = IMAGE_DIR / "lr-confusion-metrics.png"

    if confusion_image.exists():

        st.image(
            str(confusion_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {confusion_image.name}"
        )

    st.markdown(
        """
        Shows the balance between correctly identified future purchases,
        missed purchases, and false-positive purchase predictions.
        """
    )


# ============================================================
# GLOBAL EXPLAINABILITY
# ============================================================

space()

subsection("Global Explainability")

st.markdown(
    """
    Logistic Regression coefficients and odds ratios were analyzed to
    understand the direction and magnitude of each feature's relationship
    with predicted purchase intent.
    """
)


# ============================================================
# COEFFICIENT + ODDS RATIO
# ============================================================

exp_col1, exp_col2 = st.columns(
    2,
    gap="large"
)


with exp_col1:

    pill("COEFFICIENT")

    st.markdown(
        '<div class="content-heading">Direction & Strength</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
- **Positive coefficient** → pushes prediction toward purchase
- **Negative coefficient** → pushes prediction away from purchase
- Larger absolute values indicate stronger model influence
- Standardization makes numerical coefficient magnitudes more comparable
"""
    )


with exp_col2:

    pill("ODDS RATIO")

    st.markdown(
        '<div class="content-heading">Effect on Purchase Odds</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
- Calculated as **exp(coefficient)**
- **Odds Ratio > 1** → higher predicted purchase odds
- **Odds Ratio < 1** → lower predicted purchase odds
- **Odds Ratio = 1** → no change in predicted odds
"""
    )


# ============================================================
# GLOBAL FEATURE INFLUENCE
# ============================================================

st.markdown(
    '<div class="small-space"></div>',
    unsafe_allow_html=True
)

subsection("Global Feature Influence")

feature_image = IMAGE_DIR / "feature-importance-lr.png"

if feature_image.exists():

    left, center, right = st.columns(
        [0.6, 2.8, 0.6]
    )

    with center:

        st.image(
            str(feature_image),
            use_container_width=True
        )

else:

    st.warning(
        f"Image not found: {feature_image.name}"
    )


# ============================================================
# KEY GLOBAL PURCHASE DRIVERS
# ============================================================

subsection("Key Global Purchase Drivers")

global_drivers = pd.DataFrame({
    "Feature": [
        "events_so_far",
        "views_so_far",
        "view_after_cart",
        "category_events_so_far",
        "event_type_view",
        "previous_event_cart"
    ],

    "Coefficient": [
        4.4972,
        -4.6013,
        0.5282,
        0.4583,
        -1.5663,
        -0.3913
    ],

    "Odds Ratio": [
        89.7657,
        0.0100,
        1.6959,
        1.5813,
        0.2088,
        0.6762
    ],

    "Direction": [
        "Positive",
        "Negative",
        "Positive",
        "Positive",
        "Negative",
        "Negative"
    ]
})

st.dataframe(
    global_drivers,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# GLOBAL INTERPRETATION
# ============================================================


# ============================================================
# LOCAL EXPLAINABILITY
# ============================================================

space()

subsection("Local Explainability — Single Prediction")

st.markdown(
    """
    Feature-level contributions were examined for an individual prediction
    to understand which signals pushed the model toward or away from purchase.
    """
)


# ============================================================
# LOCAL PREDICTION SUMMARY
# ============================================================

metric_cards([
    ("🎯", "100.0%", "Predicted Probability"),
    ("🤖", "Purchase", "Model Prediction"),
    ("📌", "No Purchase", "Actual Outcome")
])


# ============================================================
# LOCAL FEATURE CONTRIBUTIONS
# ============================================================

subsection("Top Feature Contributions")

contribution_table = pd.DataFrame({
    "Feature": [
        "events_so_far",
        "cart_to_view_ratio",
        "carts_so_far",
        "category_events_so_far",
        "product_views_so_far"
    ],

    "Contribution": [
        "+26.88",
        "-11.07",
        "-6.93",
        "+3.89",
        "+3.54"
    ],

    "Impact": [
        "Toward Purchase",
        "Away from Purchase",
        "Away from Purchase",
        "Toward Purchase",
        "Toward Purchase"
    ]
})

st.dataframe(
    contribution_table,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# LOCAL INTERPRETATION
# ============================================================

st.info(
    """
**Prediction Interpretation:** Strong session activity, repeated category
engagement, and repeated product views pushed the prediction toward purchase,
while cart-related signals pushed in the opposite direction.

Despite the strong predicted purchase intent, the customer ultimately did
not purchase, providing an example of a **high-confidence false positive**.
"""
)

space()

# ============================================================
# DECISION TREE — NONLINEAR MODEL
# ============================================================

space()

subsection("Decision Tree — Nonlinear Model")

st.markdown(
    """
    Decision Tree was evaluated as a nonlinear model to capture
    threshold-based relationships and interactions in customer purchase behavior.
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
        '<div class="content-heading">Decision Tree</div>',
        unsafe_allow_html=True
    )


with config_col2:

    pill("MAX DEPTH")

    st.markdown(
        '<div class="content-heading">10</div>',
        unsafe_allow_html=True
    )


with config_col3:

    pill("MIN LEAF SIZE")

    st.markdown(
        '<div class="content-heading">1,000</div>',
        unsafe_allow_html=True
    )


with config_col4:

    pill("CLASS BALANCE")

    st.markdown(
        '<div class="content-heading">Balanced Weights</div>',
        unsafe_allow_html=True
    )


# ============================================================
# MODEL-SPECIFIC PREPROCESSING
# ============================================================

st.markdown(
    '<div class="small-space"></div>',
    unsafe_allow_html=True
)

st.info(
    """
**No Feature Scaling**

Unlike Logistic Regression, numerical features were **not standardized**
for the Decision Tree. Tree-based models learn threshold-based splits,
so feature scaling is not required.
"""
)


# ============================================================
# TEST PERFORMANCE
# ============================================================

space()

subsection("Test Performance")

metric_cards([
    ("📊", "77.34%", "Accuracy"),
    ("🎯", "17.17%", "Precision"),
    ("🔎", "50.68%", "Recall"),
    ("⚖️", "25.65%", "F1 Score"),
    ("📈", "0.7046", "ROC-AUC"),
    ("📉", "0.2546", "PR-AUC")
])


st.info(
    """
**Model Performance:** Decision Tree improved **Precision, F1 Score,
ROC-AUC, and PR-AUC** over Logistic Regression, while Recall decreased
slightly. The higher PR-AUC indicates improved performance on the
minority purchase class.
"""
)


# ============================================================
# CLASSIFICATION PERFORMANCE
# ============================================================

space()

subsection("Classification Performance")

pill("CONFUSION MATRIX")

st.markdown(
    '<div class="content-heading">Decision Tree Predictions</div>',
    unsafe_allow_html=True
)

confusion_image = IMAGE_DIR / "dt-confusion-matrix.png"

if confusion_image.exists():

    left, center, right = st.columns(
        [1.25, 1.5, 1.25]
    )

    with center:

        st.image(
            str(confusion_image),
            width=480
        )

else:

    st.warning(
        f"Image not found: {confusion_image.name}"
    )


st.markdown(
    """
The model correctly classified **73.43% as No Purchase** and
**3.91% as Purchase**, while **18.86% were false positives**
and **3.80% were false negatives**.
"""
)


# ============================================================
# COMPARISON WITH LOGISTIC REGRESSION
# ============================================================

space()

subsection("Comparison with Logistic Regression")

st.markdown(
    """
    ROC and Precision–Recall curves compare the nonlinear Decision Tree
    against the Logistic Regression baseline across classification thresholds.
    """
)

roc_col, pr_col = st.columns(
    2,
    gap="large"
)


# ============================================================
# AUROC
# ============================================================

with roc_col:

    pill("ROC CURVE")

    st.markdown(
        '<div class="content-heading">AUROC · 0.7046</div>',
        unsafe_allow_html=True
    )

    roc_image = IMAGE_DIR / "dt-auroc.png"

    if roc_image.exists():

        st.image(
            str(roc_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {roc_image.name}"
        )

    st.markdown(
        """
        AUROC improved from **0.6901 → 0.7046**, indicating stronger
        overall discrimination than the Logistic Regression baseline.
        """
    )


# ============================================================
# PRECISION-RECALL
# ============================================================

with pr_col:

    pill("PRECISION–RECALL CURVE")

    st.markdown(
        '<div class="content-heading">PR-AUC · 0.2546</div>',
        unsafe_allow_html=True
    )

    pr_image = IMAGE_DIR / "dt-pr.png"

    if pr_image.exists():

        st.image(
            str(pr_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {pr_image.name}"
        )

    st.markdown(
        """
        PR-AUC improved from **0.2264 → 0.2546**, showing stronger
        performance on the minority purchase class.
        """
    )


# ============================================================
# MODEL COMPARISON
# ============================================================

space()

subsection("Model Comparison")

comparison_df = pd.DataFrame({

    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC",
        "PR-AUC"
    ],

    "Logistic Regression": [
        "71.36%",
        "14.20%",
        "53.80%",
        "22.47%",
        "0.6901",
        "0.2264"
    ],

    "Decision Tree": [
        "77.34%",
        "17.17%",
        "50.68%",
        "25.65%",
        "0.7046",
        "0.2546"
    ]
})

st.dataframe(
    comparison_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# GLOBAL EXPLAINABILITY
# ============================================================

space()

subsection("Global Explainability")

st.markdown(
    """
    Decision Tree feature importance measures how strongly each feature
    contributes to reducing classification impurity across the tree.
    """
)


# ============================================================
# FEATURE IMPORTANCE
# ============================================================

feature_image = IMAGE_DIR / "dt-feature-importance.png"

if feature_image.exists():

    left, center, right = st.columns(
        [0.8, 2.4, 0.8]
    )

    with center:

        st.image(
            str(feature_image),
            use_container_width=True
        )

else:

    st.warning(
        f"Image not found: {feature_image.name}"
    )


# ============================================================
# DECISION RULE EXPLAINABILITY
# ============================================================

space()

subsection("Decision Rule Explainability")

st.markdown(
    """
    The Decision Tree provides direct explainability through the sequence
    of threshold-based rules used to generate predictions.
    """
)


# ============================================================
# TREE VISUALIZATION
# ============================================================

tree_image = IMAGE_DIR / "dt-tree.png"

if tree_image.exists():

    st.image(
        str(tree_image),
        use_container_width=True
    )

else:

    st.warning(
        f"Image not found: {tree_image.name}"
    )


# ============================================================
# TREE INTERPRETATION
# ============================================================

st.info(
    """
**Decision Path Interpretation:** The tree begins with
`cart_to_view_ratio`, confirming it as the strongest decision signal.

Subsequent splits incorporate **product views, event type, hour, category,
price, cart activity, and interaction timing**, demonstrating nonlinear
relationships between behavioral, temporal, and product-level signals.
"""
)

space()
# ============================================================
# RANDOM FOREST — ENSEMBLE MODEL
# ============================================================

space()

subsection("Random Forest — Ensemble Model")

st.markdown(
    """
    Random Forest extends the Decision Tree approach by combining multiple
    trees to capture nonlinear behavioral patterns while improving prediction
    stability and generalization.
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

    pill("TREES")

    st.markdown(
        '<div class="content-heading">200 Estimators</div>',
        unsafe_allow_html=True
    )


with config_col2:

    pill("MAX DEPTH")

    st.markdown(
        '<div class="content-heading">20</div>',
        unsafe_allow_html=True
    )


with config_col3:

    pill("CLASS BALANCE")

    st.markdown(
        '<div class="content-heading">Balanced Subsample</div>',
        unsafe_allow_html=True
    )


with config_col4:

    pill("CRITERION")

    st.markdown(
        '<div class="content-heading">Entropy</div>',
        unsafe_allow_html=True
    )


# ============================================================
# ADDITIONAL MODEL SETTINGS
# ============================================================

st.markdown(
    '<div class="small-space"></div>',
    unsafe_allow_html=True
)

rf_config = pd.DataFrame({
    "Parameter": [
        "Min Samples Split",
        "Min Samples Leaf",
        "Max Features",
        "Bootstrap",
        "Training Sample / Tree"
    ],
    "Value": [
        "500",
        "200",
        "sqrt",
        "True",
        "80%"
    ]
})

st.dataframe(
    rf_config,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# MODEL-SPECIFIC PREPROCESSING
# ============================================================


# ============================================================
# TEST PERFORMANCE
# ============================================================

space()

subsection("Test Performance")

metric_cards([
    ("📊", "79.73%", "Accuracy"),
    ("🎯", "18.76%", "Precision"),
    ("🔎", "48.85%", "Recall"),
    ("⚖️", "27.11%", "F1 Score"),
    ("📈", "0.7162", "ROC-AUC"),
    ("📉", "0.2595", "PR-AUC")
])



# ============================================================
# THRESHOLD SELECTION
# ============================================================

space()

subsection("Classification Threshold Selection")

st.markdown(
    """
    Classification thresholds were evaluated on the **validation set**
    to examine the trade-off between Precision, Recall, and F1 Score.
    """
)

threshold_image = (
    IMAGE_DIR /
    "rf-threshold-selection.png"
)

if threshold_image.exists():

    left, center, right = st.columns(
        [0.8, 2.4, 0.8]
    )

    with center:

        st.image(
            str(threshold_image),
            use_container_width=True
        )

else:

    st.warning(
        f"Image not found: {threshold_image.name}"
    )


# ============================================================
# ROC + PRECISION RECALL COMPARISON
# ============================================================

space()

subsection("Comparison with Previous Models")

st.markdown(
    """
    Random Forest was compared with Logistic Regression and Decision Tree
    across classification thresholds.
    """
)

roc_col, pr_col = st.columns(
    2,
    gap="large"
)


# ============================================================
# AUROC
# ============================================================

with roc_col:

    pill("ROC CURVE")

    st.markdown(
        '<div class="content-heading">AUROC · 0.7162</div>',
        unsafe_allow_html=True
    )

    roc_image = (
        IMAGE_DIR /
        "rf-auroc.png"
    )

    if roc_image.exists():

        st.image(
            str(roc_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {roc_image.name}"
        )

    st.markdown(
        """
        AUROC improved from **0.6901 → 0.7046 → 0.7162**
        across Logistic Regression, Decision Tree, and Random Forest.
        """
    )


# ============================================================
# PRECISION RECALL
# ============================================================

with pr_col:

    pill("PRECISION–RECALL CURVE")

    st.markdown(
        '<div class="content-heading">PR-AUC · 0.2595</div>',
        unsafe_allow_html=True
    )

    pr_image = (
        IMAGE_DIR /
        "rf-pr-rec.png"
    )

    if pr_image.exists():

        st.image(
            str(pr_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {pr_image.name}"
        )

    st.markdown(
        """
        PR-AUC improved from **0.2264 → 0.2546 → 0.2595**,
        showing stronger performance on the imbalanced purchase target.
        """
    )



# ============================================================
# GLOBAL EXPLAINABILITY
# ============================================================

space()

subsection("Global Explainability")

st.markdown(
    """
    Random Forest feature importance aggregates information across
    the ensemble to identify the behavioral and contextual signals
    most influential in purchase prediction.
    """
)


# ============================================================
# GLOBAL FEATURE IMPORTANCE
# ============================================================

feature_image = (
    IMAGE_DIR /
    "rf-global.png"
)

if feature_image.exists():

    left, center, right = st.columns(
        [0.7, 2.6, 0.7]
    )

    with center:

        st.image(
            str(feature_image),
            use_container_width=True
        )

else:

    st.warning(
        f"Image not found: {feature_image.name}"
    )


st.markdown(
    """
`cart_to_view_ratio` emerged as the strongest global feature, followed by
`carts_so_far`, `cart_intensity`, and `product_views_so_far`, highlighting
the importance of **cart progression and repeated product engagement**.
"""
)


# ============================================================
# FEATURE IMPORTANCE STABILITY
# ============================================================

space()

subsection("Feature Importance Stability Across Trees")

st.markdown(
    """
    Feature importance was evaluated across individual trees to determine
    whether the strongest predictive signals remained consistent throughout
    the ensemble.
    """
)

feature_stability_image = (
    IMAGE_DIR /
    "rf-feature-expla.png"
)

if feature_stability_image.exists():

    left, center, right = st.columns(
        [0.7, 2.6, 0.7]
    )

    with center:

        st.image(
            str(feature_stability_image),
            use_container_width=True
        )

else:

    st.warning(
        f"Image not found: {feature_stability_image.name}"
    )


st.info(
    """
**Ensemble Interpretation:** Leading behavioral features remain influential
across multiple trees, while variation in importance reflects the diversity
introduced through bootstrap sampling and random feature selection.
"""
)


# ============================================================
# PREDICTED PROBABILITY DISTRIBUTION
# ============================================================

space()

subsection("Predicted Probability Distribution")

st.markdown(
    """
    Predicted probabilities were compared across actual purchase and
    non-purchase observations to examine how effectively the model
    separates the two outcome classes.
    """
)

probability_image = (
    IMAGE_DIR /
    "rf-predi-prob.png"
)

if probability_image.exists():

    left, center, right = st.columns(
        [0.7, 2.6, 0.7]
    )

    with center:

        st.image(
            str(probability_image),
            use_container_width=True
        )

else:

    st.warning(
        f"Image not found: {probability_image.name}"
    )


st.info(
    """
**Probability Interpretation:** Purchase observations shift toward higher
predicted probabilities, while non-purchase observations are concentrated
at lower probabilities. The overlap between the distributions represents
observations that remain difficult for the model to distinguish.
"""
)

# ============================================================
# XGBOOST — GRADIENT BOOSTING MODEL
# ============================================================

space()

subsection("XGBoost — Gradient Boosting Model")

st.markdown(
    """
    XGBoost was evaluated as an advanced boosting model to capture
    complex nonlinear relationships in customer purchase behavior while
    explicitly accounting for class imbalance.
    """
)


# ============================================================
# INITIAL MODEL CONFIGURATION
# ============================================================

config_col1, config_col2, config_col3, config_col4 = st.columns(
    4,
    gap="large"
)

with config_col1:

    pill("TREES")

    st.markdown(
        '<div class="content-heading">250 Estimators</div>',
        unsafe_allow_html=True
    )


with config_col2:

    pill("MAX DEPTH")

    st.markdown(
        '<div class="content-heading">10</div>',
        unsafe_allow_html=True
    )


with config_col3:

    pill("LEARNING RATE")

    st.markdown(
        '<div class="content-heading">0.10</div>',
        unsafe_allow_html=True
    )


with config_col4:

    pill("EVALUATION")

    st.markdown(
        '<div class="content-heading">PR-AUC</div>',
        unsafe_allow_html=True
    )


# ============================================================
# ADDITIONAL MODEL SETTINGS
# ============================================================

st.markdown(
    '<div class="small-space"></div>',
    unsafe_allow_html=True
)

xgb_config = pd.DataFrame({
    "Parameter": [
        "Subsample",
        "Features / Tree",
        "Class Imbalance",
        "Tree Method",
        "Categorical Support",
        "Validation Metric"
    ],
    "Value": [
        "70%",
        "70%",
        "scale_pos_weight",
        "Histogram",
        "Enabled",
        "PR-AUC"
    ]
})

st.dataframe(
    xgb_config,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# MODEL-SPECIFIC PREPROCESSING
# ============================================================



# ============================================================
# INITIAL TEST PERFORMANCE
# ============================================================

space()

subsection("Initial Model Performance")

metric_cards([
    ("📊", "79.92%", "Accuracy"),
    ("🎯", "18.87%", "Precision"),
    ("🔎", "48.59%", "Recall"),
    ("⚖️", "27.19%", "F1 Score"),
    ("📈", "0.7156", "ROC-AUC"),
    ("📉", "0.2649", "PR-AUC")
])



# ============================================================
# CLASSIFICATION PERFORMANCE
# ============================================================

space()

subsection("Classification Performance")

pill("CONFUSION MATRIX")

confusion_image = (
    IMAGE_DIR /
    "xgb-confusion.png"
)

if confusion_image.exists():

    left, center, right = st.columns(
        [1.25, 1.5, 1.25]
    )

    with center:

        st.image(
            str(confusion_image),
            width=480
        )

else:

    st.warning(
        f"Image not found: {confusion_image.name}"
    )


# ============================================================
# ROC + PRECISION RECALL
# ============================================================

space()

subsection("Comparison with Tree-Based Models")

st.markdown(
    """
    XGBoost was compared with Decision Tree and Random Forest using
    ROC-AUC and Precision–Recall performance.
    """
)

roc_col, pr_col = st.columns(
    2,
    gap="large"
)


# ============================================================
# AUROC
# ============================================================

with roc_col:

    pill("ROC CURVE")

    st.markdown(
        '<div class="content-heading">AUROC · 0.7156</div>',
        unsafe_allow_html=True
    )

    roc_image = (
        IMAGE_DIR /
        "xgb-auroc.png"
    )

    if roc_image.exists():

        st.image(
            str(roc_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {roc_image.name}"
        )

    st.markdown(
        """
        XGBoost achieved **0.7156 AUROC**, essentially matching
        Random Forest's **0.7162** overall discrimination.
        """
    )


# ============================================================
# PRECISION RECALL
# ============================================================

with pr_col:

    pill("PRECISION–RECALL CURVE")

    st.markdown(
        '<div class="content-heading">PR-AUC · 0.2649</div>',
        unsafe_allow_html=True
    )

    pr_image = (
        IMAGE_DIR /
        "xgb-pr.png"
    )

    if pr_image.exists():

        st.image(
            str(pr_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {pr_image.name}"
        )

    st.markdown(
        """
        XGBoost achieved the strongest initial **PR-AUC of 0.2649**
        on the imbalanced purchase target.
        """
    )


# ============================================================
# HYPERPARAMETER TUNING
# ============================================================

space()

subsection("Hyperparameter Tuning")

st.markdown(
    """
    Four XGBoost configurations were evaluated on the **validation set**
    across tree depth, learning rate, and number of estimators.
    **PR-AUC** was used as the primary model-selection metric.
    """
)


# ============================================================
# SEARCH SPACE
# ============================================================

tune_col1, tune_col2, tune_col3 = st.columns(
    3,
    gap="large"
)

with tune_col1:

    pill("MAX DEPTH")

    st.markdown(
        '<div class="content-heading">6 · 8</div>',
        unsafe_allow_html=True
    )


with tune_col2:

    pill("LEARNING RATE")

    st.markdown(
        '<div class="content-heading">0.05 · 0.10</div>',
        unsafe_allow_html=True
    )


with tune_col3:

    pill("ESTIMATORS")

    st.markdown(
        '<div class="content-heading">200 · 300</div>',
        unsafe_allow_html=True
    )


# ============================================================
# TUNING RESULTS
# ============================================================

st.markdown(
    '<div class="small-space"></div>',
    unsafe_allow_html=True
)

tuning_results = pd.DataFrame({

    "Depth": [
        6,
        8,
        6,
        8
    ],

    "Learning Rate": [
        0.05,
        0.05,
        0.10,
        0.10
    ],

    "Trees": [
        300,
        300,
        200,
        200
    ],

    "Precision": [
        "18.21%",
        "18.23%",
        "18.31%",
        "17.93%"
    ],

    "Recall": [
        "54.22%",
        "54.36%",
        "53.78%",
        "54.67%"
    ],

    "F1": [
        "27.26%",
        "27.30%",
        "27.31%",
        "27.01%"
    ],

    "PR-AUC": [
        "0.2757",
        "0.2771",
        "0.2756",
        "0.2755"
    ],

    "ROC-AUC": [
        "0.7171",
        "0.7163",
        "0.7165",
        "0.7148"
    ]
})

st.dataframe(
    tuning_results,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# SELECTED CONFIGURATION
# ============================================================

# ============================================================
# GLOBAL EXPLAINABILITY — SHAP
# ============================================================

space()

subsection("Global Explainability — SHAP")

st.markdown(
    """
    SHAP values quantify the average impact of each feature on
    XGBoost predictions across the evaluation population.
    """
)

shap_global_image = (
    IMAGE_DIR /
    "xgb-shap.png"
)

if shap_global_image.exists():

    left, center, right = st.columns(
        [1.15, 1.7, 1.15]
    )

    with center:

        st.image(
            str(shap_global_image),
            width=560
        )

else:

    st.warning(
        f"Image not found: {shap_global_image.name}"
    )


st.markdown(
    """
`views_so_far` produced the largest average SHAP impact, followed by
**brand, hour, events_so_far, category information, price, and
cart-to-view ratio**.
"""
)


# ============================================================
# LOCAL EXPLAINABILITY — SHAP
# ============================================================

space()

subsection("Local Explainability — SHAP")

st.markdown(
    """
    Local SHAP waterfall plots show how individual feature values move
    predictions away from the model baseline toward either purchase
    or no purchase.
    """
)

example_col1, example_col2 = st.columns(
    2,
    gap="large"
)


# ============================================================
# EXAMPLE 1
# ============================================================

with example_col1:

    pill("EXAMPLE 1 · NO PURCHASE")

    example_1_image = (
        IMAGE_DIR /
        "xgb-example 1.png"
    )

    if example_1_image.exists():

        st.image(
            str(example_1_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {example_1_image.name}"
        )


# ============================================================
# EXAMPLE 2
# ============================================================

with example_col2:

    pill("EXAMPLE 2 · HIGHER PURCHASE INTENT")

    example_2_image = (
        IMAGE_DIR /
        "xgb-example 2.png"
    )

    if example_2_image.exists():

        st.image(
            str(example_2_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {example_2_image.name}"
        )


# ============================================================
# SHAP INTERPRETATION
# ============================================================

st.info(
    """
**Reading SHAP:** Positive SHAP values push the prediction toward
**Purchase**, while negative SHAP values push the prediction toward
**No Purchase**. Larger absolute SHAP values indicate stronger influence
on the individual prediction.
"""
)

# ============================================================
# BUSINESS TARGETING PERFORMANCE
# ============================================================

space()

subsection("Business Targeting Performance")

st.markdown(
    """
    Lift analysis evaluates how effectively predicted probabilities
    concentrate actual purchasers within the highest-ranked sessions.
    """
)


lift_df = pd.DataFrame({

    "Targeted Population": [
        "Top 1%",
        "Top 5%",
        "Top 10%",
        "Top 20%",
        "Top 30%"
    ],

    "Precision": [
        "60.69%",
        "38.21%",
        "27.27%",
        "18.80%",
        "15.18%"
    ],

    "Recall": [
        "7.87%",
        "24.77%",
        "35.35%",
        "48.74%",
        "59.04%"
    ],

    "Lift": [
        "7.87×",
        "4.95×",
        "3.53×",
        "2.44×",
        "1.97×"
    ]
})

st.dataframe(
    lift_df,
    use_container_width=True,
    hide_index=True
)


st.info(
    """
**Business Interpretation:** The highest-scored **1% of sessions**
achieved **60.69% precision and 7.87× lift**.

Expanding targeting to the **top 10%** captures **35.35% of eventual
purchases** while maintaining **3.53× lift**, showing how model scores
can prioritize high-intent sessions.
"""
)

space()

# ============================================================
# LIGHTGBM — GRADIENT BOOSTING MODEL
# ============================================================

space()

subsection("LightGBM — Gradient Boosting Model")

st.markdown(
    """
    LightGBM was evaluated as an efficient gradient boosting model
    for capturing nonlinear purchase-intent patterns while accounting
    for the highly imbalanced target.
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

    pill("TREES")

    st.markdown(
        '<div class="content-heading">300 Estimators</div>',
        unsafe_allow_html=True
    )


with config_col2:

    pill("LEARNING RATE")

    st.markdown(
        '<div class="content-heading">0.05</div>',
        unsafe_allow_html=True
    )


with config_col3:

    pill("LEAVES")

    st.markdown(
        '<div class="content-heading">31</div>',
        unsafe_allow_html=True
    )


with config_col4:

    pill("CLASS WEIGHT")

    st.markdown(
        '<div class="content-heading">11.94</div>',
        unsafe_allow_html=True
    )


# ============================================================
# MODEL SETTINGS
# ============================================================

lgbm_config = pd.DataFrame({

    "Parameter": [
        "Estimators",
        "Learning Rate",
        "Number of Leaves",
        "Minimum Child Samples",
        "Subsample",
        "Features / Tree",
        "L1 Regularization",
        "L2 Regularization",
        "Class Imbalance",
        "Evaluation Metric"
    ],

    "Value": [
        "300",
        "0.05",
        "31",
        "100",
        "80%",
        "80%",
        "0.1",
        "1.0",
        "scale_pos_weight = 11.94",
        "Average Precision / PR-AUC"
    ]
})

st.dataframe(
    lgbm_config,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# CLASS IMBALANCE
# ============================================================

space()

subsection("Class Imbalance Handling")

imbalance_col1, imbalance_col2, imbalance_col3 = st.columns(
    3,
    gap="large"
)

with imbalance_col1:

    pill("NO PURCHASE")

    st.markdown(
        '<div class="content-heading">4,071,663</div>',
        unsafe_allow_html=True
    )


with imbalance_col2:

    pill("PURCHASE")

    st.markdown(
        '<div class="content-heading">341,073</div>',
        unsafe_allow_html=True
    )


with imbalance_col3:

    pill("PURCHASE RATE")

    st.markdown(
        '<div class="content-heading">7.73%</div>',
        unsafe_allow_html=True
    )


st.info(
    """
The training data was highly imbalanced, with purchases representing
only **7.73%** of observations. A **scale_pos_weight of 11.94** was
applied to increase the influence of the minority purchase class
during model training.
"""
)


# ============================================================
# VALIDATION PERFORMANCE
# ============================================================

space()

subsection("Validation Performance")

st.markdown(
    """
    Model performance was monitored on the **validation set** using
    Average Precision, while the test set remained untouched during
    model development and threshold selection.
    """
)


training_summary = pd.DataFrame({

    "Trees": [
        25,
        50,
        100,
        150,
        200,
        250,
        300
    ],

    "Validation PR-AUC": [
        0.2568,
        0.2685,
        0.2735,
        0.2753,
        0.2762,
        0.2763,
        0.2768
    ]
})

st.dataframe(
    training_summary,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# THRESHOLD OPTIMIZATION
# ============================================================

space()

subsection("Classification Threshold Optimization")

st.markdown(
    """
    Classification thresholds from **0.10 to 0.90** were evaluated
    using the validation set. The threshold maximizing **F1 Score**
    was selected before final test evaluation.
    """
)


threshold_col1, threshold_col2, threshold_col3 = st.columns(
    3,
    gap="large"
)

with threshold_col1:

    pill("DEFAULT")

    st.markdown(
        '<div class="content-heading">0.50</div>',
        unsafe_allow_html=True
    )


with threshold_col2:

    pill("SELECTED")

    st.markdown(
        '<div class="content-heading">0.70</div>',
        unsafe_allow_html=True
    )


with threshold_col3:

    pill("VALIDATION F1")

    st.markdown(
        '<div class="content-heading">32.04%</div>',
        unsafe_allow_html=True
    )


# ============================================================
# THRESHOLD RESULTS
# ============================================================

threshold_results = pd.DataFrame({

    "Threshold": [
        0.50,
        0.55,
        0.60,
        0.65,
        0.70,
        0.75,
        0.80
    ],

    "Precision": [
        "17.97%",
        "21.50%",
        "25.60%",
        "29.18%",
        "32.75%",
        "36.09%",
        "42.30%"
    ],

    "Recall": [
        "55.69%",
        "47.14%",
        "40.33%",
        "35.24%",
        "31.37%",
        "28.04%",
        "23.15%"
    ],

    "F1 Score": [
        "27.18%",
        "29.53%",
        "31.32%",
        "31.92%",
        "32.04%",
        "31.56%",
        "29.92%"
    ]
})

st.dataframe(
    threshold_results,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# THRESHOLD SELECTION IMAGE
# Exact filename: lightgbm-threshold.png
# ============================================================

threshold_image = (
    IMAGE_DIR /
    "lightgbm-threshold.png"
)

if threshold_image.exists():

    left, center, right = st.columns(
        [0.65, 2.7, 0.65]
    )

    with center:

        st.image(
            str(threshold_image),
            use_container_width=True
        )

else:

    st.warning(
        f"Image not found: {threshold_image.name}"
    )


st.info(
    """
**Selected Threshold · 0.70**

Validation F1 reached its maximum of **32.04%** at a threshold of
**0.70**, balancing **32.75% precision** with **31.37% recall**.
"""
)


# ============================================================
# FINAL TEST PERFORMANCE
# ============================================================

space()

subsection("Final Test Performance")

metric_cards([
    ("📊", "90.08%", "Accuracy"),
    ("🎯", "33.55%", "Precision"),
    ("🔎", "29.14%", "Recall"),
    ("⚖️", "31.19%", "F1 Score"),
    ("📈", "0.7240", "ROC-AUC"),
    ("📉", "0.2640", "PR-AUC")
])


st.info(
    """
At the validation-selected **0.70 threshold**, LightGBM achieved
**33.55% precision**, **29.14% recall**, and **31.19% F1 Score**
on the untouched test set.
"""
)


# ============================================================
# PREDICTED PROBABILITY DISTRIBUTION
# Exact filename: lightgbm-purchase pro.png
# ============================================================

space()

subsection("Predicted Probability Distribution")

st.markdown(
    """
    The probability distribution shows how predicted purchase scores
    differ between actual purchasers and non-purchasers relative to
    the selected classification threshold.
    """
)


probability_image = (
    IMAGE_DIR /
    "lightgbm-purchase pro.png"
)

if probability_image.exists():

    left, center, right = st.columns(
        [0.65, 2.7, 0.65]
    )

    with center:

        st.image(
            str(probability_image),
            use_container_width=True
        )

else:

    st.warning(
        f"Image not found: {probability_image.name}"
    )


st.markdown(
    """
Actual purchases are more concentrated in the higher predicted
probability range, while non-purchases are concentrated primarily
below the **0.70 classification threshold**.
"""
)


# ============================================================
# MODEL COMPARISON
# ============================================================

space()

subsection("Model Comparison")

comparison_df = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "XGBoost",
        "LightGBM"
    ],

    "Accuracy": [
        "71.36%",
        "77.34%",
        "79.73%",
        "79.92%",
        "90.08%"
    ],

    "Precision": [
        "14.20%",
        "17.17%",
        "18.76%",
        "18.87%",
        "33.55%"
    ],

    "Recall": [
        "53.80%",
        "50.68%",
        "48.85%",
        "48.59%",
        "29.14%"
    ],

    "F1 Score": [
        "22.47%",
        "25.65%",
        "27.11%",
        "27.19%",
        "31.19%"
    ],

    "ROC-AUC": [
        "0.6901",
        "0.7046",
        "0.7162",
        "0.7156",
        "0.7240"
    ],

    "PR-AUC": [
        "0.2264",
        "0.2546",
        "0.2595",
        "0.2649",
        "0.2640"
    ]
})

st.dataframe(
    comparison_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# MODEL TAKEAWAY
# ============================================================

st.info(
    """
**LightGBM Performance**

LightGBM achieved the highest **ROC-AUC (0.7240)** and
**F1 Score (31.19%)** among the evaluated models.

XGBoost retained a marginally higher **PR-AUC
(0.2649 vs. 0.2640)**, while LightGBM's validation-optimized
**0.70 threshold** produced a stronger precision–recall balance
for binary classification.
"""
)

space()
