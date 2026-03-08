#!C:\Users\Administrator\AppData\Local\Programs\Python\Python310\python.exe

import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('http://172.26.11.182/ITEMS_base.csv')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Business,df.Brand,df.Product_Family,df.Item,df.DemandType],
               fill_color='lavender',
               align='left'))
])

#fig.show()

fig.write_html("C:/Apache/Apache24/htdocs/plotly_display_items.html")


