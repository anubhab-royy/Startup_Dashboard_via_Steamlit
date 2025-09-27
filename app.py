import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Page-Config
st.set_page_config(layout='wide',page_title='Startup Analysis')

#Loading-CSV-File
df = pd.read_csv("startup_cleaned.csv")
df['date'] = pd.to_datetime(df['date'],errors='coerce')

#Investor-Details
def load_investor_details(investor):
    st.header('Name : '+investor)

    #Recent-5-Invesments
    lst5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most Recent Invesments')
    st.dataframe(lst5_df)

    col1, col2 = st.columns(2)

    #Biggest-Invesments
    with col1:
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Invesments')
        st.dataframe(big_series)

        fig1, ax1 = plt.subplots()
        ax1.bar(big_series.index, big_series.values)
        st.pyplot(fig1)

    with col2:
        vertical_series = df[df['investors'].str.contains('India Ventures')].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested-In')
        fig2, ax2 = plt.subplots()
        ax2.pie(vertical_series,labels=vertical_series.index)
        st.pyplot(fig2)

    st.subheader('Year-On-Year Invesment')
    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains('India Venture')].groupby('year')['amount'].sum()
    fig3, ax3 = plt.subplots()
    ax3.plot(year_series.index, year_series.values)
    st.pyplot(fig3)

#Overall-Analysis
def load_overall_analysis():
    col1, col2, col3, col4 = st.columns(4)

    total = round(df['amount'].sum())
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    avg_funding = round(df.groupby('startup')['amount'].sum().mean(),2)
    total_funded_startup = df['startup'].nunique()
    
    with col1:
        st.metric('Total',str(total)+'Cr')
    with col2:
        st.metric('Max',str(max_funding)+'Cr')
    with col3:
        st.metric('Average',str(avg_funding)+'Cr')
    with col4:
        st.metric('Total Funded Startups',str(total_funded_startup))

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    
    st.header('Month-On-Month Graph')
    select_option = st.selectbox('Select Type',['Total','Count'])
    if select_option == 'Total':
        temp_df = df.groupby(['year','month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year','month'])['amount'].count().reset_index()
    temp_df['x_axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype('str')
    fig4, ax4 = plt.subplots()
    ax4.plot(temp_df['x_axis'],temp_df['amount'])
    st.pyplot(fig4)

#Sidebar
st.sidebar.title("Startup Funding Analysis")

option = st.sidebar.selectbox('Select One',['Overall','StartUp','Investor'])
if option == 'Overall':
    st.title('Overall Analysis')
    load_overall_analysis()
elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp',sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select StartUp',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find StartUp Details')
    st.title('Investor Analysis')
    if btn2:
        load_investor_details(selected_investor)