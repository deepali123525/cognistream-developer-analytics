
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="CogniStream Analytics",
    page_icon="💻",
    layout="wide"
)

st.title("💻 CogniStream")
st.subheader("Developer Flow-State & Cognitive Load Analytics")

# Load project data
activity = pd.read_csv("developer_activity.csv")
summary = pd.read_csv("developer_summary.csv")
flow = pd.read_csv("flow_metrics.csv")

# KPI cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Developers", activity["developer"].nunique())
col2.metric("Total Activity Events", len(activity))
col3.metric("90+ Min Flow Blocks", flow["flow_blocks_90_plus"].sum())

st.divider()

# Developer coding hours
st.subheader("Developer Focus Hours")

fig1 = px.bar(
    summary,
    x="developer",
    y="focus_hours",
    color="developer",
    title="Total Coding Focus Hours"
)

st.plotly_chart(fig1, use_container_width=True)

# Interruption analysis
st.subheader("Developer Interruptions")

fig2 = px.bar(
    summary,
    x="developer",
    y="interruptions",
    color="developer",
    title="Number of Slack Interruptions"
)

st.plotly_chart(fig2, use_container_width=True)

# Flow-state analysis
st.subheader("Uninterrupted Flow Blocks (90+ Minutes)")

fig3 = px.bar(
    flow,
    x="developer",
    y="flow_blocks_90_plus",
    color="developer",
    title="Developer Flow-State Performance"
)

st.plotly_chart(fig3, use_container_width=True)

# Raw data
st.subheader("Developer Activity Records")
st.dataframe(activity, use_container_width=True)

st.success("CogniStream Dashboard Loaded Successfully!")
