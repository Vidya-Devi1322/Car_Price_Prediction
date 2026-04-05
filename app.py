import streamlit as st
import pandas as pd
import pickle as pkl 

ds = pd.read_csv("clean_data.csv")
st.title("Car Project")
# st.write("Enter Company name")
company = sorted(ds["company"].unique())
selcompany = st.selectbox("Enter Company name",company)
name =sorted(ds[ds["company"] == selcompany]["name"].unique())
selname = st.selectbox("Select Car",name)
years = [] 
for i in  range(2000,2027):
    years.append(i)
selyear = int(st.selectbox("select year",years))
selkm =int(st.number_input("Enter Car Driven in KM",min_value=500))
fuel_type = sorted(ds["fuel_type"].unique())
selfuel_type = st.selectbox("select fuel type",fuel_type)
inputdata = [selname,selcompany,selyear,selkm,selfuel_type]
data = pd.DataFrame(data=[inputdata],columns=["name","company","year","kms_driven","fuel_type"])
pipe = pkl.load(open("CPP.pkl","rb+"))
if st.button("Check"):
    price = pipe.predict(data)
    st.write(price)
