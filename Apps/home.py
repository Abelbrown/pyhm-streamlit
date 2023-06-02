import streamlit as st
import pandas as pd
import numpy as np


def app():
    st.title("H&M Personalized Fashion Recommendations")
    st.header('Provide product recommendations based on previous purchases')

    st.subheader('Context')
    st.markdown("""
    In the context of a kaggle competition, H&M Group invited all datascience lovers to develop product recommendations based oon the purchase history of customers across time, along with supporting metadata. 
    
    """)

    st.subheader('Purpose')
    
    st.markdown("""
    **The challenge facing all the candidates was to predict the articles that a customer would buy (12 best recommendations) in the 7-day period following the end of the training set.**

    The metric used and imposed by H&M to rank competitors is MAP@12 ( Mean Average Precision):
    """)

    st.write("""
    $$
    MAP@12 = 1/U \sum_{u=1}^{U} (1/min(m, 12))\sum_{k=1}^{min(n,12)}P(k) * rel(k)
    $$
    """
    )
    with st.expander("Principle AP@30"):
        st.image('.//data//figures_RNN//illu_MAP12.PNG',width=600)




