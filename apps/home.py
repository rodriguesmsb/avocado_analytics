import dash_core_components as dcc  
import dash_html_components as html

from components import nav_bar
from components.aux_func import encode_image

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

        html.Section(id = "slideshow",
                        children = [
                            html.Div(id = "slideshow-container", 
                                    children = [
                                        #try to fix this next time
                                        html.Div(id = "image"),
                                        dcc.Interval(id = 'interval', interval = 3000)
                                    ])
                    ],
                    className = "section"
                            
                            ),
    
        html.Div(id = "footer_body",
                children = [
                    html.Img(src = encode_image(path_to_image)),
                    html.P("Because we all love AVOCADOS!", className = "description_footer")
                            
            
    ],
        className = "footer"),
    ],
)

