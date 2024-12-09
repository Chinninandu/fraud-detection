import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
@st.cache  # Cache the dataset for faster loading
def load_data(filepath):
    return pd.read_csv(filepath)

# Load your dataset (replace with your file path)
DATA_PATH = "C:\project 1\PS_20174392719_1491204439457_log.csv"
data = load_data(DATA_PATH)

# App title
st.title("Crime and Incarceration Trends Analysis")

# Sidebar for filtering options
st.sidebar.header("Filter Options")
transaction_type = st.sidebar.selectbox("Select Transaction Type", data['type'].unique())

# Filter data based on the selected transaction type
filtered_data = data[data['type'] == transaction_type]

# Display filtered data
st.write(f"### Data for Transaction Type: {transaction_type}")
st.dataframe(filtered_data)

# Visualize distribution of transaction types
st.write("### Distribution of Transaction Types")
type_counts = data['type'].value_counts()
fig = px.pie(
    names=type_counts.index,
    values=type_counts.values,
    hole=0.5,
    title="Distribution of Transaction Types"
)
st.plotly_chart(fig)

# Visualize transaction amounts for the selected type
st.write(f"### Transaction Amounts for {transaction_type}")
fig_bar = px.bar(
    filtered_data,
    x='nameOrig',  # Adjust column name if needed
    y='amount',
    title=f"Transaction Amounts for {transaction_type}",
    labels={'nameOrig': 'Origin', 'amount': 'Amount'},
    height=500
)
st.plotly_chart(fig_bar)

 