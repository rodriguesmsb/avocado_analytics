import dash_core_components as dcc
import dash_html_components as html

from components.aux_func import encode_image

path_to_home =  "assets/home.png"



navBar = html.Div(
        children = [
            html.Div(
                children = [
                    dcc.Link(id = "home",
                             children = html.Img(src = encode_image(path_to_home), style = {"height": "93%"}),
                             href = "/")
                ], className = "col"),
            html.Div(
                children = [
                    dcc.Link(id = "prices",
                    children = html.P("PRICE HISTORY"),
                    href = "/prices",
                    className = "link-text"
                    )
                ], 
                className = "col"),
            html.Div(className = "col"),
            ],
        className = "row"
    )

