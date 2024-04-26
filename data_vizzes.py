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
