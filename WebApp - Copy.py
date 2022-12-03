import streamlit as st
#from sklearn import datasets
#from import Model
st.title("Dataset")

st.write("""
Explore Different classifier
Which one is best?
""")

dataset_name=st.sidebar.selectbox("Select Dataset",("Accident_Severity","Model","Accident-filtered"))

classifier_name=st.sidebar.selectbox("Select Classifier", (""))

