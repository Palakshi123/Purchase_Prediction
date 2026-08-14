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
# REUSABLE COMPONENTS
# ============================================================

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
        '<div style="height:22px;"></div>',
        unsafe_allow_html=True
    )


def small_space():
    st.markdown(
        '<div style="height:10px;"></div>',
        unsafe_allow_html=True
    )


def metric_cards(cards):

    cols = st.columns(len(cards))

    for col, (icon, value, label) in zip(cols, cards):

        with col:

            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    padding:14px 8px 12px 8px;
                    min-height:64px;
                    background:#FFFFFF;
                    border:1px solid #EAEAEA;
                    border-radius:10px;
                ">
                    <span style="font-size:16px;">
                        {icon}
                    </span>

                    <span style="
                        font-size:19px;
                        font-weight:800;
                        color:#E72F3D;
                        margin-left:5px;
                    ">
                        {value}
                    </span>

                    <div style="
                        font-size:11.5px;
                        font-weight:600;
                        color:#838383;
                        text-transform:uppercase;
                        margin-top:5px;
                    ">
                        {label}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# XGBOOST
# ============================================================

space()

subsection("XGBoost — Gradient Boosting Model")

st.markdown(
    """
XGBoost was evaluated to capture complex nonlinear relationships between
customer behavioral signals while explicitly accounting for class imbalance.
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


st.markdown(
    """
**Base Model Interpretation:** The initial XGBoost model achieved
**52.35% Recall** with a **PR-AUC of 0.2552**, providing a strong
starting point for hyperparameter optimization.
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

Because purchase prediction is an **imbalanced classification problem**,
**PR-AUC** was used as the primary metric for model selection.
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
        """
### 6 · 8

Controls the complexity of individual trees.
"""
    )


with tune_col2:

    pill("LEARNING RATE")

    st.markdown(
        """
### 0.05 · 0.10

Controls how strongly each tree contributes to the model.
"""
    )


with tune_col3:

    pill("ESTIMATORS")

    st.markdown(
        """
### 200 · 300

Controls the number of boosting trees.
"""
    )


# ============================================================
# TUNING RESULTS
# ============================================================

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

    "F1 Score": [
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

space()

subsection("Selected Tuned XGBoost Model")

st.markdown(
    """
The configuration with the **highest validation PR-AUC** was selected
as the final tuned XGBoost model.
"""
)


# ============================================================
# SELECTED HYPERPARAMETERS
# ============================================================

pill("SELECTED HYPERPARAMETERS")

metric_cards([
    ("🌳", "8", "Max Depth"),
    ("⚡", "0.05", "Learning Rate"),
    ("🌲", "300", "Estimators")
])


# ============================================================
# VALIDATION PERFORMANCE
# ============================================================

small_space()

pill("VALIDATION PERFORMANCE")

metric_cards([
    ("🎯", "18.23%", "Precision"),
    ("🔎", "54.36%", "Recall"),
    ("⚖️", "27.30%", "F1 Score"),
    ("📉", "0.2771", "PR-AUC"),
    ("📈", "0.7163", "ROC-AUC")
])


st.markdown(
    """
**Selection Decision:** `max_depth = 8`, `learning_rate = 0.05`,
and `n_estimators = 300` achieved the strongest validation
**PR-AUC of 0.2771** and was therefore selected for final evaluation.
"""
)


# ============================================================
# FINAL TUNED XGBOOST — TEST PERFORMANCE
# ============================================================

space()

subsection("Final Tuned XGBoost — Test Performance")

st.markdown(
    """
After selecting the best configuration using the validation set,
the tuned model was evaluated on the **held-out test set**.
"""
)


metric_cards([
    ("📊", "76.45%", "Accuracy"),
    ("🎯", "16.74%", "Precision"),
    ("🔎", "51.68%", "Recall"),
    ("⚖️", "25.29%", "F1 Score"),
    ("📈", "0.7100", "ROC-AUC"),
    ("📉", "0.2568", "PR-AUC")
])


st.markdown(
    """
**Test Result:** Tuned XGBoost achieved a **PR-AUC of 0.2568**
on completely unseen test data while retaining **51.68% Recall**.

The difference between validation and test performance is expected because
the validation set was used for model selection, whereas the test set
provides the final unbiased evaluation.
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


xgb_shap_image = IMAGE_DIR / "xgb-shap.png"


if xgb_shap_image.exists():

    left, center, right = st.columns(
        [1.15, 1.7, 1.15]
    )

    with center:

        st.image(
            str(xgb_shap_image),
            width=560
        )

else:

    st.warning(
        f"Image not found: {xgb_shap_image.name}"
    )


st.markdown(
    """
SHAP analysis identifies the behavioral signals with the greatest
influence on model predictions and whether each feature pushes
predictions toward **Purchase** or **No Purchase**.
"""
)


# ============================================================
# LOCAL SHAP
# ============================================================

space()

subsection("Local Explainability — SHAP")

st.markdown(
    """
Local SHAP plots explain how individual feature values influence
specific purchase-intent predictions.
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
Instead of relying only on a fixed classification threshold,
predicted probabilities can be used to rank sessions by
purchase intent.
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
while maintaining **3.53× lift**, demonstrating how model scores
can prioritize high-intent sessions.
"""
)
