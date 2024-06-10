import streamlit as st
import pandas as pd 
from data_vizzes import create_pizza_plots,filter_df_by_category
from splayers import similarcms,similarcbs,similarams,similarwing,similarstriker
from mplsoccer import PyPizza, add_image, FontManager
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist
st.set_page_config(layout="wide")

def load_cbs_data():
    path = 'central_defenders.csv'
    return pd.read_csv(path)
def load_allstats():
    path = 'AllPlayers.csv'
    return pd.read_csv(path)
def load_cms_data():
    path = 'central_midfielders.csv'
    return pd.read_csv(path)
def load_ams_data():
    path = 'attacking_midfielders.csv'
    return pd.read_csv(path)
def load_wing_data():
    path = 'Wingers.csv'
    return pd.read_csv(path)
def load_strikers_data():
    path = 'strikers.csv'
    return pd.read_csv(path)
def load_fringe_gk():
    path = 'Fringe_GK.csv'
    return pd.read_csv(path)
def load_fringe_cbs():
    path = 'fringe_cbs'
    return pd.read_csv(path)
def load_fringe_fbs():
    path = 'fringe_fbs'
    return pd.read_csv(path)

radio_box = st.radio(label='Select Version',options=['North/South Players 23/24','National League Fringe 23/24'])
if radio_box == 'North/South Players 23/24':
    positions = st.selectbox(label='Select position',options = ['Central Defenders','Central Midfielders','Wingers','Attacking Midfielders','Forwards'])
    if positions == 'Central Defenders':
        roles = st.selectbox(label='Select Role',options = ['stopper_rating','central_defender_rating','ball_playing_center_back_rating','ball_carrying_center_back_rating','avg_rating'])
    if positions == 'Central Defenders':
        data = load_cbs_data()
        data1 = st.dataframe(data.iloc[:,1:].drop_duplicates().reset_index(drop='index').sort_values(roles,ascending=False).reset_index(drop='index'))
        data2 = data.iloc[:,1:].drop_duplicates().reset_index(drop='index').sort_values(roles,ascending=False).reset_index(drop='index')
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            st.header('Player Similarity Search')
            player=st.selectbox('Select player',options=data2.name.unique().tolist())
        with col2:
            similar_players = similarcbs(data2,player,5)
            st.dataframe(data2[data2['name'].isin(similar_players.name.unique().tolist())].drop_duplicates().reset_index(drop='index'))
    
           
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
            similar_players = similarcms(data,player,5)
            
            st.dataframe(data[data['name'].isin(similar_players.name.unique().tolist())].iloc[:,1:].reset_index(drop='index'))
    
        
    if positions == 'Attacking Midfielders':
        roles = st.selectbox(label = 'Select Role', options = ['Number_10_rating','Creator_rating','Shadow_Striker_rating','avg_rating'])
        data = load_ams_data()
        data1 = st.dataframe(data.iloc[:,1:].drop_duplicates().reset_index(drop='index').sort_values(roles,ascending=False).reset_index(drop='index'))
        st.divider()
        col1,col2 = st.columns(2)
    
        with col1:
            st.header('Player Similarity Search')
            player=st.selectbox('Select player',options=data.name.unique().tolist())
        with col2:
            similar_players = similarams(data,player,3)
            
            st.dataframe(data[data['name'].isin(similar_players.name.unique().tolist())].iloc[:,1:].reset_index(drop='index'))
    
    if positions == 'Wingers':
        roles = st.selectbox(label = 'Select Role', options = ['winger', 'dribbling_winger', 'inside_fwd', 'space_inv','avg_rating'])
        data = load_wing_data()
        data1 = st.dataframe(data.iloc[:,1:].drop_duplicates().reset_index(drop='index').sort_values(roles,ascending=False).reset_index(drop='index'))
        st.divider()
        col1,col2 = st.columns(2)
    
        with col1:
            st.header('Player Similarity Search')
            player=st.selectbox('Select player',options=data.name.unique().tolist())
        with col2:
            similar_players = similarwing(data,player,3)
            
            st.dataframe(data[data['name'].isin(similar_players.name.unique().tolist())].iloc[:,1:].reset_index(drop='index'))
    if positions == 'Forwards':
        roles = st.selectbox(label = 'Select Role', options = ['center_forward','deep_lying_forward','pressing_forward','target_man','poacher','avg_rating'])
        data = load_strikers_data()
        data1 = st.dataframe(data.iloc[:,1:].drop_duplicates().reset_index(drop='index').sort_values(roles,ascending=False).reset_index(drop='index'))
        st.divider()
        col1,col2 = st.columns(2)
    
        with col1:
            st.header('Player Similarity Search')
            player=st.selectbox('Select player',options=data.name.unique().tolist())
        with col2:
            similar_players = similarstriker(data,player,4)
            
            st.dataframe(data[data['name'].isin(similar_players.name.unique().tolist())].iloc[:,1:].reset_index(drop='index'))
    
        
    st.divider()
    st.header('Player statistics vs Position average')
    pos = st.selectbox('Select Player Position',options = ['Central Defender','Central Midfielder','Attacking Midfielder','Winger','Striker'])
    if pos == 'Central Midfielder':
        data1 = load_cms_data()
        data2 = load_allstats()
        data2 = data2[(data2['name'].isin(data1.name.to_list()) & (data2['current_team_name'].isin(data1.current_team_name.to_list())))]
        player1 = st.selectbox('Select Player',options=sorted(data2.name.tolist()))
        met = st.selectbox('Select statistic group',options=['Defensive','Attacking','Passes','Key Passes'])
        col1,col2,col3 = st.columns(3)
        with col2:
            if met == 'Defensive':
                filtered_data = filter_df_by_category(data2,'defensive')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'defensive').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Attacking':
                filtered_data = filter_df_by_category(data2,'attacking')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'attacking').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Passes':
                filtered_data = filter_df_by_category(data2,'passing')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'passing').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Key Passes':
                filtered_data = filter_df_by_category(data2,'key passing')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'key passing').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))       
    if pos == 'Central Defender':
        data1 = load_cbs_data()
        data2 = load_allstats()
        data2 = data2[(data2['name'].isin(data1.name.to_list()) & (data2['current_team_name'].isin(data1.current_team_name.to_list())))]
        player1 = st.selectbox('Select Player',options=sorted(data2.name.tolist()))
        met = st.selectbox('Select statistic group',options=['Defensive','Attacking','Passes','Key Passes'])
        col1,col2,col3 = st.columns(3)
        with col2:
            if met == 'Defensive':
                filtered_data = filter_df_by_category(data2,'defensive')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'defensive').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Attacking':
                filtered_data = filter_df_by_category(data2,'attacking')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'attacking').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Passes':
                filtered_data = filter_df_by_category(data2,'passing')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'passing').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Key Passes':
                filtered_data = filter_df_by_category(data2,'key passing')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'key passing').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))       
    
    if pos == 'Attacking Midfielder':
        data1 = load_ams_data()
        data2 = load_allstats()
        data2 = data2[(data2['name'].isin(data1.name.to_list()) & (data2['current_team_name'].isin(data1.current_team_name.to_list())))]
        player1 = st.selectbox('Select Player',options=sorted(data2.name.tolist()))
        met = st.selectbox('Select statistic group',options=['Defensive','Attacking','Passes','Key Passes'])
        col1,col2,col3 = st.columns(3)
        with col2:
            if met == 'Defensive':
                filtered_data = filter_df_by_category(data2,'defensive')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'defensive').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Attacking':
                filtered_data = filter_df_by_category(data2,'attacking')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'attacking').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Passes':
                filtered_data = filter_df_by_category(data2,'passing')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'passing').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Key Passes':
                filtered_data = filter_df_by_category(data2,'key passing')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'key passing').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))       
    if pos == 'Winger':
        data1 = load_wing_data()
        data2 = load_allstats()
        data2 = data2[(data2['name'].isin(data1.name.to_list()) & (data2['current_team_name'].isin(data1.current_team_name.to_list())))]
        player1 = st.selectbox('Select Player',options=sorted(data2.name.tolist()))
        met = st.selectbox('Select statistic group',options=['Defensive','Attacking','Passes','Key Passes'])
        col1,col2,col3 = st.columns(3)
        with col2:
            if met == 'Defensive':
                filtered_data = filter_df_by_category(data2,'defensive')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'defensive').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Attacking':
                filtered_data = filter_df_by_category(data2,'attacking')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'attacking').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Passes':
                filtered_data = filter_df_by_category(data2,'passing')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'passing').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Key Passes':
                filtered_data = filter_df_by_category(data2,'key passing')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'key passing').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))      
    if pos == 'Striker':
        data1 = load_strikers_data()
        data2 = load_allstats()
        data2 = data2[(data2['name'].isin(data1.name.to_list()) & (data2['current_team_name'].isin(data1.current_team_name.to_list())))]
        player1 = st.selectbox('Select Player',options=sorted(data2.name.tolist()))
        met = st.selectbox('Select statistic group',options=['Defensive','Attacking','Passes','Key Passes'])
        col1,col2,col3 = st.columns(3)
        with col2:
            if met == 'Defensive':
                filtered_data = filter_df_by_category(data2,'defensive')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'defensive').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Attacking':
                filtered_data = filter_df_by_category(data2,'attacking')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'attacking').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Passes':
                filtered_data = filter_df_by_category(data2,'passing')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'passing').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))
        with col2:
            if met == 'Key Passes':
                filtered_data = filter_df_by_category(data2,'key passing')
                filtered_data1 = filter_df_by_category(data2[data2['name']==player1],'key passing').reset_index(drop='index')
                filtered_data2 = pd.DataFrame(filtered_data1.loc[0])
                filtered_mean = filtered_data.mean().reset_index()[0].to_list()
                player_data = filtered_data2.round(2)
                player_data['League average'] = filtered_mean
                st.write(player_data.rename(columns={0:'Player Stats'}).round(2))  
if radio_box == 'National League Fringe 23/24':
    st.title('Goalkeepers')
    gks = load_fringe_gk()
    st.write(gks.iloc[:,1:])
    st.title('Center Backs')
    cbs = load_fringe_cbs()
    st.write(cbs.iloc[:,1:])
    st.title('Full/Wing Backs')
    fbs = load_fringe_fbs()
    st.write(fbs.iloc[:,1:])
    st.title('Midfielders')
    

