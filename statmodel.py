import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import statsmodels.api as sm
import pandas as pd

data = pd.DataFrame(sm.datasets.get_rdataset('mtcars', 'datasets', cache=True).data)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Label('Plot title:'),
    dcc.Input(id='input-title', value='MTCars visualization', type='text'),
    html.Br(),
    html.Label('X-axis:'),
    dcc.Dropdown(
        id='dropdown-x',
        options=[{'label': col, 'value': col} for col in data.columns],
        value='mpg'
    ),
    html.Br(),
    html.Label('Y-axis:'),
    dcc.Dropdown(
        id='dropdown-y',
        options=[{'label': col, 'value': col} for col in data.columns],
        value='mpg'
    ),
    html.Br(),
    html.Div(
        dcc.Graph(id='chart')
    )
], style={'padding': '30px'})


@app.callback(
    Output('chart', 'figure'),
    Input('input-title', 'value'),
    Input('dropdown-x', 'value'),
    Input('dropdown-y', 'value'))

def update_output(title, x_axis, y_axis):
    fig = px.scatter(data, x=x_axis, y=y_axis, title=title)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)