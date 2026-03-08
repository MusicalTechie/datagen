#!C:/Users/Administrator/AppData/Local/Programs/Python/Python310/python.exe

#---
#- plotly_display_matrix_to_webserver.py
#---
#- This version sends results directly back to the webserver
#- rather than to a file first.
#---

#NOTE: 
#      Not all of these are necessary in this script... but all could be 
#      important for some actions.  Here simply as a reminder of each 
#      plotly library.
#
import pandas as pd
import plotly.express as ppx
import plotly.graph_objects as pgo
import plotly.subplots as psp
import plotly.figure_factory as pff
import plotly.io as pio

# DISABLED
# Get the data from an HTTP source (presumes it will download and be used, must be in HTML area like "htdocs") 
# df = pd.read_csv('http://172.26.11.182/MATRIX_base.csv')

# ENABLED
# Get the data from a local path directly
df = pd.read_csv('C:/Apache/Apache24/cgi-bin/DataGen/data_results/base/MATRIX_base.csv')

# Create table object
v_graphic_object = pgo.Figure(data=[pgo.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Item,df.Location,df.Status,df.LifeCycle,df.TrendNPI,df.TrendCORE,df.TrendEOL,df.DateNPI,df.DateCORE,df.DateEOL,df.SafetyStockType,df.InitialSafetyStockValue],
               fill_color='lavender',
               align='left'))
])

# The "show" command will create a webserver of some kind and display the result
# Defaults to 127.0.0.1:80
# This command will NOT successfully return a content-type and HTML-ready data to Apache
# app.run_server(debug=False, host='0.0.0.0', port = 8080)
# v_graphic_object.show()

# Write the resulting object to a file
# v_graphic_object.write_html("C:/Apache/Apache24/htdocs/plotly_display_items.html")


#---
#- Print a "content header" to inform the webserver (Apache) that HTML-compliant content is coming
#---
print('Content-type: text/html\n')

#---
#- Convert the graphic to HTML format (does not include the content-type header) and stream it back to the webserver
#---
print( pio.to_html(v_graphic_object, config=None, auto_play=True, include_plotlyjs=True, include_mathjax=False, post_script=None, full_html=True, animation_opts=None, default_width='100%', default_height='100%', validate=True, div_id=None) )
