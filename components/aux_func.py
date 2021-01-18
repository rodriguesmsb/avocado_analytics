import base64


def encode_image(image_file):
    ''' 
    Function to encode a image in a format that allows its plot on html.Fig
    '''
    encode = base64.b64encode(open(image_file, "rb").read())
    return "data:image/jpeg;base64,{}".format(encode.decode())