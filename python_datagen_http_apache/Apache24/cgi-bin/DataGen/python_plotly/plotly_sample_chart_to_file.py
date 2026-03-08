#!C:\Users\Administrator\AppData\Local\Programs\Python\Python310\python.exe

#---
#- plotly_sample_chart.py
#---

import pandas as pd
import plotly.express as px

dfb = pd.read_csv("bird-window-collision-death.csv")

df = px.data.tips()

#app.run_server(debug=False, host='0.0.0.0', port = 8080)

fig = px.pie(dfb, values='Deaths', names='Bldg #', color="Side", hole=0.3)
fig.update_traces(textinfo="label+percent", insidetextfont=dict(color="white"))
fig.update_layout(legend={"itemclick":False})

#This command will NOT successfully return a content-type and HTML-ready data to Apache
#fig.write_image("plotly_sample_chart.png")

#This is a useful temporary test command to write the graph or chart into a standalone HTML file.
fig.write_html("C:/Apache/Apache24/htdocs/plotly_sample_chart.html")

#Send a result back as pure HTML content
#This command will NOT successfully return a content-type and HTML-ready data to Apache
#plotly.io.to_html(fig, config=None, auto_play=True, full_html=True)
px.to_html(fig, config=None, auto_play=True, full_html=True)

# Will create a webserver of some kind and display the result
# Defaults to 127.0.0.1:80
# This command will NOT successfully return a content-type and HTML-ready data to Apache
# fig.show()



