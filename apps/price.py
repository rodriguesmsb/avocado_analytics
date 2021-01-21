import dash_core_components as dcc  
import dash_html_components as html
from components import nav_bar
from components.aux_func import encode_image
import pandas as pd
import numpy as np


###Read data that will be use
data = pd.read_csv("data/avocado.csv")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)
path_to_image = "assets/heart.png"
path_to_avocado = "assets/favicon.ico"


layout = html.Div(
    id = "main_body",
    children = [
        #Create a div element to hold header
        html.Div(id = "header",
            children = [
                html.P(children = html.Img(src = encode_image(path_to_avocado)), className = "emoji"),
                html.H1(children = "Avocado Analytics",
                className = "header-title"),
                html.P(
                children = "A web page dedicated to analyze"
                " the behavior of avocado prices in US"
                " between 2015 and 2018",
                className = "description"
                ),
                    
        ],
        className = "header"
    ),
        #Add a div with navbar over here
        nav_bar.navBar,

        #Add menu selector
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Region", className="menu-title"),
                        dcc.Dropdown(
                            id="region-filter",
                            options=[
                                {"label": region, "value": region}
                                for region in np.sort(data.region.unique())
                            ],
                            value="Albany",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children = "Type", className = "menu-title"),
                        dcc.Dropdown(
                            id="type-filter",
                            options=[
                                {"label": avocado_type, "value": avocado_type}
                                for avocado_type in data.type.unique()
                            ],
                            value = "organic",
                            clearable = False,
                            searchable = False,
                            className="dropdown",
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                            ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.Date.min().date(),
                            max_date_allowed=data.Date.max().date(),
                            start_date=data.Date.min().date(),
                            end_date=data.Date.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),

        #Add graph here
        html.Div(
            children = [
                dcc.Graph(
                    id = "price-chart",
                    config = {"displayModeBar": False},
                )

            ],
            className = "card"
        ),

        html.Div(id = "footer_body",
                children = [
                    html.Img(src = encode_image(path_to_image)),
                    html.P("Because we all love AVOCADOS!", className = "description_footer")
                            
            
    ],
        className = "footer"),
    ],
)
