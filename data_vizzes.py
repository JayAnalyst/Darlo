import pandas as pd
from mplsoccer import PyPizza, add_image, FontManager
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt 
import streamlit as st
def create_pizza_plots(data, indices, params, minvalues, maxvalues):
    # Load fonts if needed
    font_normal = FontProperties(family='sans-serif', style='normal', size=12)
    font_bold = FontProperties(family='sans-serif', weight='bold', size=14)

    # Prepare data list and parameters
    values_list = [data.iloc[idx, 2:7].values.tolist() for idx in indices]
    baker = PyPizza(
        params=params,
        min_range=minvalues,  # min range values
        max_range=maxvalues,  # max range values
        background_color="#ffffff", straight_line_color="#000000",
        last_circle_color="#000000", last_circle_lw=2.5, straight_line_lw=1,
        other_circle_lw=0, other_circle_color="#000000", inner_circle_size=20,
    )

    for i, values in enumerate(values_list):
        # plot pizza
        fig, ax1 = baker.make_pizza(
            values,  # list of values
            figsize=(12, 6),  # adjust figsize according to your need
            color_blank_space="same",  # use same color to fill blank space
            blank_alpha=0.4,  # alpha for blank-space colors
            param_location=110,  # where the parameters will be added
            kwargs_slices=dict(
                facecolor="#1A78CF", edgecolor="#000000",
                zorder=1, linewidth=1
            ),  # values to be used when plotting slices
            kwargs_params=dict(
                color="k", fontsize=8, zorder=5,
                fontproperties=font_normal, va="center"
            ),  # values to be used when adding parameter
            kwargs_values=dict(
                color="k", fontsize=8,
                fontproperties=font_normal, zorder=3,
                bbox=dict(
                    edgecolor="#000000", facecolor="#1A78CF",
                    boxstyle="round,pad=0.3", lw=1
                )
            )  # values to be used when adding parameter-values
        )

        # Turn off the axes

        # Add a title and subtitle
        fig.text(0.5, 0.95, f"{data['name'][idx]} - {data['current_team_name'][idx]}", size=12, ha="center", color="k")
        #fig.text(0.0, 0.90, f"Minutes played - {data['total_matches'][i]}", size=30, ha="center", fontproperties=font_bold, color="lightgrey")
        #fig.text(0.0, 0.85, f"Z Score = {round(data['z_score'][i], 2)}", size=30, ha='center', fontproperties=font_bold, color='lightgrey')
        
        # Show the plot
        st.pyplot(fig)

# Example usage:
# create_pizza_plots(data, [0, 1, 2, 3, 4], params, minvalues, maxvalues)
