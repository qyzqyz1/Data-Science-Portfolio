import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import plotly.plotly as py
import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
plotly.tools.set_credentials_file(username='tomqu', api_key='aP4Eg4z5ExldqnhJsWfc')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
mapbox_access_token = 'pk.eyJ1IjoicXl6cXl6MSIsImEiOiJjanNodXdsMG8wcnAxNDlxZzhiazE3cjk2In0.8_FK2gmApimPtbIbKYcIlQ'

df = pd.read_csv("mapplot.csv")

crime_type = df['TYPE'].unique()

markdown_text = '''
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Further Explorations on:
##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How does each type of crime change over the years?
##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What are the major problems each neighbourhood is facing?
##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How are the crimes distributed among a week and a day?

###  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Let's find out the answers to the above questions in Tableau

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![Tableau Public Gallery](https://sm.pcmag.com/t/pcmag_uk/review/t/tableau-de/tableau-desktop_9582.640.jpg)](https://public.tableau.com/views/BankBalanceSegmentationinU_K_/Storyline?:embed=y&:display_count=yes)
'''

app.layout = html.Div([
    dcc.Tabs(id = "tabs", children = [
    dcc.Tab(label = "What occurred on a given date", style={'fontSize':20, 'fontWeight':'bold'}, children = [
    # Map plot showing crimes on a single day
    html.Div([
        html.Div(' Select a Date of Interest:', style={'fontSize':18, 'color':'blue','marginLeft': '1em','marginTop':'1em','marginBottom':'0.2em'}),
        html.Div([
        dcc.DatePickerSingle(
            id='my-date-picker-single',
            min_date_allowed=dt(2003, 1, 1),
            max_date_allowed=dt(2017, 7, 13),
            initial_visible_month=dt(2017, 5, 1),
            date=dt(2017, 5, 1)
        )],
        style={'marginLeft': '2em','float':'left','display':'inline-block'}
        ),
        html.Br(),
        html.Div(' Select a Pitch Level:', style={'fontSize':18, 'color':'blue','marginLeft': '20em','marginTop':'-2.8em'}),
        html.Div([
        dcc.Slider(
        id='pitch-level',
        min=0,
        max=90,
        value=0,
        marks={
            0: {'label': '0°', 'style': {'color': '#77b0b1'}},
            30: {'label': '30°'},
            60: {'label': '60°'},
            90: {'label': '90°', 'style': {'color': '#f50'}}
        },
        included=False
        )],
        style={'width':'20%','display':'inline-block','marginLeft': '8.5em','marginBottom':'2.2em','marginTop':'0.7em'}
        ),

        html.Div(' Select a Background Style:', style={'fontSize':18, 'color':'blue','marginLeft': '39em','marginTop':'-5em','marginBottom':'0.5em'}),
        html.Div([
        dcc.RadioItems(
        id='style-option',
        options=[
            {'label': 'Google Map', 'value': 'mapbox://styles/mapbox/basic-v9'},
            {'label': 'White', 'value': 'mapbox://styles/mapbox/light-v9'},
            {'label': 'Dark', 'value': 'mapbox://styles/mapbox/dark-v9'}
        ],
        value='mapbox://styles/mapbox/basic-v9',
        labelStyle={'display': 'inline-block'}
        )],
        style={'width':'20%','display':'inline-block','marginLeft': '36em','marginTop':'-15em','marginBottom':'1em'}
        ),
        html.Br(),
        dcc.Graph(id='singleday_map', config={'scrollZoom':True})
    ])
    ]),

    # Map plot showing different types of crimes
    dcc.Tab(label = "Where each type of crime tends to occur", style={'fontSize':20, 'fontWeight':'bold'}, children = [
    html.Div([
    html.Div(' Select a Crime Type:', style={'fontSize':18, 'color':'blue','marginLeft': '0.1em'}),
        dcc.Dropdown(
            id='crime',
            options=[{'label': str(i), 'value': str(i)} for i in crime_type],
            value='Break and Enter Commercial'
        )
        ],
        style={'width': '20%', 'float': 'left','display': 'inline-block','marginLeft': '1.5em'}),

    html.Div([
        html.Div(' Opacity Level:', style={'fontSize':18, 'color':'blue','marginLeft': '0.3em','marginTop':'0.1em'}),
        dcc.RadioItems(
            id='radio-item',
            options=[{'label': i, 'value': i} for i in [0.1,0.2,0.3,0.4,0.5]],
            value=0.2,
            labelStyle={'display': 'inline-block','marginTop':'0.4em'}
        )
        ],
        style={'display': 'inline-block','marginLeft': '3em'}),

    html.Div([
        html.Label('Year Range:', style={'fontSize':18, 'color':'blue','marginLeft': '1.3em','float':'left'}),
        html.Div([
        dcc.RangeSlider(
            id = 'year-range',
            min = pd.DatetimeIndex(df['DATE']).year.unique().min(),
            max = pd.DatetimeIndex(df['DATE']).year.unique().max(),
            value = [2013, 2017],
            marks={i: '{}'.format(i) for i in range(2003,2018)}
            )],
            style={'width': '60%','marginLeft': '10em','marginTop': '0.6em'}
            ),
            ]),
    html.Br(),
    dcc.Graph(id='crime_map', config={'scrollZoom':True})
    ]),
     dcc.Tab(label='Tableau Dashboard',style={'fontSize':20, 'fontWeight':'bold'}, children=[
                html.Div([
            dcc.Markdown(children=markdown_text)
        ])
        ])
    ])
    ])

@app.callback(
    dash.dependencies.Output('singleday_map', 'figure'),
    [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('pitch-level','value'),
    dash.dependencies.Input('style-option','value')])

def update_figure(picker_date, pitch_level,style_option):
    date = dt.strptime(picker_date, '%Y-%m-%d')
    dff = df[(df['YEAR']==date.year) & (df['MONTH']==date.month) & (df['DAY']==date.day)]
    data = []
    for crime_type in df['TYPE'].unique():
        temp = dff[dff['TYPE']==crime_type]
        temp_data = go.Scattermapbox(
            lat=temp['Latitude'],
            lon=temp['Longitude'],
            mode='markers',
            marker=dict(
                size=12,
                color=temp['Color'],
            ),
            text=temp['TYPE'] + " at " + temp['NEIGHBOURHOOD'],
            name=crime_type)
        data.append(temp_data)
    return {
        'data': data,
        'layout': go.Layout(
            autosize=True,
            height=650,
            hovermode='closest',
            margin={'l': 10, 'b': 10, 't':10, 'r': 10},
            legend={'x': 0, 'y': 1},
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(
                lat=49.25,
                lon=-123.1
                ),
            pitch=pitch_level,
            style=style_option,
            zoom=11)
        )
}

@app.callback(
    dash.dependencies.Output('crime_map', 'figure'),
    [dash.dependencies.Input('crime', 'value'),
    dash.dependencies.Input('radio-item','value'),
    dash.dependencies.Input('year-range', 'value')])
def update_figure(crime_name, opacity_value, year_range):
    subset_df = df[df['TYPE'] == crime_name]
    start_year = int(year_range[0])
    end_year = int(year_range[1])
    dff = subset_df[(pd.DatetimeIndex(subset_df['DATE']).year >=start_year) & (pd.DatetimeIndex(subset_df['DATE']).year <= end_year)]
    return {
        'data': [go.Scattermapbox(
            lat=dff['Latitude'],
            lon=dff['Longitude'],
            text=dff['TYPE'],
            mode='markers',
            marker=dict(
                size=10,
                color=dff['Color'],
                opacity=opacity_value),
            name = crime_name
        )],
        'layout': go.Layout(
            autosize=True,
            height=650,
            hovermode='closest',
            margin={'l': 10, 'b': 10, 't':10, 'r': 10},
            legend={'x': 0, 'y': 1},
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(
                lat=49.25,
                lon=-123.1
                ),
            pitch=0,
            zoom=11)
        )
}


if __name__ == '__main__':
    app.run_server(debug=True)
