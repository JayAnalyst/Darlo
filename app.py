import streamlit as st
import pandas as pd 
from data_vizzes import create_pizza_plots,setup_and_find_similar_players
from mplsoccer import PyPizza, add_image, FontManager
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist
st.set_page_config(layout="wide")

def load_cbs_data():
    path = 'central_defenders.csv'
    return pd.read_csv(path)
def load_cms_data():
    path = 'central_midfielders.csv'
    return pd.read_csv(path)
positions = st.selectbox(label='Select position',options = ['Central Defenders','Central Midfielders'])
if positions == 'Central Defenders':
    roles = st.selectbox(label='Select Role',options = ['stopper_rating','central_defender_rating','ball_playing_center_back_rating','ball_carrying_center_back_rating','avg_rating'])
if positions == 'Central Defenders':
    data = load_cbs_data()
    data1 = st.dataframe(data.iloc[:,1:].drop_duplicates().reset_index(drop='index').sort_values(roles,ascending=False).reset_index(drop='index'))
    data2 = data.iloc[:,1:].drop_duplicates().reset_index(drop='index').sort_values(roles,ascending=False).reset_index(drop='index')
    st.divider()
    st.header(f'Best {roles}')
    params = ['stopper','central defender','ball player','ball carrier','average rating']
    minvalues = data2.iloc[:,2:7].min().values.tolist()
    maxvalues = data2.iloc[:,2:7].max().values.tolist()
    col1, col2 = st.columns(2)
    with col1:
        create_pizza_plots(data2,[0,1],params,minvalues,maxvalues)
    with col2:
        create_pizza_plots(data2,[2,3],params,minvalues,maxvalues)
    
    col3,col4 = st.columns(2)
    with col3:
        create_pizza_plots(data2,[4,5],params,minvalues,maxvalues)
    with col4:
        create_pizza_plots(data2,[6,7],params,minvalues,maxvalues) 
if positions == 'Central Midfielders':
    roles = st.selectbox(label='Select Role',options = ['Regista_rating','Creative_playmaker_rating','Defensive_midfielder_rating','Box_to_box_rating','Central_midfielder_general_rating','avg_rating'])
    data = load_cms_data()
    data1 = st.dataframe(data.iloc[:,1:].drop_duplicates().reset_index(drop='index').sort_values(roles,ascending=False).reset_index(drop='index'))
    st.divider()
    col1,col2 = st.columns(2)

    with col1:
        st.header('Player Similarity Search')
        player=st.selectbox('Select player',options=data.name.unique().tolist())
    with col2:
        setup_and_find_similar_players(data,player,5)
        st.dataframe(simplayer)
    

