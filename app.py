import streamlit as st

st.title('🎈 App Name')

st.write('Hello world!')


# Run the app with:
# streamlit run app.py
# The app will be available at http://localhost:8501

# st.title('CSV File Uploader')

# # File uploader
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     # Read the CSV file
#     df = pd.read_csv(uploaded_file)
    
#     # Display the dataframe
#     st.write("Dataframe:")
#     st.dataframe(df)
    
#     # Show basic information
#     st.write("Basic Information:")
#     st.write(df.info())
    
#     # Show summary statistics
#     st.write("Summary Statistics:")
#     st.write(df.describe())