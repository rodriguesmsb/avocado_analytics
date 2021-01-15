import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app
from apps import home

###Add code to use external css
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]


###Create a instance of Dash class
app = dash.Dash(__name__, external_stylesheets = [external_stylesheets])
app.title = "Avocado Analytics: Understand Your Avocados!"

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/apps/home":
        return home.layout
    else:
        return home.layout


@app.callback(Output('image', 'children'),
              [Input('interval', 'n_intervals')])
def display_image(n):
    if n == None or n % 3 == 1:
        img = html.Img(src="http://placeimg.com/625/225/any")
    elif n % 3 == 2:
        img = html.Img(src="http://placeimg.com/625/225/animals")
    elif n % 3 == 0:
        img = html.Img(src="http://placeimg.com/625/225/arch")
    else:
        img = "None"
    return img


if __name__ == '__main__':
    app.run_server(debug = True)
