import pandas as pd 
import plotly.express as px 
df = pd.read_csv("covid.csv") 
fig = px.scatter(df, x="Date", y='Cases', color="Country", size_max=60) 
fig.show()