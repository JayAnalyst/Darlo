import pandas as pd
from mplsoccer import PyPizza, add_image, FontManager
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt 
import streamlit as st
def create_pizza_plots(data, indices, params, minvalues, maxvalues):
    # Load fonts if needed
    font_normal = FontProperties(family='sans-serif', style='normal', size=12)
    font_bold = FontProperties(family='sans-serif', weight='bold', size=14)

    # Loop over indices and create a pizza plot for each
    for i in indices:
        # Prepare data for the current index
        values = data.iloc[i, 2:7].values.tolist()
        
        # Create new figure and axis for each plot
        fig, ax1 = plt.subplots(figsize=(12, 6))
        
        # Create a pizza plot baker
        baker = PyPizza(
            params=params,
            min_range=minvalues,  # min range values
            max_range=maxvalues,  # max range values
            background_color="#ffffff", straight_line_color="#000000",
            last_circle_color="#000000", last_circle_lw=2.5, straight_line_lw=1,
            other_circle_lw=0, other_circle_color="#000000", inner_circle_size=20,
        )

        # plot pizza
        fig, ax = baker.make_pizza(
            values,  # Use the new axis
            color_blank_space="same",  # use same color to fill blank space
            blank_alpha=0.4,  # alpha for blank-space colors
            param_location=110,  # where the parameters will be added
            kwargs_slices=dict(
                facecolor="#1A78CF", edgecolor="#000000",
                zorder=1, linewidth=1
            ),  # values to be used when plotting slices
            kwargs_params=dict(
                color="k", fontsize=12, zorder=5,
                fontproperties=font_normal, va="center"
            ),  # values to be used when adding parameter
            kwargs_values=dict(
                color="k", fontsize=12,
                fontproperties=font_normal, zorder=3,
                bbox=dict(
                    edgecolor="#000000", facecolor="#1A78CF",
                    boxstyle="round,pad=0.3", lw=1
                )
            )  # values to be used when adding parameter-values
        )

        # Add a title and subtitle
        fig.text(0.5, 0.95, f"{data['name'][i]} - {data['current_team_name'][i]}", size=20, ha="center", color="k")
        
        # Show the plot with Streamlit
        st.pyplot(fig)


    # Example usage:
    # create_pizza_plots(data, [0, 1, 2, 3, 4], params, minvalues, maxvalues)



import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist

def setup_and_find_similar_players(df, player_name, num_players=5):
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
    

# Example usage:
# similar_players = setup_and_find_similar_players('path_to_csv_file.csv', 'D. Weeks')
# print(similar_players)


def filter_df_by_category(df, category):
    defensive_columns = [
        'successful_defensive_actions_avg', 'defensive_duels_avg', 'defensive_duels_won', 'aerial_duels_avg', 
        'aerial_duels_won', 'tackle_avg', 'possession_adjusted_tackle', 'shot_block_avg', 'interceptions_avg', 
        'possession_adjusted_interceptions', 'fouls_avg', 'yellow_cards', 'yellow_cards_avg', 'red_cards', 
        'red_cards_avg'
    ]

    attacking_columns = [
        'successful_attacking_actions_avg', 'goals', 'goals_avg', 'non_penalty_goal', 'non_penalty_goal_avg', 
        'xg_shot', 'xg_shot_avg', 'head_goals', 'head_goals_avg', 'shots', 'shots_avg', 'shots_on_target_percent', 
        'goal_conversion_percent', 'assists', 'assists_avg', 'xg_assist', 'xg_assist_avg', 'crosses_avg', 
        'accurate_crosses_percent', 'dribbles_avg', 'successful_dribbles_percent', 'offensive_duels_avg', 
        'offensive_duels_won', 'touch_in_box_avg', 'progressive_run_avg'
    ]

    passing_columns = [
        'passes_avg', 'accurate_passes_percent', 'forward_passes_avg', 'successful_forward_passes_percent', 
        'back_passes_avg', 'successful_back_passes_percent', 'vertical_passes_avg', 
        'successful_vertical_passes_percent', 'long_passes_avg', 'successful_long_passes_percent', 
        'average_pass_length', 'average_long_pass_length'
    ]

    key_passing_columns = [
        'assists', 'assists_avg', 'xg_assist', 'xg_assist_avg', 'pre_assist_avg', 'pre_pre_assist_avg', 
        'smart_passes_avg', 'accurate_smart_passes_percent', 'key_passes_avg', 'passes_to_final_third_avg', 
        'accurate_passes_to_final_third_percent', 'pass_to_penalty_area_avg', 
        'accurate_pass_to_penalty_area_percent', 'through_passes_avg', 'successful_through_passes_percent', 
        'deep_completed_pass_avg', 'deep_completed_cross_avg', 'progressive_pass_avg', 
        'successful_progressive_pass_percent'
    ]

    columns_dict = {
        'defensive': defensive_columns,
        'attacking': attacking_columns,
        'passing': passing_columns,
        'key passing': key_passing_columns
    }
    
    if category not in columns_dict:
        raise ValueError("Invalid category. Choose from 'defensive', 'attacking', 'passing', or 'key passing'.")
    
    # Get the list of relevant columns for the given category
    relevant_columns = columns_dict[category]
    
    # Filter the DataFrame to retain only the relevant columns
    return df[relevant_columns]

# Example usage:
# Assume `original_df` is your existing DataFrame
# filtered_df = filter_df_by_category(original_df, 'defensive')
# print(filtered_df)
