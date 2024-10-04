import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('day.csv')

workingdays_counts = data['workingday'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    workingdays_counts, 
    labels=workingdays_counts.index,
    autopct='%1.1f%%',
    startangle=90)
plt.title('Perbandingan Peminjaman Sepeda di hari kerja (1) dan nonkerja (0)')
st.title("Submission by Alif Adhitya | ML 74")
st.pyplot(plt)

data_season1 = data[data['season'] == 1]
data_season2 = data[data['season'] == 2]
data_season3 = data[data['season'] == 3]
data_season4 = data[data['season'] == 4]

def plot_pie_chart(data_counts, title):
    plt.figure(figsize=(6, 6))
    plt.pie(data_counts, labels=data_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title(title)
    return plt 

col1, col2 = st.columns(2)

with col1:
    st.pyplot(plot_pie_chart(data_season1['workingday'].value_counts(), 'Musim Semi (Spring)'))
    st.pyplot(plot_pie_chart(data_season3['workingday'].value_counts(), 'Musim Gugur (Fall)'))

with col2:
    st.pyplot(plot_pie_chart(data_season2['workingday'].value_counts(), 'Musim Panas (Summer)'))
    st.pyplot(plot_pie_chart(data_season4['workingday'].value_counts(), 'Musim Dingin (Winter)'))
