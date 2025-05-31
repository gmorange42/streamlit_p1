

#PLEASE COPY THE CONTAINT OF THIS FILE IN A PYTHON FILE (e.g. super_exo.py).
#THEN DO IN YOUR BACH TERMINAL "streamlit run super_exo.py"

import streamlit as st
import pandas as pd
import numpy as np

#Load csv
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv')

#Create dictionnary with borough name and images url
image_dict = {'Queens': 'https://th.bing.com/th/id/OIP.1Hsy9Cg76_TOnKDhdnmL-gHaE0?w=233&h=180&c=7&r=0&o=5&dpr=2.5&pid=1.7',
              'Manhattan': 'https://th.bing.com/th/id/OIP.-TzFBbHeO7cr_QR7Z466wQHaE8?w=282&h=188&c=7&r=0&o=5&dpr=2.5&pid=1.7',
              'Bronx': 'https://th.bing.com/th/id/OIP.c-LGr6-I0gjE4mjc0sTFDgHaE3?w=270&h=180&c=7&r=0&o=5&dpr=2.5&pid=1.7',
              'Brooklyn': 'https://th.bing.com/th/id/OIP.S1upVUcwRlvQsmGoNJcq2QHaE_?w=279&h=188&c=7&r=0&o=5&dpr=2.5&pid=1.7',
              np.nan: 'https://th.bing.com/th/id/OIP.X8IwbyQGIUFBJssHmf0VoQHaHa?w=162&h=180&c=7&r=0&o=5&dpr=2.5&pid=1.7'}

#Write title
st.title("Bienvenue sur le site de Guigui")

#Display selectbox to choose the pickup_borough
pickup_borough = st.selectbox(
    "Indiquez votre arrondissement de récupération",
    df['pickup_borough'].unique(),
)

#Write the pickup_borough
st.write("Tu as choisis:",pickup_borough)

#Display corresponding image
st.image(image_dict[pickup_borough])