import streamlit as st
import pandas as pd



# Loading CSV File
df = pd.read_csv("startup_funding.csv")



# Sidebar
st.sidebar.title("Startup Funding Analysis")

option = st.sidebar.selectbox('Select One',['Overall','StartUp','Investor'])

if option == 'Overall':
    st.title('Overall Analysis')

elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp',sorted(df['Startup Name'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')

else:
    st.sidebar.selectbox('Select StartUp',sorted(df['Investors Name'].fillna('Un-Disclosed').unique().tolist()))
    btn2 = st.sidebar.button('Find StartUp Details')
    st.title('Investor Analysis')