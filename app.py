import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Exam1 - Abdul Hadi", layout="wide")

st.title("📊 Exam 1 - Exploratory Data Analysis App")
st.markdown("**By Abdul Hadi**")

# --- Dataset from notebook (manually included) ---
data = {
    "symboling": [3, 1, 2, 3, 0],
    "normalized-losses": [NaN, 164, 164, NaN, 158],
    "make": ["alfa-romero", "audi", "audi", "bmw", "chevrolet"],
    "fuel-type": ["gas", "gas", "gas", "gas", "gas"],
    "aspiration": ["std", "std", "std", "std", "std"],
    "num-of-doors": ["two", "four", "four", "two", "two"],
    "body-style": ["convertible", "sedan", "sedan", "sedan", "hatchback"],
    "drive-wheels": ["rwd", "fwd", "4wd", "rwd", "fwd"],
    "engine-location": ["front", "front", "front", "front", "front"],
    "wheel-base": [88.6, 99.8, 99.4, 101.2, 94.5],
    "length": [168.8, 176.6, 176.6, 176.8, 157.1],
    "width": [64.1, 66.2, 66.4, 64.8, 64.2],
    "height": [48.8, 54.3, 54.3, 54.3, 53.3],
    "curb-weight": [2548, 2337, 2824, 2395, 1874],
    "engine-type": ["dohc", "ohc", "ohc", "ohc", "l"],
    "num-of-cylinders": ["four", "four", "five", "six", "three"],
    "engine-size": [130, 109, 136, 108, 61],
    "fuel-system": ["mpfi", "mpfi", "mpfi", "mpfi", "2bbl"],
    "bore": [3.47, 3.19, 3.19, 3.5, 2.91],
    "stroke": [2.68, 3.4, 3.4, 3.39, 3.03],
    "compression-ratio": [9.0, 10.0, 8.0, 8.8, 9.5],
    "horsepower": [111, 102, 115, 101, 48],
    "peak-rpm": [5000, 5500, 5500, 5800, 5100],
    "city-mpg": [21, 24, 18, 23, 47],
    "highway-mpg": [27, 30, 22, 29, 53],
    "price": [13495, 17450, 15250, 17710, 5151]
}
df = pd.DataFrame(data)

# --- Show Dataset ---
st.subheader("🧾 Dataset Preview")
st.dataframe(df)

# --- Descriptive Stats ---
cols = ['bore', 'stroke', 'compression-ratio', 'horsepower']
st.subheader("📈 Descriptive Statistics")
st.write(df[cols].describe())

# --- Correlation ---
st.subheader("📊 Pearson Correlation Matrix")
corr = df[cols].corr()
st.dataframe(corr)

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="YlGnBu", ax=ax)
st.pyplot(fig)

# --- Scatter Plot ---
st.subheader("📉 Scatter Plot")
num_cols = df.select_dtypes(include='number').columns.tolist()
x_col = st.selectbox("Choose X-axis", num_cols)
y_col = st.selectbox("Choose Y-axis", num_cols, index=1 if len(num_cols) > 1 else 0)

fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax2)
st.pyplot(fig2)
