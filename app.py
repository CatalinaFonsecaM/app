import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide')
st.title('project')


df = pd.read_csv('mercadeo1.csv')

col1, col2 = st.columns([2,3])

with col1: 
    st.header('Final Dataframe')
    st.dataframe(df.head())

    st.header('Statistical exploration')
    fig,ax = plt.subplots(1, 1, figsize=(10, 8))
    plt.hist(df['income'], bins=40, color='purple')
    st.pyplot(fig)

with col2:
    st.header('Average consume')
    fig,ax=plt.subplots(1,1, figsize=(20,6))
    (df
 .groupby(['cat_age'])['mntwines','mntfruits', 'mntmeatproducts','mntfishproducts','mntsweetproducts','mntgoldprods']
 .mean()
 .plot(kind='bar', stacked=True, cmap='plasma',ax=ax))
    st.pyplot(fig)
    
    st.header('Average income by education')
    fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    education_order = ['Basic', '2n Cycle', 'Graduation','Master','PhD']
    sns.violinplot(data=df, x='education', y='income',order=education_order, palette='plasma', ax=ax)
    st.pyplot(fig)

    st.header('segmentation 1')
    sns.boxplot(x='cat_age', y='mntwines', data=mercadeo,palette='plasma')