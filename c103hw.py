import pandas as pd

import plotly.express as px

df = pd.read_csv("Copy+of+data+-+data (1).csv")
print(df)

fig=px.scatter(df,x='date', y='cases',color='country',size_max=60)
fig.show()