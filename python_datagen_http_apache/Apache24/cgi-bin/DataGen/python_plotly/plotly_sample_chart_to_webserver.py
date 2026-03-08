#!C:\Users\Administrator\AppData\Local\Programs\Python\Python310\python.exe

#---
#- plotly_sample_chart.py
#---
#- This version sends results directly back to the webserver
#- rather than to a file first.
#---

#NOTE: 
#      Not all of these are necessary in this script... but all could be 
#      important for some actions.  Here simply as a reminder of each 
#      plotly library.
#
import pandas as ppd
import plotly.express as ppx
import plotly.graph_objects as pgo
import plotly.subplots as psp
import plotly.figure_factory as pff
import plotly.io as pio

# Get the data 
dfb = ppd.read_csv("bird-window-collision-death.csv")

# Populate the mouseover tips
df = ppx.data.tips()

# Build the chart
v_graphic_object = ppx.pie(dfb, values='Deaths', names='Bldg #', color="Side", hole=0.3)
v_graphic_object.update_traces(textinfo="label+percent", insidetextfont=dict(color="white"))
v_graphic_object.update_layout(legend={"itemclick":False})

# The "show" command will create a webserver of some kind and display the result
# Defaults to 127.0.0.1:80
# This command will NOT successfully return a content-type and HTML-ready data to Apache
# app.run_server(debug=False, host='0.0.0.0', port = 8080)
# v_graphic_object.show()

# This command will NOT successfully return a content-type and HTML-ready data to Apache
# It will create an image file however.
# v_graphic_object.write_image("plotly_sample_chart.png")

# This is a useful temporary test command to write the graph or chart into a standalone HTML file.
# v_graphic_object.write_html("C:/Apache/Apache24/htdocs/plotly_sample_chart.html")


#---
#- Print a "content header" to inform the webserver (Apache) that HTML-compliant content is coming
#---
print('Content-type: text/html\n')

#---
#- Convert the graphic to HTML format (does not include the content-type header) and stream it back to the webserver
#---
print( pio.to_html(v_graphic_object, config=None, auto_play=True, include_plotlyjs=True, include_mathjax=False, post_script=None, full_html=True, animation_opts=None, default_width='100%', default_height='100%', validate=True, div_id=None) )





