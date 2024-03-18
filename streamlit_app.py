import streamlit as st 
import pandas as pd 
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTaUESVFbUnxC9q5-d-BiQXk6JD4r--bTZ3lNcryvfCeKqJq-tnz3VLhPwS_bZ5WXsRGYkOrtgkLlTU/pub?output=csv')
l=voc.shape[0]
i=np.random.choice(range(l))
word_fr=voc['Définition'].values[i]
word_chi=voc['Hanzi'].values[i]
word_pin=voc['Pinyin'].values[i]
st.write(word_fr+" | "+word_chi+" | "+word_pin)
st.button("refresh")
indices=np.random.choices(range(l),h=4,replace=False)
st.write(indices)
