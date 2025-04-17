import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Exam1 - Abdul Hadi", layout="wide")
st.title("📊 Exam 1 - Exploratory Data Analysis App")
st.markdown("**By Abdul Hadi**")

df = pd.read_csv("exam1_abdulhadi.csv")

st.subheader("🧾 Dataset Preview")
st.dataframe(df)

cols = ['bore', 'stroke', 'compression-ratio', 'horsepower']
st.subheader("📈 Descriptive Statistics")
st.write(df[cols].describe())

st.subheader("📊 Pearson Correlation Matrix")
corr = df[cols].corr()
st.dataframe(corr)

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="YlGnBu", ax=ax)
st.pyplot(fig)

st.subheader("📉 Scatter Plot")
num_cols = df.select_dtypes(include='number').columns.tolist()
x_col = st.selectbox("Choose X-axis", num_cols)
y_col = st.selectbox("Choose Y-axis", num_cols, index=1 if len(num_cols) > 1 else 0)

fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax2)
st.pyplot(fig2)
