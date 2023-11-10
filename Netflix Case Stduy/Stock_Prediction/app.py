import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Netflix Stocks Trend")
uploaded_file = "NetflixStocks.csv"

df = pd.read_csv(uploaded_file)

st.subheader("Stock Summary")
st.write(df.describe())
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

#Opening visuals
st.subheader("Stock Price Plot (2002-2022)")
yearly_open = df.groupby('Year')['Open'].mean()
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
yearly_open.plot(kind='line', marker='o', color='blue')
plt.title('Average Open Amount by Year')
plt.xlabel('Year')
plt.ylabel('Open Amount')
plt.grid(True)
st.pyplot(plt)


#CLosing price visuals
st.subheader("Closing Price vs Time Chart")
fig=plt.figure(figsize=(12,6))
plt.plot(df.Close)
st.pyplot(fig)


#60 days moving avg
st.subheader("Closing Price vs Time Chart (60 Days Moving Avg)")
ma60=df.Close.rolling(60).mean()
fig=plt.figure(figsize=(12,6))
plt.plot(ma60)
plt.plot(df.Close)
st.pyplot(fig)


st.subheader("Closing Price vs Time Chart (90 Days vs 180 Days Moving Avg)")
ma90=df.Close.rolling(90).mean()
ma180=df.Close.rolling(180).mean()
fig=plt.figure(figsize=(12,6))
plt.plot(ma90)
plt.plot(ma180)
plt.plot(df.Close)
st.pyplot(fig)
