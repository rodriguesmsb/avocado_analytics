import dash_core_components as dcc  
import dash_html_components as html

from components import nav_bar
from components.aux_func import encode_image

path_to_heart = "assets/heart.png"
path_to_home = "assets/home.png"
path_to_avocado = "assets/favicon.ico"
avocado = "assets/avocado.png"
real_python = "assets/real_python.png"
dash_logo = "assets/dash_logo.png"
ico_logo = "assets/flaticon.png"



layout = html.Div(
    children = [
        #create header
        html.Div(
            children = [
                html.Div(
                    children = [
                        html.P(children="🥑", className = "header-emoji"),
                        html.H1(
                            children = ["Avocado Analytics"],
                            className = "title-h1"
                        ),
                        html.P(
                            children = "Analyze the behavior of avocado prices"
                            " and the number of avocados sold in the US"
                            " between 2015 and 2018",
                            className = "title-p"                 
        ),
                    ],
                    className = "title"
                )
            ],
            className = "header"
        ),

        #create nav bar
        html.Div(
            children = [
                dcc.Link(html.Img(
                    src = encode_image(path_to_home),
                    className = "img-home"),
                    href = "/"),
                html.A("Price History", href = "/prices", className = "nav-prices"),
                html.A("Predictions", href = "/prediction", className = "nav-prediction"),
            ],
            className = "nav-bar"
        ),

        #create body
        html.Div(
            children = ["main body"],
            className = "body"
        ),

        #create footer
        html.Div(
            children = [
                html.Img(
                    src = encode_image(path_to_heart),
                    className = "img-heart"),
                html.P("Because we all love avocados",
                    className = "footer-text")],
            className = "footer"
        )

    ],
    className = "main"

)