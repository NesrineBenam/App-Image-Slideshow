## home_page.py
from dash import Dash
from dash import html
from dash import dcc
from dash import Input
from dash import Output
from dash import State
import dash_bootstrap_components as dbc

# Set App Style from built-in themes
app = Dash(__name__, external_stylesheets= [dbc.themes.QUARTZ])

# Navigation Bar Components
search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search", className="bg-light text-dark")), # Text Input
        dbc.Col( dbc.Button("Search", color= "primary", n_clicks= 0 ),width="auto"),
    ],
    className="g-1 ms-auto flex-nowrap mt-3 mt-md-0",
    align="right",
)

nav_brand = dbc.NavbarBrand("Family Album",className="fw-bold" )

nav_link = dbc.NavLink("GitHub", href="#")

dropdown = dbc.DropdownMenu(
    children= [
        dbc.DropdownMenuItem("Home", id = "home-dropdown", href="#"),
        dbc.DropdownMenuItem("Picture Label", id = "picture-label-dropdown", n_clicks=0 ),
    ],
    nav= True,
    in_navbar= True,
    label= "Menu",
    size = 'md',
)

logo = "https://i.pinimg.com/originals/3e/e9/12/3ee912433ff51be233eb9117400da303.png"

# Build Navigation bar layout
navbar = dbc.Navbar(
    dbc.Container( # html.div
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src= logo, height="50px")),
                    dbc.Col(nav_brand),
                    dbc.Col(dropdown),
                    dbc.Col(nav_link),
                ],
                align="center",
            ),
            dbc.Collapse(
                search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            )
     ]
    ),
    color= "dark", # "Dark" bar
    dark= True, # Contrast Text,

)
def make_album_card(footer_name):
    """ Returns a Card with """
    card = [dbc.CardImg(src="https://media.timeout.com/images/105976422/1024/576/image.jpg", className="img-fluid"),
            dbc.CardBody(
             html.P("Hashtags # ", )
            ),
        dbc.CardFooter(footer_name),
    ]
    return card


home_page_body = html.Div([
        dbc.Row(
            [
                dbc.Col(dbc.Card(make_album_card(2023), color="secondary", inverse=True, className="p-1")),
                dbc.Col(dbc.Card(make_album_card(2022), color="secondary", inverse=True, className="p-1")),
                dbc.Col(dbc.Card(make_album_card(2021), color="secondary", inverse=True, className="p-1")),

            ],
            className="mb-4"
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(make_album_card(2020), color="secondary", inverse=True, className="p-1")),
                dbc.Col(dbc.Card(make_album_card(2019), color="secondary", inverse=True, className="p-1")),
                dbc.Col(dbc.Card(make_album_card(2018), color="secondary", inverse=True, className="p-1")),

            ],
            className="mb-4"
        ),
    ],
    className="p-2 "
)

###### Build App Layout
app.layout = html.Div(
    [navbar, home_page_body]
)


# Run App
if __name__ == '__main__' :
    app.run_server(debug = True)

