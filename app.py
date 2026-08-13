# ============================================================
# WILL THIS SESSION CONVERT?
# E-COMMERCE PURCHASE INTENT DASHBOARD
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Will This Session Convert?",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Will This Session Convert?")
st.subheader("Predicting Purchase Intent")

st.caption(
    "Exploring customer behavior to understand the signals "
    "that indicate whether a purchase will occur within the current session."
)

st.divider()


# ============================================================
# LOAD DASHBOARD DATA
# ============================================================

@st.cache_data
def load_data():

    kpis = pd.read_csv("dashboard_data/kpis.csv")
    funnel = pd.read_csv("dashboard_data/funnel.csv")
    session_conversion = pd.read_csv(
        "dashboard_data/session_conversion.csv"
    )
    hourly = pd.read_csv("dashboard_data/hourly.csv")
    purchase_hourly = pd.read_csv(
        "dashboard_data/purchase_hourly.csv"
    )
    daily = pd.read_csv("dashboard_data/daily.csv")
    brands = pd.read_csv("dashboard_data/brands.csv")
    categories = pd.read_csv("dashboard_data/categories.csv")
    customer_behavior = pd.read_csv(
        "dashboard_data/customer_behavior.csv"
    )

    return (
        kpis,
        funnel,
        session_conversion,
        hourly,
        purchase_hourly,
        daily,
        brands,
        categories,
        customer_behavior
    )


(
    kpis,
    funnel,
    session_conversion,
    hourly,
    purchase_hourly,
    daily,
    brands,
    categories,
    customer_behavior
) = load_data()


# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================

st.header("📊 Executive Overview")

kpi = dict(
    zip(
        kpis["Metric"],
        kpis["Value"]
    )
)


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Customer Events",
    f"{int(kpi['Total Events']):,}"
)

col2.metric(
    "Unique Customers",
    f"{int(kpi['Unique Customers']):,}"
)

col3.metric(
    "User Sessions",
    f"{int(kpi['Unique Sessions']):,}"
)

col4.metric(
    "Unique Products",
    f"{int(kpi['Unique Products']):,}"
)


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Product Views",
    f"{int(kpi['Views']):,}"
)

col2.metric(
    "Cart Events",
    f"{int(kpi['Carts']):,}"
)

col3.metric(
    "Purchases",
    f"{int(kpi['Purchases']):,}"
)

col4.metric(
    "Session Conversion",
    f"{float(kpi['Conversion Rate']):.2f}%"
)


st.divider()


# ============================================================
# CUSTOMER JOURNEY
# ============================================================

st.header("🛍️ Customer Journey")

st.caption(
    "How customers move from product exploration to purchase."
)


fig = go.Figure(

    go.Funnel(

        y=funnel["Stage"],

        x=funnel["Events"],

        textinfo="value+percent initial"

    )

)


fig.update_layout(
    title="View → Cart → Purchase Funnel",
    height=450
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# ============================================================
# SESSION CONVERSION
# ============================================================

st.header("🎯 Do Sessions Convert?")


fig = px.bar(

    session_conversion,

    x="Outcome",

    y="Percentage",

    text="Percentage",

    title="Purchase vs No-Purchase Sessions"

)


fig.update_traces(

    texttemplate="%{text:.2f}%",

    textposition="outside"

)


fig.update_yaxes(
    title="Sessions (%)"
)


fig.update_xaxes(
    title=""
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# ============================================================
# REPEAT CUSTOMER BEHAVIOR
# ============================================================

st.header("🔁 Does Repeat Engagement Matter?")


fig = px.bar(

    customer_behavior,

    x="customer_type",

    y="conversion_rate",

    text="conversion_rate",

    title="Conversion Rate: Repeat vs One-Session Users"

)


fig.update_traces(

    texttemplate="%{text:.2f}%",

    textposition="outside"

)


fig.update_yaxes(
    title="Conversion Rate (%)"
)


fig.update_xaxes(
    title=""
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# ============================================================
# TEMPORAL BEHAVIOR
# ============================================================

st.header("⏰ When Are Customers Most Active?")


col1, col2 = st.columns(2)


with col1:

    fig = px.line(

        hourly,

        x="hour",

        y="Events",

        markers=True,

        title="Customer Activity by Hour"

    )


    fig.update_xaxes(
        dtick=1,
        title="Hour of Day"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


with col2:

    fig = px.line(

        purchase_hourly,

        x="hour",

        y="Purchases",

        markers=True,

        title="Purchases by Hour"

    )


    fig.update_xaxes(
        dtick=1,
        title="Hour of Day"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# DAY OF WEEK
# ============================================================

st.header("📅 Shopping Behavior by Day")


fig = px.bar(

    daily,

    x="day_of_week",

    y="Events",

    text="Events",

    title="Customer Activity by Day of Week"

)


fig.update_xaxes(
    title=""
)


fig.update_yaxes(
    title="Customer Events"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# ============================================================
# BRAND + CATEGORY
# ============================================================

st.header("🏆 What Are Customers Interested In?")


col1, col2 = st.columns(2)


with col1:

    fig = px.bar(

        brands,

        x="Events",

        y="Brand",

        orientation="h",

        title="Top 10 Brands by Engagement"

    )


    fig.update_layout(

        yaxis={
            "categoryorder":
            "total ascending"
        }

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


with col2:

    fig = px.bar(

        categories,

        x="Events",

        y="Category",

        orientation="h",

        title="Top Categories by Engagement"

    )


    fig.update_layout(

        yaxis={
            "categoryorder":
            "total ascending"
        }

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# BUSINESS INSIGHTS
# ============================================================

st.divider()

st.header("💡 What Did We Learn?")


col1, col2, col3 = st.columns(3)


with col1:

    st.info(
        """
        ### 🛒 Behavioral Intent

        Cart activity provides a strong signal of purchase intent.

        Customers progressing deeper into the funnel are more
        likely to convert.
        """
    )


with col2:

    st.info(
        """
        ### 🔁 Engagement

        Repeated customer interactions provide additional
        behavioral context for predicting conversion.

        Session history can help distinguish browsing from
        genuine purchase intent.
        """
    )


with col3:

    st.info(
        """
        ### ⏰ Context Matters

        Purchase behavior varies across time, products,
        categories and brands.

        These contextual signals can improve purchase
        prediction.
        """
    )


# ============================================================
# PREDICTION PROBLEM
# ============================================================

st.divider()

st.header("🤖 From EDA to Predictive Modeling")


st.markdown(
    """
    ### Prediction Question

    **Given everything a customer has done so far in the current
    session, will a purchase occur before the session ends?**
    """
)


st.markdown(
    """
    The exploratory analysis informed the creation of behavioral
    features that can be calculated at any point during a session:

    - Events observed so far
    - Views observed so far
    - Cart actions observed so far
    - Cart-to-view ratio
    - Whether a cart action has occurred
    - Session elapsed time
    - Previous customer action
    - Product interaction frequency
    - Brand interaction frequency
    - Category interaction frequency
    - Time of day
    - Product price characteristics
    """
)


st.success(
    "EDA  →  Behavioral Feature Engineering  →  "
    "Purchase Intent Prediction"
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "E-Commerce Purchase Intent Prediction | "
    "Exploratory Data Analysis & Machine Learning"
)
