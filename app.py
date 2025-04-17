import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Exam 1 - EDA App", layout="wide")
st.title("📊 Exam 1 - Interactive EDA App")
st.markdown("**By Abdul Hadi**")

# Load CSV
df = pd.read_csv("clean_df.csv")

# Sidebar
st.sidebar.header("Filter Options")
show_data = st.sidebar.checkbox("Show Raw Data", value=True)
show_stats = st.sidebar.checkbox("Show Summary Statistics", value=True)
show_corr = st.sidebar.checkbox("Show Correlation Matrix", value=True)
show_plot = st.sidebar.checkbox("Show Scatter Plot", value=True)

if show_data:
    st.subheader("🔍 Raw Dataset Preview")
    st.dataframe(df)

if show_stats:
    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

if show_corr:
    st.subheader("📊 Correlation Matrix")
    corr = df.corr()
    st.dataframe(corr)

    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

if show_plot:
    st.subheader("📉 Scatter Plot")

    num_cols = df.select_dtypes(include='number').columns.tolist()
    x_col = st.selectbox("Select X-axis", num_cols, index=num_cols.index("symboling"))
    y_col = st.selectbox("Select Y-axis", num_cols, index=num_cols.index("normalized-losses"))

    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax2)
    st.pyplot(fig2)
