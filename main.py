import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink('About', href='#')),
        dbc.NavItem(dbc.NavLink('Products', href='#')),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem('More pages', header=True),
                dbc.DropdownMenuItem('Page 2', href='#'),
                dbc.DropdownMenuItem('Page 3', href='#'),
            ],
            nav=True,
            in_navbar=True,
            label='More',
        ),
    ],
    brand='Bootstrap NavBar',
    brand_href='#',
    color='#0099f9',
    dark=True,
)

jumbotron = dbc.Jumbotron([
    html.H1('Welcome', className='display-3'),
    html.P('This is a sample jumbotron', className='lead'),
    html.Hr(className='my-2'),
    html.P('Additional dummy text'),
    html.P(dbc.Button('Learn more', color='primary'), className='lead'),
])

app.layout = html.Div([
    navbar,
    jumbotron
])

if __name__ == '__main__':
    app.run_server(debug=True)