import streamlit as st
import pandas as pd 

def load_data():
    path = 'Positions\Goalkeepers.csv'
    return pd.read_csv(path)

data = load_data()

print(data)