import streamlit as st
import pandas as pd
import time



# Text Utility

st.title('Startup Dashboard')

st.header('I am learning Streamlit')

st.subheader('Anubhab Roy')

st.write('This is a normal text')

st.markdown("""
### My Favorite Games
- BGMI
- Detroit : Become Human
- Valorant            
""")

st.code("""
print("Welcome to Steamlit")
""")

st.latex('x^2 + y^2 + 2 = 0')




# Display Elements

df = pd.DataFrame({
    'name':['Anubhav','Vaibhav','Aritra'],
    'marks':[50,60,90],
    'package':[10,12,14]})
st.dataframe(df)

st.metric('Revenue','Rs 3L','-3%')

st.json({
    'name':['Anubhav','Vaibhav','Aritra'],
    'marks':[50,60,90],
    'package':[10,12,14]})



# Display Media

st.image('ghost_avatar.png')

st.video("D:\\Downloads\\Dump\Annabelle.2.Creation.2017.1080p.BluRay.H264.AAC-RARBG\\Annabelle.2.Creation.2017.1080p.BluRay.H264.AAC-RARBG.mp4")



# Create Layout

st.sidebar.title('Sidebar ka Title')

col1, col2 = st.columns(2)
with  col1:
    st.image("ghost_avatar.png")
with  col2:
    st.image("ghost_avatar.png")



# Showing Status

st.error("Login Failed")
st.success("Login Success")
st.warning("Warning")
st.info("Information")

bar = st.progress(0)
for i in range(1,101):
    time.sleep(0.01)
    bar.progress(i)



# Taking User Input

email = st.text_input("Enter Email")
password = st.text_input("Enter Password")
gen = st.selectbox("Select Gender",["Male","Female","Others"])

btn = st.button("Login")

if btn:
    if email == "asdf@gmail" and password == 'asdf':
        st.success("Login Success")
        st.balloons()
        st.write(gen)
    else:
        st.error("Login Failed")

file = st.file_uploader("Upload a CSV File")

if file is not None:
    read_file = pd.read_csv(file)
    st.dataframe(read_file.describe())