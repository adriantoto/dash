# input stock graph

#Libraries
import dash
from dash.dependencies import  Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
from datetime import datetime

#Define the start and end
start = datetime(2018, 1, 1)
end = datetime.now()

#Define the first chosen/default stock
stock = 'TSLA'

#Declare the dataframe variable 
df = web.DataReader(stock, 'iex', start, end)

#Run the dash
app = dash.Dash()

#The dash layout
app.layout = html.Div(children = [

    html.Div(children='''
        symbol to graph:
    '''),

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')

    ])

#Callback function
@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
    )

#declare the update_graph function
def update_graph(input_data):
    start = datetime(2018, 1, 1)
    end = datetime.now()
    df = web.DataReader(input_data, 'iex', start, end)
    return dcc.Graph(id='example-graph',
              figure={
                  'data': [{'x': df.index, 'y': df.close, "type": 'line', 'name': input_data},
                           ],
                  'layout': {
                      'title': input_data
                  }
              })
