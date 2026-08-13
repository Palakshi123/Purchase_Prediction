import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Will This Session Convert?",
    page_icon="🛒",
    layout="wide"
)

# ============================================================
# HERO SECTION
# ============================================================

st.title("🛒 Will This Session Convert?")

st.subheader("Predicting Purchase Intent")

st.markdown(
    """
    ### From Browsing Behavior to Purchase Prediction

    An end-to-end data science framework analyzing customer
    behavior and predicting whether a purchase will occur
    within the current user session.
    """
)

st.divider()

# ============================================================
# PROJECT OBJECTIVE
# ============================================================

st.header("🎯 Project Objective")

st.markdown(
    """
    - Analyze customer behavior across **views, carts, and purchases**
    - Identify behavioral signals associated with **purchase intent**
    - Predict whether a **purchase will occur before the current session ends**
    - Translate model predictions into actionable customer insights
    """
)

st.divider()

# ============================================================
# PROJECT WORKFLOW
# ============================================================

st.header("🔬 Data Science Framework")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("01")
    st.write("**EDA**")
    st.caption("Understand customer behavior")

with col2:
    st.subheader("02")
    st.write("**Feature Engineering**")
    st.caption("Build behavioral signals")

with col3:
    st.subheader("03")
    st.write("**Modeling**")
    st.caption("Predict purchase intent")

with col4:
    st.subheader("04")
    st.write("**Evaluation**")
    st.caption("Measure model performance")

st.divider()

# ============================================================
# PREDICTION QUESTION
# ============================================================

st.header("💡 The Prediction Question")

st.info(
    """
    Given everything a customer has done so far in the current
    session, will a purchase occur before the session ends?
    """
)

st.divider()

st.caption(
    "E-Commerce Purchase Intent Prediction | Machine Learning Project"
)
