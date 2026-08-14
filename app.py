# ============================================================
# IMPORTS
# ============================================================

import streamlit as st
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Purchase Prediction",
    page_icon="🛒",
    layout="wide"
)


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"


# ============================================================
# GLOBAL STYLING
# ============================================================

st.markdown(
    """
    <style>

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    h1 {
        font-size: 34px !important;
        font-weight: 700 !important;
    }

    h2 {
        font-size: 27px !important;
        font-weight: 700 !important;
        margin-top: 20px !important;
    }

    h3 {
        font-size: 21px !important;
        font-weight: 650 !important;
    }

    h4 {
        font-size: 17px !important;
        font-weight: 650 !important;
        margin-bottom: 12px !important;
    }

    .section-caption {
        color: #666666;
        font-size: 15px;
        line-height: 1.6;
        margin-top: -8px;
        margin-bottom: 25px;
    }

    .model-description {
        color: #555555;
        font-size: 15px;
        line-height: 1.65;
        margin-bottom: 25px;
    }

    .key-takeaway {
        margin-top: 28px;
        padding: 18px 20px;
        background-color: #F8F9FA;
        border-left: 4px solid #E72F3D;
        border-radius: 8px;
    }

    .takeaway-title {
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .takeaway-text {
        font-size: 14px;
        color: #555555;
        line-height: 1.6;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def subsection(title):

    st.markdown(f"### {title}")


def add_space(height=25):

    st.markdown(
        f"<div style='height:{height}px;'></div>",
        unsafe_allow_html=True
    )


def show_image(image_path):

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
# MACHINE LEARNING
# ============================================================

st.divider()

st.markdown("## Machine Learning")

st.markdown(
    """
    <div class="section-caption">
        Multiple classification models were evaluated to predict whether
        a purchase will occur later within the same user session.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOGISTIC REGRESSION
# ============================================================

subsection("Logistic Regression")

st.markdown(
    """
    <div class="model-description">
        Logistic Regression was used as an interpretable baseline model
        for predicting future purchase intent from customer behavioral,
        session, temporal, product, and categorical features.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOGISTIC REGRESSION IMAGE PATHS
# ============================================================

lr_confusion = IMAGE_DIR / "lr-confusion-metrics.png"

lr_features = IMAGE_DIR / "lr-features.png"

lr_local = IMAGE_DIR / "lr-local.png"

lr_roc = IMAGE_DIR / "lr-roc-curve.png"

lr_threshold = IMAGE_DIR / "lr-threshold.png"


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.markdown("#### Model Performance")

st.markdown(
    """
    <div class="section-caption">
        Classification performance and discrimination capability
        of the Logistic Regression model on the holdout dataset.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# ROW 1
# CONFUSION MATRIX + AUROC
# ============================================================

col1, col2 = st.columns(
    2,
    gap="large"
)


with col1:

    st.markdown(
        "##### Confusion Matrix"
    )

    show_image(
        lr_confusion
    )


with col2:

    st.markdown(
        "##### AUROC Curve"
    )

    show_image(
        lr_roc
    )


add_space(35)


# ============================================================
# THRESHOLD ANALYSIS
# ============================================================

st.markdown("#### Threshold Optimization")

st.markdown(
    """
    <div class="section-caption">
        Classification thresholds were evaluated to understand the
        trade-off between precision, recall, and overall predictive performance.
    </div>
    """,
    unsafe_allow_html=True
)


left, center, right = st.columns(
    [0.35, 2.3, 0.35]
)


with center:

    show_image(
        lr_threshold
    )


add_space(35)


# ============================================================
# GLOBAL MODEL EXPLAINABILITY
# ============================================================

st.markdown("#### Global Model Explainability")

st.markdown(
    """
    <div class="section-caption">
        Global feature effects show which customer behavior and session
        characteristics contribute most strongly to the model predictions.
    </div>
    """,
    unsafe_allow_html=True
)


left, center, right = st.columns(
    [0.25, 2.5, 0.25]
)


with center:

    show_image(
        lr_features
    )


add_space(35)


# ============================================================
# LOCAL MODEL EXPLAINABILITY
# ============================================================

st.markdown("#### Local Model Explainability")

st.markdown(
    """
    <div class="section-caption">
        Local explainability illustrates how individual feature values
        influence the predicted purchase probability for a specific observation.
    </div>
    """,
    unsafe_allow_html=True
)


left, center, right = st.columns(
    [0.25, 2.5, 0.25]
)


with center:

    show_image(
        lr_local
    )


add_space(25)


# ============================================================
# LOGISTIC REGRESSION TAKEAWAY
# ============================================================

st.markdown(
    """
    <div class="key-takeaway">

        <div class="takeaway-title">
            Key Takeaway
        </div>

        <div class="takeaway-text">
            Logistic Regression provides an interpretable baseline for
            purchase prediction. The model establishes baseline discrimination
            performance while allowing both global and individual prediction
            drivers to be examined. Threshold optimization provides additional
            flexibility when balancing precision and recall.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


add_space(40)
