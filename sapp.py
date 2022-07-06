
from turtle import title
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.write("""
# Visualizing   Titanic Data

Shown are the  **Survivors Distribution in Tintanic** with respective ***Correlates***

""")

titanic=pd.read_csv('titanic_train (3).csv')

st.write("""
## count plot
""")
def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Count Plot", #New page
        ]
    )

    if page == "Line Plot":
        linePlot()
    
    elif page == "Count Plot":
        countPlot()
    elif page == "Box plot":
        BoxPlot()
    elif page == "Bar plot":
        Barplot()
def countPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(x = "Sex",hue='Survived', data = titanic)
    st.pyplot(fig)

countPlot()
st.write("""
## Box plot
""")
def BoxPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(x='Embarked', y='Age', data=titanic)
    st.pyplot(fig)

BoxPlot()
st.write("""
## Bar plot
""")
def Barplot():
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(x='Sex', y='Fare', data=titanic)
    st.pyplot(fig)

Barplot()


