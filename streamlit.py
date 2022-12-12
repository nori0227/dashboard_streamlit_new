import pandas as pd
import streamlit as st
import numpy as np

st.title('FIFA WORLDCUP 2022 Playing Time & Stats Data')

st.caption('These datatsets are public and were retreived on Dec 12, 2022')
#### Dataframe 1 - Head 25 ####
#header
st.header('FIFA WORLDCUP 2022 Player Playing Time')
#### Caption ####
st.caption('This dataset provides a good understanding of playing time for players in FIFA World CUP 2022')
df1 = pd.read_csv('player_playingtime.csv')
df1 = df1.head(25)
df1


## dataframe 2 - Head 100
#header
st.header('FIFA WOLDCUP 2022 Player Playing Time')
#### Caption ####
st.caption('This dataset provides a good understanding of stats for players in FIFA World CUP 2022')
df2 = pd.read_csv('player_stats.csv')
df2 = df2.head(100)
df2

#### Toggle ####

if st.checkbox('Show first 100 records of FIFA 2022 Worldcup'):
    st.dataframe(df1)

# Displaying the dataframe
if st.checkbox('player_stats'):
    st.dataframe(df2)
# Creating a barchart
st.subheader('Display of  Number of Yellow Cards Received by Players')
cards_yellow= df2['cards_yellow'].value_counts()
st.bar_chart(cards_yellow)
st.caption('Visual provides insight of players numbers getting number of yellow cards')

# Creating a line chart
st.subheader('Number of Goals')
num_goals = df2['goals'].value_counts()
st.bar_chart(num_goals)
st.caption('Visual provides insight on the number of players drawing goals')

