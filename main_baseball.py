import streamlit as st
# import pandas as pd
from pybaseball import playerid_lookup, statcast_pitcher

st.title("PyBaseball_streamlit")

df = playerid_lookup('ohtani', 'shohei')

ohtani_stats = statcast_pitcher('2023-03-01', '2023-10-01', 660271)
ohtani_stats = ohtani_stats.groupby("pitch_type").release_speed.agg("max")

st.dataframe(ohtani_stats)

st.bar_chart(ohtani_stats)
