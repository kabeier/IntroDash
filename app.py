#import dash 
import dash
#import dcc to create our graph in our layout
import dash_core_components as dcc
#used to generate HTML components
import dash_html_components as html

#init a Dash as app
app=dash.Dash()
#Colors dictionary 
colors={
    'background' : '#111111',
    'text' : '#7FDBFF'
}
#style here is camelCase but same as css and you use className instead of class

#Build the app layout in HTML with the html import
    #The HTML tag names are capitalized
app.layout = html.Div(
    #Build the page
    style={'backgroundColor':colors['background']},
    children=[
        html.H1(
            children='Hello Dash',
            style={
                'textAlign':'center',
                'color':colors['text']
            }
        ),
        html.Div(
            children='Dash: A web application framework for Python.',
            style={
                'textAlign' : 'center',
                'color' : colors['text']
            }
        ),
        #Add the Graph to the page
        dcc.Graph(
            id='Graph1',
            figure={
                'data':[
                    {'x':[1,2,3],'y':[4,1,2], 'type':'bar', 'name':'SF'},
                    {'x':[1,2,3],'y':[2,4,5], 'type':'bar', 'name':'Montreal'}
                ],
                'layout':{
                    'plot_bgcolor' : colors['background'],
                    'paper_bgcolor' : colors['background'],
                    'font' : {
                        'color' : colors['text']
                    }

                }
            }
        )
])

if __name__ == '__main__':
    app.run_server(debug=True)