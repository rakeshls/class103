import pandas as pd
import plotly.express as px
#data = [10,20,30,40,50]
#df = pd.DataFrame(data)
#print(df)
df = pd.read_csv('csvfiles/line_chart.csv')
fig = px.line(df,x="Year",y="Per capita income",color="Country",title="Per capita income")
fig.show()
