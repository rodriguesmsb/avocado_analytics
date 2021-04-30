import dash_core_components as dcc  
import dash_html_components as html

from components import nav_bar
from components.aux_func import encode_image

path_to_image = "assets/heart.png"
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
            children = ["navbar"],
            className = "nav-bar"
        ),

        #create body
        html.Div(
            children = ["main body"],
            className = "body"
        ),

        #create footer
        html.Div(
            children = ["footer"],
            className = "footer"
        )

    ],
    className = "main"

)