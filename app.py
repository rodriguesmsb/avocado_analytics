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
import pandas as pd 


###read and manipulate data
data = pd.read_csv("data/avocado.csv")

data = data.query("type == 'conventional' and region == 'Albany'")

data["Date"] = pd.to_datetime(data["Date"], format = "%Y-%m-%d")

data.sort_values("Date", inplace = True)


###Create a instance of Dash class
app = dash.Dash(__name__)


###Create a simple layout
app.layout = html.Div(
    children=[
        html.H1(children="Avocado Analytics",),
        html.P(
            children="Analyze the behavior of avocado prices"
            " and the number of avocados sold in the US"
            " between 2015 and 2018",
        ),
        #Create a graph for avocado price
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),

        #Create a graph for avocado sold
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)


###Initialize app
if __name__ == "__main__":
    app.run_server(debug=True)