from dash import Dash, dcc, html, Input, Output, dash_table
import pandas as pd
from dash.exceptions import PreventUpdate
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

available_countries = ['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina', 'Australia',
 'Austria', 'Bahrain', 'Bangladesh', 'Belgium']

app.layout = html.Div([
    
    dcc.Store(id='store_data', data=[], storage_type="session"),
    dcc.Store(id='temp_store_data', data=[], storage_type="memory"),

    html.Button(id='button', children='load-data'),

    html.H2('Country'),
    dcc.Dropdown(available_countries, 'Canada', id='select_country'),
    dash_table.DataTable(id='data_table'),
    
])

@app.callback(
    Output('store_data', 'data'),
    Input('button', 'n_clicks')
)
def get_store_data(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        print('load data clicked')
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
        return df.to_dict('records')


@app.callback(
    Output('temp_store_data', 'data'),
    [
        Input('select_country', 'value'),
        Input('store_data', 'data')
    ]
)
def get_temp_store_data(country_col, store_data):
    df = pd.DataFrame(store_data)
    if len(df)>=1:    
        dff= df[df.country==country_col]
        #print(dff.to_dict('records'))
        return dff.to_dict('records')
    else: 
        return []

@app.callback(
    Output('data_table', 'data'),
    Input('temp_store_data', 'data'),
)
def get_data(temp_data):
    dff= pd.DataFrame(temp_data)
    return dff.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True, port=9002)