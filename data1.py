import pandas as pd
import plotly.express as px
#data = [10,20,30,40,50]
#df = pd.DataFrame(data)
#print(df)
df = pd.read_csv('csvfiles/data.csv')
fig = px.scatter(df,x="Population",y="Per capita",color="Country",size='Percentage')
fig.show()
