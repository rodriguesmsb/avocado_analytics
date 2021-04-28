
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

        html.Section(id = "figures",
                        children = [
                            html.Div(
                                children = [
                                    html.P("About Avocados!", className = "home-text"),
                                    html.A(
                                        html.Img(src = encode_image(avocado), className = "figure"),
                                        href = "https://en.wikipedia.org/wiki/Avocado"
                                    )
                                ],
                            ),
                            html.Div(
                                children = [
                                    html.P("Inspired by!", className = "home-text"),
                                    html.A(
                                        html.Img(src = encode_image(real_python), className = "figure"),
                                         href = "https://realpython.com/python-dash/"
                                    ),
                                    
                                ]
                                
                            ),
                            html.Div(
                                children = [
                                    html.P("Created using!", className = "home-text"),
                                    html.A(
                                        html.Img(src = encode_image(dash_logo), className = "figure"),
                                        href = "https://dash.plotly.com/"
                                    ),
                                    
                                ]
                            ),
                            html.Div(
                                children = [
                                    html.P("Icons", className = "home-text"),
                                    html.A(
                                        html.Img(src = encode_image(ico_logo), className = "figure"),
                                        href = "https://www.flaticon.com/"

                                    )
                                    

                                ]
                            )       
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
