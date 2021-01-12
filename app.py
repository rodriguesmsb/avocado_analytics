#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri 08 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

###Import required libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pandas as pd
import numpy as np

###Add code to use external css
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]


###read and manipulate data
data = pd.read_csv("data/avocado.csv")

data["Date"] = pd.to_datetime(data["Date"], format = "%Y-%m-%d")

data.sort_values("Date", inplace = True)


###Create a instance of Dash class
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"

###Create a simple layout
app.layout = html.Div(

    #this part will contain the app body
    children = [

        #Create a div element to hold header
        html.Div(
            children = [
                html.P(children = "🥑", className="header-emoji"),
                html.H1(children="Avocado Analytics",
                className = "header-title"),
                html.P(
                children="Analyze the behavior of avocado prices"
                " and the number of avocados sold in the US"
                " between 2015 and 2018",
                className = "header-description"
                ),
            ],
            className = "header"
        ),

        #create a div element to hold menu
        html.Div(children = [

            #create dropdown menus
            html.Div(children = [
                html.Div(children="Region", className = "menu-title"),
                dcc.Dropdown(
                            id = "region-filter",
                            options = [
                                {"label": region, "value": region}
                                for region in np.sort(data.region.unique())
                            ],
                            value = "Albany",
                            clearable = False,
                            className = "dropdown",
                        ),

            ]),
            html.Div(children = [
                html.Div(children = "Type", className = "menu-title"),
                dcc.Dropdown(
                        id = "type-filter",
                        options = [
                            {"label": avocado_type, "value": avocado_type}
                            for avocado_type in data.type.unique()
                        ],
                        value="organic",
                        clearable = False,
                        searchable = False,
                        className = "dropdown",
                    ),

            ]),
            html.Div(children = [
                html.Div(children="Date Range",className="menu-title"),
                dcc.DatePickerRange(
                        id="date-range",
                        min_date_allowed=data.Date.min().date(),
                        max_date_allowed=data.Date.max().date(),
                        start_date=data.Date.min().date(),
                        end_date=data.Date.max().date(),
                    ),
                
            ]),
        ], className = "menu"),
    #create a div to hold graphs
    html.Div(children = [
        html.Div(
                children = dcc.Graph(
                    id = "price-chart", config = {"displayModeBar": False},),
                    className = "card",
                ),
        html.Div(
                children = dcc.Graph(
                    id = "volume-chart", config = {"displayModeBar": False},),
                    className = "card",
                )], className = "wrapper")
    ],  
)

#Add interactivity with callback functions

@app.callback(
    [Output("price-chart", "figure"), Output("volume-chart", "figure")],
    [
        Input("region-filter", "value"),
        Input("type-filter", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)
def update_charts(region, avocado_type, start_date, end_date):
    mask = (
        (data.region == region)
        & (data.type == avocado_type)
        & (data.Date >= start_date)
        & (data.Date <= end_date)
    )
    filtered_data = data.loc[mask, :]
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Average Price of Avocados",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "$", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    volume_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Total Volume"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": "Avocados Sold", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return price_chart_figure, volume_chart_figure




###Initialize app
if __name__ == "__main__":
    app.run_server(debug = True)