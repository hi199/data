import pandas as pd
import plotly.express as px
df=pd.read_csv("covid.csv")
fig=px.bar(df,x='Date',y='NumberOfCases')
fig.show()