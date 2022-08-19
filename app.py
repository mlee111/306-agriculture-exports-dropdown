import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'Pokedex'
sourceurl = 'https://plot.ly/python/choropleth-maps/'
githublink = 'https://github.com/mlee111/306-agriculture-exports-dropdown'
# here's the list of possible columns to choose from.

list_of_columns = ['Water', 'Grass', 'Fire', 'Normal', 'Bug', 'Poison', 'Electric', 'Fairy', 'Psychic', 'Dragon', 'Dark', 'Ground', 'Fighting', 'Rock', 'Ice']
########## Set up the chart

import pandas as pd
df = pd.read_csv('assets/Pokemon.csv')

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1('Pokemon Data'),
    html.Div([
        html.Div([
                html.H6('Select a variable for analysis:'),
                dcc.Dropdown(
                    id='options-drop',
                    options=[{'label': i, 'value': i} for i in list_of_columns],
                    value='Type 1'
                ),
        ], className='two columns'),
        html.Div([dcc.Graph(id='figure-1'),
            ], className='ten columns'),
    ], className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


# make a function that can intake any varname and produce a map.
@app.callback(Output('figure-1', 'figure'),
             [Input('options-drop', 'value')])
def make_figure(varname):
    mygraphtitle = f'Pokemon grouped by generation'
    mycolorbartitle = "Num Pokemon"

    subset = df[df['Type 1'] == varname]
    grouped_data = subset.groupby('Generation')
    df = pd.DataFrame(grouped_data.count()['Type 1'])
    
    barchart = go.Bar(
        x=df.index,
        y=df['Type 1'],
        name=varname
    )
    fig = go.Figure(data=[barchart])
    fig.show()
    return fig


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
