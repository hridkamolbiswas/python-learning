from dash import Dash, dcc, html, Input, Output
import pandas as pd
from dash.exceptions import PreventUpdate

import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

available_countries = df['country'].unique()
#print(available_countries[0:10])
app.layout = html.Div([
    html.H2('Country'),
    dcc.Dropdown(available_countries, 'Canada', id='select_country'),
    dcc.Graph(id='graph'),
    
])

@app.callback(
    Output('graph', 'figure'),
    Input('select_country', 'value'),
)
def get_figure(country_col):
    dff= df[df.country==country_col]
    return px.scatter(dff, x='year')


if __name__ == '__main__':
    app.run_server(debug=True, port=9001)