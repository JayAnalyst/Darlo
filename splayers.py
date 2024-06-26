import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist

def similarcms(df, player_name, num_players=5):
    # Load and clean the data

    df_clean = df.drop_duplicates().reset_index(drop=True)
    
    # Focus on the rating columns for similarity
    rating_columns = ['Regista_rating', 'Creative_playmaker_rating', 'Defensive_midfielder_rating',
                      'Box_to_box_rating', 'Central_midfielder_general_rating', 'avg_rating']
    
    # Standardizing the rating columns
    scaler = StandardScaler()
    df_clean[rating_columns] = scaler.fit_transform(df_clean[rating_columns])
    
    # Compute the pairwise Euclidean distances between players
    distance_matrix = cdist(df_clean[rating_columns], df_clean[rating_columns], metric='euclidean')
    
    # Convert the distance matrix into a DataFrame for easier manipulation
    distance_df = pd.DataFrame(distance_matrix, index=df_clean['name'], columns=df_clean['name'])
    
    # Find similar players function
    if player_name not in distance_df.index:
        return "Player not found. Please check the name and try again."
    
    player_distances = distance_df[player_name].sort_values()
    similar_players = player_distances.iloc[1:num_players+1].index.tolist()
    
    simplayer = df_clean[df_clean['name'].isin(similar_players)].reset_index(drop='index')
    return simplayer


def similarcbs(df, player_name, num_players=5):
    # Load and clean the data

    df_clean = df.drop_duplicates().reset_index(drop=True)
    
    # Focus on the rating columns for similarity
    rating_columns = ['stopper_rating','central_defender_rating','ball_playing_center_back_rating','ball_carrying_center_back_rating','avg_rating']
    
    # Standardizing the rating columns
    scaler = StandardScaler()
    df_clean[rating_columns] = scaler.fit_transform(df_clean[rating_columns])
    
    # Compute the pairwise Euclidean distances between players
    distance_matrix = cdist(df_clean[rating_columns], df_clean[rating_columns], metric='euclidean')
    
    # Convert the distance matrix into a DataFrame for easier manipulation
    distance_df = pd.DataFrame(distance_matrix, index=df_clean['name'], columns=df_clean['name'])
    
    # Find similar players function
    if player_name not in distance_df.index:
        return f"Player not found. Please check the name '{player_name}' and try again."
    
    try:
        # Get the sorted distances and extract similar players
        player_distances = distance_df[player_name].sort_values()
        similar_players = player_distances.iloc[1:num_players+1].index.tolist()
        
        # Check if similar players are found and return results
        if similar_players:
            simplayer = df_clean[df_clean['name'].isin(similar_players)].reset_index(drop=True)
            return simplayer
        else:
            return "No similar players."
    except Exception as e:
        return f"An error occurred while finding similar players: {e}"


def similarams(df, player_name, num_players=3):
    # Load and clean the data

    df_clean = df.drop_duplicates().reset_index(drop=True)
    
    # Focus on the rating columns for similarity
    rating_columns = ['Number_10_rating','Creator_rating','Shadow_Striker_rating','avg_rating']
    
    # Standardizing the rating columns
    scaler = StandardScaler()
    df_clean[rating_columns] = scaler.fit_transform(df_clean[rating_columns])
    
    # Compute the pairwise Euclidean distances between players
    distance_matrix = cdist(df_clean[rating_columns], df_clean[rating_columns], metric='euclidean')
    
    # Convert the distance matrix into a DataFrame for easier manipulation
    distance_df = pd.DataFrame(distance_matrix, index=df_clean['name'], columns=df_clean['name'])
    
    # Find similar players function
    if player_name not in distance_df.index:
        return f"Player not found. Please check the name '{player_name}' and try again."
    
    try:
        # Get the sorted distances and extract similar players
        player_distances = distance_df[player_name].sort_values()
        similar_players = player_distances.iloc[1:num_players+1].index.tolist()
        
        # Check if similar players are found and return results
        if similar_players:
            simplayer = df_clean[df_clean['name'].isin(similar_players)].reset_index(drop=True)
            return simplayer
        else:
            return "No similar players."
    except Exception as e:
        return f"An error occurred while finding similar players: {e}"

def similarwing(df, player_name, num_players=3):
    # Load and clean the data

    df_clean = df.drop_duplicates().reset_index(drop=True)
    
    # Focus on the rating columns for similarity
    rating_columns = ['winger', 'dribbling_winger', 'inside_fwd', 'space_inv','avg_rating']
    
    # Standardizing the rating columns
    scaler = StandardScaler()
    df_clean[rating_columns] = scaler.fit_transform(df_clean[rating_columns])
    
    # Compute the pairwise Euclidean distances between players
    distance_matrix = cdist(df_clean[rating_columns], df_clean[rating_columns], metric='euclidean')
    
    # Convert the distance matrix into a DataFrame for easier manipulation
    distance_df = pd.DataFrame(distance_matrix, index=df_clean['name'], columns=df_clean['name'])
    
    # Find similar players function
    if player_name not in distance_df.index:
        return f"Player not found. Please check the name '{player_name}' and try again."
    
    try:
        # Get the sorted distances and extract similar players
        player_distances = distance_df[player_name].sort_values()
        similar_players = player_distances.iloc[1:num_players+1].index.tolist()
        
        # Check if similar players are found and return results
        if similar_players:
            simplayer = df_clean[df_clean['name'].isin(similar_players)].reset_index(drop=True)
            return simplayer
        else:
            return "No similar players."
    except Exception as e:
        return f"An error occurred while finding similar players: {e}"
    
def similarstriker(df, player_name, num_players=4):
    # Load and clean the data

    df_clean = df.drop_duplicates().reset_index(drop=True)
    
    # Focus on the rating columns for similarity
    rating_columns = ['center_forward','deep_lying_forward','pressing_forward','target_man','poacher','avg_rating']
    
    # Standardizing the rating columns
    scaler = StandardScaler()
    df_clean[rating_columns] = scaler.fit_transform(df_clean[rating_columns])
    
    # Compute the pairwise Euclidean distances between players
    distance_matrix = cdist(df_clean[rating_columns], df_clean[rating_columns], metric='euclidean')
    
    # Convert the distance matrix into a DataFrame for easier manipulation
    distance_df = pd.DataFrame(distance_matrix, index=df_clean['name'], columns=df_clean['name'])
    
    # Find similar players function
    if player_name not in distance_df.index:
        return f"Player not found. Please check the name '{player_name}' and try again."
    
    try:
        # Get the sorted distances and extract similar players
        player_distances = distance_df[player_name].sort_values()
        similar_players = player_distances.iloc[1:num_players+1].index.tolist()
        
        # Check if similar players are found and return results
        if similar_players:
            simplayer = df_clean[df_clean['name'].isin(similar_players)].reset_index(drop=True)
            return simplayer
        else:
            return "No similar players."
    except Exception as e:
        return f"An error occurred while finding similar players: {e}"





    