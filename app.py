import streamlit as st
import pandas as pd

# Run the app with:
# streamlit run app.py
# The app will be available at http://localhost:8501

# Load the data
data = pd.read_csv('data/sports-political-donations.csv')

# Sidebar widgets
st.sidebar.header('Filter Options')
min_amount = st.sidebar.slider('Minimum Donation Amount', 0, 1000000, 0)
max_amount = st.sidebar.slider('Maximum Donation Amount', 0, 1000000, 1000000)
party = st.sidebar.selectbox('Party', ['All', 'Democrat', 'Republican', 'Bipartisan'])

# Filter data based on user input
filtered_data = data[(data['Amount'].str.replace('[$,]', '', regex=True).astype(float) >= min_amount) &
                     (data['Amount'].str.replace('[$,]', '', regex=True).astype(float) <= max_amount)]

if party != 'All':
    filtered_data = filtered_data[filtered_data['Party'] == party]

# Display the filtered data
st.write(filtered_data)