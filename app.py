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
    page_title="Will this Session convert into Purchase?",
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

st.markdown(
    """
<style>

/* ==========================================================
   ROOT TOKENS
   ========================================================== */

:root {
    --accent: #E72F3D;
    --accent-soft: rgba(231, 47, 61, 0.08);
    --accent-soft-strong: rgba(231, 47, 61, 0.14);
    --ink: #1F1F1F;
    --ink-muted: #555555;
    --ink-faint: #838383;
    --line: #EAEAEA;
    --surface: #FAFAFA;
}


/* ==========================================================
   HIDE DEFAULT STREAMLIT CHROME
   (prevents the fixed top toolbar from overlapping our header)
   ========================================================== */

header[data-testid="stHeader"] {
    display: none;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ==========================================================
   PAGE
   ========================================================== */

.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    padding-left: 3rem;
    padding-right: 3rem;
    max-width: 1400px;
}

html, body, [class*="css"] {
    font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, sans-serif;
}


/* ==========================================================
   NORMAL TEXT
   ========================================================== */

p, li {
    font-size: 15px !important;
    line-height: 1.62 !important;
    color: var(--ink-muted);
}

strong {
    color: var(--ink);
}

hr {
    margin: 0.6rem 0 !important;
    border-color: var(--line) !important;
}


/* ==========================================================
   HEADER
   ========================================================== */

.dashboard-header {
    display: flex;
    align-items: center;
    gap: 14px;
}

.dashboard-badge {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 46px;
    height: 46px;
    min-width: 46px;
    border-radius: 12px;
    background: linear-gradient(135deg, var(--accent) 0%, #C21F2C 100%);
    font-size: 22px;
    box-shadow: 0 4px 14px rgba(231, 47, 61, 0.28);
}

.dashboard-title {
    font-size: 27px;
    font-weight: 800;
    color: var(--ink);
    line-height: 1.2;
    margin: 0;
    letter-spacing: -0.3px;
}

.dashboard-subtitle {
    font-size: 15px;
    font-weight: 600;
    color: var(--ink-muted);
    margin-top: 3px;
}

.dashboard-description {
    font-size: 14.5px;
    color: var(--ink-faint);
    margin-top: 10px;
    padding-top: 12px;
    border-top: 1px solid var(--line);
    max-width: 900px;
}


/* ==========================================================
   SECTION TITLES
   ========================================================== */

.section-block {
    margin-top: 8px;
    padding-top: 26px;
    border-top: 1px solid var(--line);
}

.section-eyebrow {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.2px;
    color: var(--accent);
    text-transform: uppercase;
    margin-bottom: 4px;
}

.section-title {
    font-size: 21px;
    font-weight: 800;
    color: var(--ink);
    line-height: 1.25;
    margin-top: 0;
    margin-bottom: 3px;
    letter-spacing: -0.2px;
}

.section-subtitle {
    font-size: 14px;
    color: var(--ink-faint);
    line-height: 1.5;
    margin-top: 0;
    margin-bottom: 18px;
}

.subsection-title {
    font-size: 16px;
    font-weight: 700;
    color: var(--ink);
    line-height: 1.3;
    margin-top: 18px;
    margin-bottom: 10px;
    padding-left: 10px;
    border-left: 3px solid var(--accent);
}

.content-heading {
    font-size: 14.5px;
    font-weight: 700;
    color: #333333;
    margin-top: 4px;
    margin-bottom: 6px;
}


/* ==========================================================
   KPI CARDS
   ========================================================== */

.metric-row {
    display: flex;
    gap: 10px;
    margin-bottom: 4px;
}

.metric-card {
    text-align: center;
    padding: 14px 8px 12px 8px;
    min-height: 64px;
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 10px;
    width: 100%;
    transition: border-color 0.15s ease;
}

.metric-icon {
    font-size: 16px;
}

.metric-value {
    font-size: 19px;
    font-weight: 800;
    color: var(--accent);
    margin-left: 5px;
    letter-spacing: -0.2px;
}

.metric-label {
    font-size: 11.5px;
    font-weight: 600;
    color: var(--ink-faint);
    text-transform: uppercase;
    letter-spacing: 0.3px;
    margin-top: 5px;
}


/* ==========================================================
   PILLS
   ========================================================== */

.feature-pill {
    display: inline-block;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.4px;
    color: var(--accent);
    background-color: var(--accent-soft);
    border: 1px solid var(--accent-soft-strong);
    border-radius: 14px;
    padding: 4px 10px;
    margin-bottom: 9px;
}


/* ==========================================================
   TARGET VARIABLE
   ========================================================== */

.target-card {
    background-color: var(--surface);
    border: 1px solid var(--line);
    border-left: 4px solid var(--accent);
    border-radius: 8px;
    padding: 14px 18px;
    margin-top: 6px;
    margin-bottom: 10px;
}

.target-header {
    font-size: 15px;
    font-weight: 800;
    color: var(--accent);
    margin-bottom: 6px;
    font-family: "Source Code Pro", monospace;
}

.target-text {
    font-size: 14px;
    color: var(--ink-muted);
    line-height: 1.6;
}

.target-value {
    display: inline-block;
    font-size: 12.5px;
    font-weight: 700;
    color: var(--ink);
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 5px;
    padding: 2px 8px;
    margin-top: 8px;
    margin-right: 6px;
}


/* ==========================================================
   FUNNEL
   ========================================================== */

.funnel-stage-card {
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 14px 8px;
    text-align: center;
}

.funnel-arrow {
    text-align: center;
}


/* ==========================================================
   TABLES
   ========================================================== */

div[data-testid="stDataFrame"] {
    font-size: 13px !important;
    border: 1px solid var(--line);
    border-radius: 8px;
    overflow: hidden;
}


/* ==========================================================
   SELECT BOX
   ========================================================== */

div[data-testid="stSelectbox"] label p {
    font-size: 14px !important;
    font-weight: 700 !important;
    color: var(--ink) !important;
}

div[data-baseweb="select"] {
    font-size: 14px !important;
}


/* ==========================================================
   CONTAINERS / IMAGES
   ========================================================== */

div[data-testid="stImage"] img {
    border-radius: 8px;
    border: 1px solid var(--line);
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 10px !important;
}


/* ==========================================================
   FINAL MODEL
   ========================================================== */

.final-model-card {
    background: linear-gradient(135deg, var(--accent) 0%, #C21F2C 100%);
    border-radius: 12px;
    padding: 22px 26px;
    margin-top: 20px;
    box-shadow: 0 6px 20px rgba(231, 47, 61, 0.22);
}

.final-model-eyebrow {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.2px;
    color: rgba(255,255,255,0.85);
    text-transform: uppercase;
    margin-bottom: 4px;
}

.final-model {
    font-size: 22px;
    font-weight: 800;
    color: #FFFFFF;
    margin: 0;
}


/* ==========================================================
   FOOTER
   ========================================================== */

.app-footer {
    margin-top: 34px;
    padding-top: 16px;
    border-top: 1px solid var(--line);
    font-size: 12.5px;
    color: var(--ink-faint);
    text-align: center;
}


/* ==========================================================
   SPACING
   ========================================================== */

.section-space {
    height: 22px;
}

.small-space {
    height: 10px;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# REUSABLE COMPONENTS
# ============================================================

def section_title(title, subtitle, eyebrow=None):

    st.markdown(
        '<div class="section-block">',
        unsafe_allow_html=True
    )

    if eyebrow:

        st.markdown(
            f'<div class="section-eyebrow">{eyebrow}</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="section-subtitle">{subtitle}</div></div>',
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


def small_space():

    st.markdown(
        '<div class="small-space"></div>',
        unsafe_allow_html=True
    )


def metric_cards(cards):

    cols = st.columns(len(cards))

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


def centered_image(
    filename,
    width=None,
    ratio=(0.7, 2.6, 0.7)
):

    image_path = IMAGE_DIR / filename

    if image_path.exists():

        left, center, right = st.columns(ratio)

        with center:

            if width:

                st.image(
                    str(image_path),
                    width=width
                )

            else:

                st.image(
                    str(image_path),
                    use_container_width=True
                )

    else:

        st.warning(
            f"Image not found: {image_path.name}"
        )


# ============================================================
# DASHBOARD HEADER
# ============================================================

st.markdown(
    """
<div class="dashboard-header">
    <div class="dashboard-badge">🛒</div>
    <div>
        <div class="dashboard-title">Will Session Convert into Purchase?</div>
        <div class="dashboard-subtitle">Purchase Behavior Analytics &amp; Machine Learning Dashboard</div>
    </div>
</div>
<div class="dashboard-description">
    Predicting purchase intent from customer browsing, cart,
    product, and session behavior.
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# DATASET INFORMATION
# ============================================================

section_title(
    "Dataset Information",
    "One month of e-commerce behavioral data capturing View, Cart, and Purchase interactions.",
    eyebrow="Overview"
)

metric_cards([
    ("📊", "42.45M", "Total Records"),
    ("👥", "3.02M", "Unique Customers"),
    ("🛒", "9.24M", "Unique Sessions"),
    ("📦", "166,794", "Unique Products"),
    ("🏷️", "3,444", "Unique Brands"),
    ("🗂️", "126", "Unique Categories")
])

small_space()

metric_cards([
    ("🔢", "9", "Initial Features"),
    ("📅", "1 Month", "Dataset Period"),
    ("🧭", "4", "Category Levels"),
    ("👆", "3", "Event Types")
])


# ============================================================
# DATA QUALITY
# ============================================================

section_title(
    "Missing Value & Duplicate Records Analysis",
    "Assessment of missing values, recoverable product metadata, and duplicate records.",
    eyebrow="Data Quality"
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

left, right = st.columns(
    2,
    gap="large"
)

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
        """
**Recovery Strategy:** Missing brand values were recovered where a reliable
brand mapping existed for the same Product ID, restoring
**172,423 records (2.82%)**.
"""
    )


with right:

    subsection("Duplicate Record Analysis")

    st.dataframe(
        duplicate_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        """
**Duplicate Treatment:** 30,220 exact duplicate interaction records
(**0.07%**) were removed before downstream analysis.
"""
    )

    subsection("Missing Value Treatment")

    st.dataframe(
        treatment_table,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FEATURE ENGINEERING
# ============================================================

section_title(
    "Feature Engineering",
    "Generating predictive behavioral signals from customer activity observed up to the current interaction.",
    eyebrow="Modeling Prep"
)


# ============================================================
# FEATURE GENERATION
# ============================================================

subsection("01 · Feature Generation")

st.markdown(
    """
Behavioral and session-level features were generated using only information
available **up to the current interaction**, preventing future information
from leaking into model inputs.
"""
)

metric_cards([
    ("🧩", "14", "Generated Features"),
    ("👆", "4", "Behavioral"),
    ("🕒", "2", "Temporal / Session"),
    ("⚡", "2", "Session Intensity"),
    ("🎯", "4", "Purchase Intent"),
    ("🔄", "2", "Context")
])

small_space()

feature_groups = pd.DataFrame({
    "Feature Group": [
        "Behavioral",
        "Temporal / Session",
        "Session Intensity",
        "Purchase Intent",
        "Context"
    ],

    "Features": [
        "events_so_far · views_so_far · carts_so_far · product_views_so_far",
        "session_start · elapsed_seconds",
        "session_activity_rate · engagement_intensity",
        "repeat_product_view · previous_event_cart · fast_session · high_intent_no_cart",
        "brand_events_so_far · previous_event"
    ]
})

st.dataframe(
    feature_groups,
    use_container_width=True,
    hide_index=True
)

st.markdown(
    """
**Feature Engineering Principle:** Each observation represents a snapshot
of the customer session at the current interaction. Predictors are constructed
only from behavior that has already occurred, ensuring the model does not
have access to future session information.
"""
)


# ============================================================
# TARGET VARIABLE
# ============================================================

space()

subsection("Target Variable")

st.markdown(
"""<div class="target-card">
<div class="target-header">🎯 purchase_later</div>
<div class="target-text">
Predicts whether a purchase will occur later within the same user session using behavior observed up to the current interaction.
<div>
<span class="target-value">1 = Purchase Later</span>
<span class="target-value">0 = No Purchase Later</span>
</div>
</div>
</div>""",
    unsafe_allow_html=True
)


# ============================================================
# FEATURE ENCODING
# ============================================================

space()

subsection("02 · Feature Encoding")

st.markdown(
    """
Categorical variables were converted into model-ready numerical
representations based on their cardinality and model requirements.
"""
)

encoding_col1, encoding_col2 = st.columns(
    2,
    gap="large"
)

with encoding_col1:

    pill("FREQUENCY ENCODING")

    st.markdown(
        '<div class="content-heading">Brand</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
- Handles high-cardinality brand information
- Avoids thousands of sparse dummy variables
- Represents relative brand prevalence
- Reduces memory requirements
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
- Event type
- Day of week
- Category hierarchy
- Previous event

One-hot encoding avoids introducing an artificial ordinal relationship
between categorical values.
"""
    )


# ============================================================
# FUNNEL ANALYSIS & CONVERSION RATE
# ============================================================

section_title(
    "Funnel Analysis & Conversion Rate",
    "Event-level customer journey from product discovery to purchase.",
    eyebrow="Behavioral Analytics"
)


# ============================================================
# HORIZONTAL FUNNEL
# ============================================================

view_col, view_cart_col, cart_col, cart_purchase_col, purchase_col = st.columns(
    [2.2, 1.3, 2.2, 1.3, 2.2],
    gap="small"
)

funnel_stages = [
    (view_col, "👁️ VIEW", "23.31M", "23,306,949 events"),
    (cart_col, "🛒 CART", "499.1K", "499,095 events"),
    (purchase_col, "💳 PURCHASE", "558.5K", "558,484 events"),
]

funnel_arrows = [
    (view_cart_col, "2.14%", "View → Cart"),
    (cart_purchase_col, "111.90%", "Cart → Purchase"),
]

for col, label, value, caption in funnel_stages:

    with col:

        st.markdown(
            f"""
<div class="funnel-stage-card">
    <p style="text-align:center; font-size:13px; font-weight:700; color:#666666; margin-bottom:2px;">{label}</p>
    <p style="text-align:center; font-size:27px; font-weight:800; color:#E72F3D; margin:0;">{value}</p>
    <p style="text-align:center; font-size:12.5px; color:#888888; margin-top:2px; margin-bottom:0;">{caption}</p>
</div>
""",
            unsafe_allow_html=True
        )

for col, rate, label in funnel_arrows:

    with col:

        st.markdown(
            f"""
<div class="funnel-arrow">
    <p style="text-align:center; font-size:22px; font-weight:700; color:#E72F3D; margin-bottom:0;">→</p>
    <p style="text-align:center; font-size:17px; font-weight:700; color:#333333; margin:0;">{rate}</p>
    <p style="text-align:center; font-size:12px; color:#888888; margin-top:2px;">{label}</p>
</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# OVERALL VIEW → PURCHASE CONVERSION
# ============================================================

small_space()

overall_left, overall_center, overall_right = st.columns(
    [2, 2, 2]
)

with overall_center:

    st.markdown(
        """
<div style="text-align:center;">
    <p style="font-size:14px; color:#666666; margin-bottom:0;">Overall View → Purchase Conversion</p>
    <p style="font-size:24px; font-weight:800; color:#E72F3D; margin-top:2px;">2.40%</p>
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# FUNNEL INSIGHT
# ============================================================

subsection("💡 Funnel Insight")

st.markdown(
    """
Only **2.14% of view events progress to cart activity**, indicating that
the largest drop-off occurs before the cart stage. Overall, purchase events
represent **2.40% of view activity**.

**Note:** Cart → Purchase is **111.90%** because this is an aggregate
**event-level funnel**, not a strict sequential session-level funnel.
Purchase events can therefore exceed cart events.
"""
)


# ============================================================
# EXPLORATORY DATA ANALYSIS
# ============================================================

section_title(
    "Univariate / Bivariate / Multivariate Data Visualization",
    "Exploring customer behavior, purchase patterns, session activity, "
    "product characteristics, pricing, and temporal trends.",
    eyebrow="Exploratory Analysis"
)


# ============================================================
# VISUALIZATION CONFIGURATION
# ============================================================

eda_visualizations = {

    # ========================================================
    # UNIVARIATE ANALYSIS
    # ========================================================

    "Event Distribution":
        "event_distribution.png",

    "Purchase vs No-Purchase Sessions":
        "purchase_sessions.png",

    "Customer Activity by Day of Week":
        "day_of_week.png",


    # ========================================================
    # BIVARIATE ANALYSIS
    # ========================================================

    "Repeat Customer Conversion":
        "repeat_conversion.png",

    "Weekend vs Weekday Behavior":
        "weekend_weekday.png",

    "Price by Event Type":
        "price_event_type.png",

    "Session Behavior":
        "session_behavior.png",

    "Events Before Purchase":
        "events_before_purchase.png",

    "Time to First Purchase":
        "time_first_purchase.png",


    # ========================================================
    # MULTIVARIATE ANALYSIS
    # ========================================================

    "Brand Analysis":
        "brands.png",

    "Electronics Analysis":
        "electronics.png",

    "Price × Brand Analysis":
        "price-brand.png",

    "Multivariate Analysis":
        "multi-variate.png"
}


# ============================================================
# ANALYSIS TYPE
# ============================================================

analysis_type = {

    "Event Distribution":
        "UNIVARIATE",

    "Purchase vs No-Purchase Sessions":
        "UNIVARIATE",

    "Customer Activity by Day of Week":
        "UNIVARIATE",

    "Repeat Customer Conversion":
        "BIVARIATE",

    "Weekend vs Weekday Behavior":
        "BIVARIATE",

    "Price by Event Type":
        "BIVARIATE",

    "Session Behavior":
        "BIVARIATE",

    "Events Before Purchase":
        "BIVARIATE",

    "Time to First Purchase":
        "BIVARIATE",

    "Brand Analysis":
        "MULTIVARIATE",

    "Electronics Analysis":
        "MULTIVARIATE",

    "Price × Brand Analysis":
        "MULTIVARIATE",

    "Multivariate Analysis":
        "MULTIVARIATE"
}


# ============================================================
# BUSINESS INSIGHTS
# ============================================================

business_insights = {

    "Event Distribution":
        "Product views dominate customer activity, while purchases "
        "represent a much smaller share of interactions.",

    "Purchase vs No-Purchase Sessions":
        "Most customer sessions do not result in a purchase, "
        "highlighting the imbalance in conversion behavior.",

    "Customer Activity by Day of Week":
        "Tuesday records the highest purchase activity, making it "
        "a potentially important day for targeted engagement.",

    "Repeat Customer Conversion":
        "Repeat customers demonstrate stronger purchase intent "
        "than one-session customers.",

    "Weekend vs Weekday Behavior":
        "Weekday activity is higher than weekend activity, indicating "
        "stronger customer engagement during the workweek.",

    "Price by Event Type":
        "Purchased products are concentrated within a narrower price "
        "range than products customers only view.",

    "Session Behavior":
        "Customers who purchase demonstrate higher session engagement "
        "than customers who leave without purchasing.",

    "Events Before Purchase":
        "Purchase likelihood increases as customers interact with "
        "more events during a session.",

    "Time to First Purchase":
        "Most purchases occur relatively early in the session, "
        "suggesting purchase intent develops quickly.",

    "Brand Analysis":
        "Purchase behavior differs across brands, suggesting that "
        "brand preference contributes to customer purchase intent.",

    "Electronics Analysis":
        "Customer behavior varies across electronics product segments, "
        "highlighting differences in engagement and conversion patterns.",

    "Price × Brand Analysis":
        "Price and brand jointly influence purchase behavior, suggesting "
        "that customer price sensitivity varies across brands.",

    "Multivariate Analysis":
        "Purchase behavior is influenced by interactions between "
        "customer activity, product characteristics, price, and "
        "session-level engagement."
}


# ============================================================
# VISUALIZATION SELECTOR
# ============================================================

selected_visualization = st.selectbox(
    "Select an analysis",
    list(eda_visualizations.keys())
)


# ============================================================
# DISPLAY ANALYSIS TYPE
# ============================================================

pill(
    analysis_type[selected_visualization]
)


# ============================================================
# IMAGE PATH
# ============================================================

image_path = (
    IMAGE_DIR /
    eda_visualizations[selected_visualization]
)


# ============================================================
# DISPLAY VISUALIZATION
# ============================================================

if image_path.exists():

    left, center, right = st.columns(
        [0.7, 2.6, 0.7]
    )

    with center:

        subsection(
            selected_visualization
        )

        st.image(
            str(image_path),
            use_container_width=True
        )

else:

    st.warning(
        f"Visualization not found: {image_path.name}"
    )


# ============================================================
# BUSINESS INSIGHT
# ============================================================

subsection("💡 Business Insight")

st.markdown(
    f"""
**{business_insights[selected_visualization]}**
"""
)

# ============================================================
# TEXT ENRICHMENT
# ============================================================

section_title(
    "Product Description Generation — Text Generation + Enrichment",
    "Generating semantic product descriptions from structured metadata to introduce richer product context.",
    eyebrow="Enrichment Pipeline"
)

subsection(
    "Why Product Description Generation using LLM API?"
)

st.markdown(
    """
- **Product ID** and **Category ID** are internal identifiers and could not
  be reliably matched with external product databases.
- Open-source datasets contained similar metadata but lacked reliable
  descriptions mapped to these specific products.
- An **LLM API** was therefore used to generate standardized product
  descriptions from available product metadata.
"""
)


# ============================================================
# TEXT ENRICHMENT PIPELINE
# ============================================================

subsection("Text Enrichment Pipeline")

centered_image(
    "text_enrichment_pipeline.png",
    width=900,
    ratio=(0.5, 3, 0.5)
)


# ============================================================
# LLM SELECTION
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


st.markdown(
    """
**Model Selection Decision:** An OpenAI API model was selected because it
provided a practical balance between **cost, quality, speed, and scalability**.
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
# MACHINE LEARNING MODELING
# ============================================================

section_title(
    "Machine Learning Modeling",
    "Evaluating linear, tree-based, boosting, and ensemble models for future purchase-intent prediction.",
    eyebrow="Modeling"
)


# ============================================================
# TRAIN / VALIDATION / TEST
# ============================================================

subsection("Train / Validation / Test Split")

st.markdown(
    """
Data was split **chronologically at the user-session level** using each
session's start time, ensuring that an entire session belongs to only
one dataset.
"""
)

metric_cards([
    ("🧠", "70%", "Training Sessions"),
    ("⚙️", "15%", "Validation Sessions"),
    ("🧪", "15%", "Test Sessions")
])

small_space()

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


subsection("Why This Split?")

st.markdown(
    """
- **No session overlap** — all events from the same session remain together.
- **Prevents data leakage** across training and evaluation datasets.
- **Preserves chronology** by training on earlier sessions.
- **Production-like evaluation** measures performance on future sessions.
- Every model uses the **same validation and test datasets**.
"""
)


# ============================================================
# LOGISTIC REGRESSION
# ============================================================

space()

subsection("Logistic Regression — Baseline Model")

st.markdown(
    """
Logistic Regression provides an interpretable linear baseline.
Class-balanced learning was used to increase sensitivity to the minority
purchase class.
"""
)

metric_cards([
    ("📊", "39.55%", "Accuracy"),
    ("🎯", "9.76%", "Precision"),
    ("🔎", "82.92%", "Recall"),
    ("⚖️", "17.47%", "F1 Score"),
    ("📈", "0.6961", "ROC-AUC"),
    ("📉", "0.2294", "PR-AUC")
])

st.markdown(
    """
**Model Interpretation:** Logistic Regression achieved the **highest Recall
(82.92%)**, successfully identifying most future purchasers. However,
Precision was only **9.76%**, resulting in a large number of false-positive
purchase predictions.
"""
)


# ============================================================
# LOGISTIC REGRESSION — MODEL EVALUATION
# ============================================================

small_space()

subsection("Model Evaluation")


# ============================================================
# ROW 1 — ROC CURVE + CONFUSION MATRIX
# ============================================================

lr_roc_col, lr_confusion_col = st.columns(
    2,
    gap="large"
)


with lr_roc_col:

    pill("ROC CURVE")

    lr_roc_image = (
        IMAGE_DIR /
        "lr-roc-curve.png"
    )

    if lr_roc_image.exists():

        st.image(
            str(lr_roc_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {lr_roc_image.name}"
        )


with lr_confusion_col:

    pill("CONFUSION MATRIX")

    lr_confusion_image = (
        IMAGE_DIR /
        "lr-confusion-metrics.png"
    )

    if lr_confusion_image.exists():

        st.image(
            str(lr_confusion_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {lr_confusion_image.name}"
        )


# ============================================================
# ROW 2 — THRESHOLD + FEATURE IMPORTANCE
# ============================================================

small_space()

lr_threshold_col, lr_features_col = st.columns(
    2,
    gap="large"
)


with lr_threshold_col:

    pill("THRESHOLD ANALYSIS")

    lr_threshold_image = (
        IMAGE_DIR /
        "lr-threshold.png"
    )

    if lr_threshold_image.exists():

        st.image(
            str(lr_threshold_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {lr_threshold_image.name}"
        )


with lr_features_col:

    pill("GLOBAL FEATURE IMPORTANCE")

    lr_features_image = (
        IMAGE_DIR /
        "lr-features.png"
    )

    if lr_features_image.exists():

        st.image(
            str(lr_features_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {lr_features_image.name}"
        )


# ============================================================
# DECISION TREE
# ============================================================

space()

subsection("Decision Tree — Nonlinear Model")

st.markdown(
    """
Decision Tree was evaluated to capture nonlinear thresholds and interactions
between customer behavioral signals.
"""
)

metric_cards([
    ("📊", "74.64%", "Accuracy"),
    ("🎯", "15.95%", "Precision"),
    ("🔎", "53.55%", "Recall"),
    ("⚖️", "24.57%", "F1 Score"),
    ("📈", "0.6962", "ROC-AUC"),
    ("📉", "0.2478", "PR-AUC")
])

st.markdown(
    """
**Model Interpretation:** Decision Tree substantially improved Precision
and F1 Score over the linear baseline while retaining **53.55% Recall**.
"""
)


# ============================================================
# DECISION TREE — MODEL EVALUATION
# ============================================================

small_space()

subsection("Model Evaluation")


# ============================================================
# ROW 1 — CONFUSION MATRIX + ROC CURVE
# ============================================================

dt_confusion_col, dt_roc_col = st.columns(
    2,
    gap="large"
)

with dt_confusion_col:

    pill("CONFUSION MATRIX")

    image_path = IMAGE_DIR / "dt-confusion-matrix.png"

    if image_path.exists():

        st.image(
            str(image_path),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {image_path.name}"
        )


with dt_roc_col:

    pill("ROC CURVE")

    image_path = IMAGE_DIR / "dt-auroc.png"

    if image_path.exists():

        st.image(
            str(image_path),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {image_path.name}"
        )


# ============================================================
# ROW 2 — PR CURVE + FEATURE IMPORTANCE
# ============================================================

small_space()

dt_pr_col, dt_feature_col = st.columns(
    2,
    gap="large"
)

with dt_pr_col:

    pill("PRECISION–RECALL CURVE")

    image_path = IMAGE_DIR / "dt-pr.png"

    if image_path.exists():

        st.image(
            str(image_path),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {image_path.name}"
        )


with dt_feature_col:

    pill("GLOBAL FEATURE IMPORTANCE")

    image_path = IMAGE_DIR / "dt-feature-importance.png"

    if image_path.exists():

        st.image(
            str(image_path),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {image_path.name}"
        )


# ============================================================
# ROW 3 — DECISION TREE STRUCTURE
# ============================================================

small_space()

pill("DECISION TREE STRUCTURE")

dt_tree_image = IMAGE_DIR / "dt-tree.png"

if dt_tree_image.exists():

    left, center, right = st.columns(
        [0.3, 3.4, 0.3]
    )

    with center:

        st.image(
            str(dt_tree_image),
            use_container_width=True
        )

else:

    st.warning(
        f"Image not found: {dt_tree_image.name}"
    )


# ============================================================
# DECISION TREE INSIGHT
# ============================================================

small_space()

st.markdown(
    """
**Decision Tree Insight:** The tree structure provides a directly interpretable
view of how behavioral features split customers into different purchase-intent
segments, while feature importance highlights the variables contributing most
to the model's predictions.
"""
)

# ============================================================
# RANDOM FOREST
# ============================================================

space()

subsection("Random Forest — Ensemble Model")

st.markdown(
    """
Random Forest combines multiple decision trees to improve prediction
stability and capture nonlinear customer behavior.
"""
)


subsection("Base Random Forest")

metric_cards([
    ("📊", "72.34%", "Accuracy"),
    ("🎯", "15.25%", "Precision"),
    ("🔎", "56.72%", "Recall"),
    ("⚖️", "24.03%", "F1 Score"),
    ("📈", "0.7116", "ROC-AUC"),
    ("📉", "0.2516", "PR-AUC")
])


subsection("Tuned Random Forest")

metric_cards([
    ("📊", "72.65%", "Accuracy"),
    ("🎯", "15.19%", "Precision"),
    ("🔎", "55.55%", "Recall"),
    ("⚖️", "23.86%", "F1 Score"),
    ("📈", "0.7055", "ROC-AUC"),
    ("📉", "0.2471", "PR-AUC")
])

st.markdown(
    """
**Tuning Result:** Hyperparameter tuning did not improve Random Forest
PR-AUC. The base Random Forest remained stronger with **0.2516 PR-AUC**
compared with **0.2471** after tuning.
"""
)

small_space()

pill("MODEL EVALUATION")


# ============================================================
# ROW 1 — THRESHOLD SELECTION + ROC CURVE
# ============================================================

rf_threshold_col, rf_roc_col = st.columns(
    2,
    gap="large"
)

with rf_threshold_col:

    pill("THRESHOLD SELECTION")

    rf_threshold_image = IMAGE_DIR / "rf-threshold-selection.png"

    if rf_threshold_image.exists():

        st.image(
            str(rf_threshold_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {rf_threshold_image.name}"
        )


with rf_roc_col:

    pill("ROC CURVE")

    rf_roc_image = IMAGE_DIR / "rf-auroc.png"

    if rf_roc_image.exists():

        st.image(
            str(rf_roc_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {rf_roc_image.name}"
        )


# ============================================================
# ROW 2 — PRECISION–RECALL CURVE + FEATURE IMPORTANCE
# ============================================================

small_space()

rf_pr_col, rf_feature_col = st.columns(
    2,
    gap="large"
)

with rf_pr_col:

    pill("PRECISION–RECALL CURVE")

    rf_pr_image = IMAGE_DIR / "rf-pr-rec.png"

    if rf_pr_image.exists():

        st.image(
            str(rf_pr_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {rf_pr_image.name}"
        )


with rf_feature_col:

    pill("GLOBAL FEATURE IMPORTANCE")

    rf_feature_image = IMAGE_DIR / "rf-global.png"

    if rf_feature_image.exists():

        st.image(
            str(rf_feature_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {rf_feature_image.name}"
        )


# ============================================================
# RANDOM FOREST INSIGHT
# ============================================================

small_space()

st.markdown(
    """
**Random Forest Insight:** Cart progression and repeated product engagement
emerged as important predictive signals across the Random Forest ensemble.
"""
)


# ============================================================
# XGBOOST
# ============================================================

space()

subsection("XGBoost — Gradient Boosting Model")

st.markdown(
    """
XGBoost was evaluated to capture complex nonlinear relationships while
explicitly accounting for class imbalance.
"""
)


# ============================================================
# BASE XGBOOST
# ============================================================

subsection("Base XGBoost")

metric_cards([
    ("📊", "75.86%", "Accuracy"),
    ("🎯", "16.48%", "Precision"),
    ("🔎", "52.35%", "Recall"),
    ("⚖️", "25.07%", "F1 Score"),
    ("📈", "0.7072", "ROC-AUC"),
    ("📉", "0.2552", "PR-AUC")
])


# ============================================================
# XGBOOST TUNING
# ============================================================

small_space()

subsection("Hyperparameter Tuning")

st.markdown(
    """
Four XGBoost configurations were evaluated on the **validation set**
across tree depth, learning rate, and number of estimators.

**PR-AUC** was used as the primary tuning metric.
"""
)

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


small_space()

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

st.markdown(
    """
**Selected Configuration:** `max_depth = 8` · `learning_rate = 0.05` ·
`n_estimators = 300`

This configuration achieved the strongest validation **PR-AUC of 0.2771**.
"""
)

# ============================================================
# TUNED XGBOOST — TEST PERFORMANCE
# ============================================================

space()

subsection("Tuned XGBoost — Test Performance")

metric_cards([
    ("📊", "76.45%", "Accuracy"),
    ("🎯", "18.23%", "Precision"),
    ("🔎", "54.36%", "Recall"),
    ("⚖️", "27.30%", "F1 Score"),
    ("📈", "0.7163", "ROC-AUC"),
    ("📉", "0.2771", "PR-AUC")
])

small_space()

st.markdown(
    """
**Selected Configuration:** `max_depth = 8` · `learning_rate = 0.05` ·
`n_estimators = 300`

The tuned XGBoost model achieved **76.45% Accuracy**, **18.23% Precision**,
**54.36% Recall**, and a **PR-AUC of 0.2771**.
"""
)


# ============================================================
# XGBOOST GLOBAL SHAP
# ============================================================

space()

subsection("Global Explainability — SHAP")

st.markdown(
    """
SHAP values quantify the impact of each feature on XGBoost predictions
across the evaluation population.
"""
)

centered_image(
    "xgb-shap.png",
    width=560,
    ratio=(1.15, 1.7, 1.15)
)

st.markdown(
    """
SHAP analysis identifies the behavioral signals with the greatest influence
on model predictions and whether each feature pushes predictions toward
**Purchase** or **No Purchase**.
"""
)


# ============================================================
# XGBOOST LOCAL SHAP
# ============================================================

space()

subsection("Local Explainability — SHAP")

st.markdown(
    """
Local SHAP plots explain how individual feature values influence specific
purchase-intent predictions.
"""
)

example_col1, example_col2 = st.columns(
    2,
    gap="large"
)

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


st.markdown(
    """
**Reading SHAP:** Positive SHAP values push predictions toward
**Purchase**, while negative values push predictions toward
**No Purchase**. Larger absolute values indicate stronger influence.
"""
)


# ============================================================
# BUSINESS TARGETING PERFORMANCE
# ============================================================

space()

subsection("Business Targeting Performance")

st.markdown(
    """
Instead of relying only on a fixed classification threshold, predicted
probabilities can be used to rank sessions by purchase intent.
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

st.markdown(
    """
**Business Interpretation:** The highest-scored **1% of sessions**
achieved **60.69% Precision and 7.87× lift**.

Targeting the **top 10%** captures **35.35% of eventual purchases**
while maintaining **3.53× lift**, demonstrating how model scores can
prioritize high-intent sessions.
"""
)


# ============================================================
# LIGHTGBM
# ============================================================

space()

subsection("LightGBM — Gradient Boosting Model")

st.markdown(
    """
LightGBM was evaluated as an efficient gradient boosting alternative
for large-scale purchase-intent prediction.
"""
)

metric_cards([
    ("📊", "89.82%", "Accuracy"),
    ("🎯", "32.21%", "Precision"),
    ("🔎", "28.98%", "Recall"),
    ("⚖️", "30.51%", "F1 Score"),
    ("📈", "0.7018", "ROC-AUC"),
    ("📉", "0.2508", "PR-AUC")
])

st.markdown(
    """
**Model Interpretation:** LightGBM substantially increased Precision and
Accuracy, but Recall declined to **28.98%**. This means more than 70% of
actual future purchasers were not identified.
"""
)

small_space()

pill("MODEL EVALUATION")

lgbm_threshold_col, lgbm_purchase_col = st.columns(
    2,
    gap="large"
)

with lgbm_threshold_col:

    pill("THRESHOLD ANALYSIS")

    lgbm_threshold_image = IMAGE_DIR / "lightgbm-threshold.png"

    if lgbm_threshold_image.exists():

        st.image(
            str(lgbm_threshold_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {lgbm_threshold_image.name}"
        )


with lgbm_purchase_col:

    pill("PURCHASE PROBABILITY DISTRIBUTION")

    lgbm_purchase_image = IMAGE_DIR / "lightgbm-purchase pro.png"

    if lgbm_purchase_image.exists():

        st.image(
            str(lgbm_purchase_image),
            use_container_width=True
        )

    else:

        st.warning(
            f"Image not found: {lgbm_purchase_image.name}"
        )


# ============================================================
# XGBOOST + RANDOM FOREST ENSEMBLE
# ============================================================

space()

subsection("XGBoost + Random Forest Ensemble")

st.markdown(
    """
An ensemble was evaluated by combining predictions from XGBoost and
Random Forest to determine whether complementary tree structures could
improve overall performance.
"""
)

metric_cards([
    ("📊", "90.14%", "Accuracy"),
    ("🎯", "33.43%", "Precision"),
    ("🔎", "28.13%", "Recall"),
    ("⚖️", "30.55%", "F1 Score"),
    ("📈", "0.7114", "ROC-AUC"),
    ("📉", "0.2560", "PR-AUC")
])

st.markdown(
    """
**Ensemble Result:** The ensemble achieved the highest Accuracy,
Precision and F1 Score. However, Recall declined to **28.13%**, and
PR-AUC remained slightly below Tuned XGBoost.
"""
)


# ============================================================
# FINAL MODEL COMPARISON
# ============================================================

section_title(
    "Final Model Comparison",
    "Performance comparison across all candidate models on the held-out test set.",
    eyebrow="Results"
)

final_comparison = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest — Base",
        "Random Forest — Tuned",
        "XGBoost — Base",
        "XGBoost — Tuned",
        "LightGBM",
        "XGBoost + RF Ensemble"
    ],

    "Accuracy": [
        "39.55%",
        "74.64%",
        "72.34%",
        "72.65%",
        "75.86%",
        "76.45%",
        "89.82%",
        "90.14%"
    ],

    "Precision": [
        "9.76%",
        "15.95%",
        "15.25%",
        "15.19%",
        "16.48%",
        "16.74%",
        "32.21%",
        "33.43%"
    ],

    "Recall": [
        "82.92%",
        "53.55%",
        "56.72%",
        "55.55%",
        "52.35%",
        "51.68%",
        "28.98%",
        "28.13%"
    ],

    "F1 Score": [
        "17.47%",
        "24.57%",
        "24.03%",
        "23.86%",
        "25.07%",
        "25.29%",
        "30.51%",
        "30.55%"
    ],

    "ROC-AUC": [
        "0.6961",
        "0.6962",
        "0.7116",
        "0.7055",
        "0.7072",
        "0.7100",
        "0.7018",
        "0.7114"
    ],

    "PR-AUC": [
        "0.2294",
        "0.2478",
        "0.2516",
        "0.2471",
        "0.2552",
        "0.2568",
        "0.2508",
        "0.2560"
    ]
})

st.dataframe(
    final_comparison,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# MODEL PERFORMANCE TRADE-OFF
# ============================================================

small_space()

subsection("Model Performance Trade-Off")

tradeoff_df = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Tuned XGBoost",
        "LightGBM",
        "XGBoost + RF Ensemble"
    ],

    "Primary Strength": [
        "Highest Recall",
        "Highest PR-AUC",
        "High Precision & Accuracy",
        "Highest Precision & F1"
    ],

    "Key Limitation": [
        "Very low Precision",
        "Moderate Precision",
        "Low Recall",
        "Low Recall"
    ]
})

st.dataframe(
    tradeoff_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# CONCLUSION — FINAL MODEL SELECTION
# ============================================================

section_title(
    "Final Model Selection",
    "Selecting the model that provides the strongest balance for purchase-intent prediction.",
    eyebrow="Final Model Selection"
)

st.markdown(
    """
<div class="final-model-card">
    <div class="final-model-eyebrow">🏆 Selected Model</div>
    <div class="final-model">Tuned XGBoost</div>
</div>
""",
    unsafe_allow_html=True
)

small_space()

metric_cards([
    ("📊", "76.45%", "Accuracy"),
    ("🎯", "18.23%", "Precision"),
    ("🔎", "54.36%", "Recall"),
    ("⚖️", "27.30%", "F1 Score"),
    ("📈", "0.7163", "ROC-AUC"),
    ("📉", "0.2771", "PR-AUC")
])

small_space()

st.markdown(
    """
**Final Model:** Tuned XGBoost achieved **76.45% Accuracy**, 
**18.23% Precision**, **54.36% Recall**, **27.30% F1 Score**, 
**0.7163 ROC-AUC**, and **0.2771 PR-AUC**.
"""
)

# ============================================================
# SELECTION RATIONALE
# ============================================================

small_space()

subsection("Why Tuned XGBoost?")

st.markdown(
    """
**Tuned XGBoost was selected because it achieved the highest PR-AUC
(`0.2568`) while retaining over half of actual future purchasers
(`51.68% Recall`)** — the strongest overall Precision–Recall trade-off
among all evaluated models.
"""
)

rationale_col1, rationale_col2 = st.columns(
    2,
    gap="large"
)

with rationale_col1:

    st.markdown(
        """
- **Logistic Regression** led on Recall (82.92%) but Precision was only
  9.76% — too many false positives to act on.
- **LightGBM** and the **ensemble** pushed Precision above 32%, but
  Recall fell below 29% — most purchasers were missed.
"""
    )

with rationale_col2:

    st.markdown(
        """
- **Tuned XGBoost** balances both: highest PR-AUC, meaningful Precision,
  and Recall above 50%.
- Accuracy alone was not used to select the model, since the purchase
  class is a small minority — high Accuracy is easy to achieve while
  still missing most purchasers.
"""
    )


# ============================================================
# FINAL MODEL CARD
# ============================================================

space()

st.markdown(
    """
<div class="final-model-card">
    <div class="final-model-eyebrow">Final Model</div>
    <p class="final-model">🏆 Tuned XGBoost</p>
</div>
""",
    unsafe_allow_html=True
)

# ============================================================
# LIMITATIONS & FUTURE WORK
# ============================================================

section_title(
    "Limitations & Future Work",
    "Trade-offs made in this project, and what would change with more time or data.",
    eyebrow="Reflection"
)

lim_col1, lim_col2, lim_col3 = st.columns(
    3,
    gap="large"
)

with lim_col1:

    pill("LIMITATIONS")

    st.markdown(
        """
- Only one month of data — seasonality and long-term trends aren't captured
- Features describe the current session only, not the customer's history
- Severe class imbalance keeps Precision low across every model tested
"""
    )


with lim_col2:

    pill("TRADE-OFFS MADE")

    st.markdown(
        """
- Optimized for PR-AUC and Recall over raw Accuracy, given how rare
  purchases are
- Chose Tuned XGBoost over the ensemble — traded some Precision for
  meaningfully higher Recall
- Stuck to tree-based models over deep sequence models, to keep training
  and inference simple
"""
    )


with lim_col3:

    pill("WITH MORE TIME OR DATA")

    st.markdown(
        """
- Collect more data — multiple months to capture seasonality and trends
- Continue feature engineering — customer-level history, pricing, and
  richer temporal signals
- Try sequence models (RNN / Transformer) directly on event streams
- Add production monitoring to catch performance drift over time
"""
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="app-footer">
    E-Commerce Purchase Prediction Dashboard · Behavioral Analytics &amp; Machine Learning
</div>
""",
    unsafe_allow_html=True
)
