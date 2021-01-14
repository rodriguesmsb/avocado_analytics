import dash_bootstrap_components as dbc
import dash_html_components as html
import base64

path_to_home =  "assets/home.png"


def encode_image(image_file):
    ''' 
    Function to encode a image in a format that allows its plot on html.Fig
    '''
    encode = base64.b64encode(open(image_file, "rb").read())
    return "data:image/jpeg;base64,{}".format(encode.decode())

navBar = html.Div(
        children = [
            html.Div(className = "col"),
            html.Div(className = "col"),
            html.Div(className = "col")
            ],
        className = "row"
    )

