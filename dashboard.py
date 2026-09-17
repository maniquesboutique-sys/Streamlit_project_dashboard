import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Project Delivery Dashboard")

# 1. Create a quick sample dataset using NumPy
np.random.seed(42)
data = {
    'Project': [f'Project {i}' for i in range(1, 11)],
    'Domain': ['FTTx', '5G Core', 'Cloud', 'FTTx', '5G Core', 'Cloud', 'FTTx', '5G Core', 'Cloud', 'FTTx'],
    'Budget_k': np.random.randint(50, 300, 10),
    'Delay_Days': np.random.randint(0, 30, 10)
}
df = pd.DataFrame(data)

# 2. Interactive Streamlit Filter Widget
domain_filter = st.selectbox("Select Domain:", ["All"] + list(df['Domain'].unique()))

if domain_filter != "All":
    filtered_df = df[df['Domain'] == domain_filter]
else:
    filtered_df = df

st.subheader("Filtered Projects")
st.dataframe(filtered_df)

# 3. Render a Seaborn Chart inside Streamlit
st.subheader("Budget vs Delay Days")
fig, ax = plt.subplots()
sns.barplot(data=filtered_df, x='Project', y='Budget_k', hue='Domain', ax=ax)
plt.xticks(rotation=45)

st.pyplot(fig)