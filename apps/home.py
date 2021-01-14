import dash_core_components as dcc  
import dash_html_components as html
import base64

from components import nav_bar

path_to_image = "assets/heart.png"


def encode_image(image_file):
    ''' 
    Function to encode a image in a format that allows its plot on html.Fig
    '''
    encode = base64.b64encode(open(image_file, "rb").read())
    return "data:image/jpeg;base64,{}".format(encode.decode())




layout = html.Div(
            children = [
                #   Create a div element to hold header
                html.Div(
                    children = [
                        html.P(children = "🥑", className = "emoji"),
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
    
                html.Div(children = [
                    html.P("Because we all love AVOCADOS!", className = "description"),
                    html.Img(src = encode_image(path_to_image))
            
            ],
                className = "footer"),
            ],
    )

