## home_page.py
from dash import Dash
from dash import html
from dash import dcc
from dash import Input
from dash import Output
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets= [dbc.themes.BOOTSTRAP])

app.layout= dbc.Alert(
    "Hello,", className="m-5"
)

if __name__ == '__main__' :
    app.run_server(debug = True)

