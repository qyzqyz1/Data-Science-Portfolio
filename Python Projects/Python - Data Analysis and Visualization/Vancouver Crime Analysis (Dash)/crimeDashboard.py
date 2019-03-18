import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import plotly.plotly as py
import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import dash_table
import datetime
import numpy as np


plotly.tools.set_credentials_file(username='tomqu', api_key='aP4Eg4z5ExldqnhJsWfc')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
mapbox_access_token = 'pk.eyJ1IjoicXl6cXl6MSIsImEiOiJjanNodXdsMG8wcnAxNDlxZzhiazE3cjk2In0.8_FK2gmApimPtbIbKYcIlQ'

df = pd.read_csv("Vancouver_Crime.csv")
df['DATE'] = pd.to_datetime(df['DATE'])
color_df = df[['TYPE','Color']].drop_duplicates()

crime_type = df['TYPE'].unique()
crime_type = np.insert(crime_type, 0, 'All')
col_names = ['Rank', 'Neighbourhoods', 'Counts', '% Among Neighbourhoods',
       'Total Crimes', '% Among Total Crimes']
columns = [{'name': i, 'id': i, 'deletable': True} for i in col_names]

July = dt.strptime('2017-07-01', '%Y-%m-%d')
t_df = df.groupby(["YEAR","MONTH"]).aggregate({"NEIGHBOURHOOD":"count"})
t_df.columns=['Count']
t_df.reset_index(inplace=True)
t_df = t_df.assign(DATE=pd.to_datetime(t_df[['YEAR', 'MONTH']].assign(day=1)))
t_df = t_df[t_df['DATE']<July]
l_df = t_df.reset_index()

t_val = []
t_lab = []

PAGE_SIZE = 5

markdown_text1 = '''

&nbsp;

## &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Vancouver&nbsp;&nbsp; Crime&nbsp;&nbsp; EDA

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Crime Analysis](https://images.projectsgeek.com/2016/01/Crime-Investigation-Management-System.jpg)

'''

markdown_text = '''

&nbsp;

&nbsp;

# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Thank you!


&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Downtown Vancouver](https://cdn.passporthealthglobal.com/wp-content/uploads/2018/03/passport-health-downtown-vancouver-travel-clinic-page.jpg?x10491)
'''

app.layout = html.Div([
    dcc.Tabs(id = "tabs", children = [
    dcc.Tab(label='Introduction',style={'fontSize':20, 'fontWeight':'bold'}, children=[
        html.Div([
        dcc.Markdown(children=markdown_text1)
    ])
    ]),
    dcc.Tab(label = "Initial Exploration", style={'fontSize':20, 'fontWeight':'bold'}, children = [
    # Map plot showing crimes on a single day
    html.Div([
        html.Div(' Select a Date of Interest:', style={'fontSize':18, 'color':'blue','marginLeft': '1em','marginTop':'1em','marginBottom':'0.2em'}),
        html.Div([
        dcc.DatePickerSingle(
            id='my-date-picker-single',
            min_date_allowed=dt(2003, 1, 1),
            max_date_allowed=dt(2017, 7, 13),
            initial_visible_month=dt(2016, 1, 1),
            date=dt(2016, 1, 1)
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
            45: {'label': '45°'},
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
            {'label': 'Dark', 'value': 'mapbox://styles/mapbox/dark-v9'},
            {'label': 'White', 'value': 'mapbox://styles/mapbox/light-v9'}
        ],
        value='mapbox://styles/mapbox/basic-v9',
        labelStyle={'display': 'inline-block'}
        )],
        style={'width':'20%','display':'inline-block','marginLeft': '36em','marginTop':'-15em','marginBottom':'1em'}
        ),

        html.Div([
        html.Label('Enter number of days from now:', style={'fontSize':18, 'color':'blue'}),
        dcc.Input(
            id='days-away',
            placeholder='Enter a value...',
            type='text',
            value=''
        )],
        style={'marginTop':'-5.3em','marginLeft':'69em'}
        ),

        html.Div([
        html.Label('Color Opacity:', style={'fontSize':18, 'color':'blue'}),
        dcc.Dropdown(
        id='color-opacity',
        options=[
            {'label': '1.0', 'value': '1.0'},
            {'label': '0.5', 'value': '0.5'},
            {'label': '0.4', 'value': '0.4'},
            {'label': '0.3', 'value': '0.3'},
            {'label': '0.2', 'value': '0.2'},
            {'label': '0.1', 'value': '0.1'}
            ],
            value='1.0'
        )],
        style={'width':'7%','marginTop':'-4.4em','marginLeft':'90em'}
        ),

        html.Br(),
        dcc.Graph(id='singleday_map', config={'scrollZoom':True})
    ])
    ]),

    # Map plot showing different types of crimes
    dcc.Tab(label = "Further Exploration", style={'fontSize':20, 'fontWeight':'bold'}, children = [
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
    html.Div([
        html.Div([
            dcc.Graph(id='crime_map', config={'scrollZoom':True})
            ],style={'display':'inline-block'}),
        html.Div([
            dcc.Graph(id='bar_plot', clear_on_unhover=True),
            dash_table.DataTable(
                id='table-paging-and-sorting',
                columns=columns,
                style_cell={'textAlign': 'center','fontSize':'12'},
                style_header={
                    'fontWeight': 'bold',
                    'fontSize':'14',
                    'backgroundColor': 'rgb(187, 233, 249)'
                },
                style_cell_conditional=[
                {
                'if': {'column_id': c},
                'textAlign': 'left'
                } for c in columns],
                pagination_settings={
                    'current_page': 0,
                    'page_size': PAGE_SIZE
                },
                pagination_mode='be',
                sorting='be',
                sorting_type='single',
                sorting_settings=[]
            )
        ],style={'display':"inline-block"})
    ]),
    html.Div([
        html.Div([
        dcc.Graph(id='time-series')
        ], className='six columns'),
        html.Div([
        dcc.Graph(id='time-plots'),
        dcc.RadioItems(
            id='select-timeplot',
            options=[
                {'label': 'Months in Year', 'value': 'bar_chart'},
                {'label': 'Days and Hours', 'value': 'heatmap'}
                ],
            value='bar_chart',
            labelStyle={'display':'inline-block'},
            style={'marginLeft':'5.5em'}
        )
        ], className='six columns')
    ], className='row')


    ]),

    # Live Updating Plot
    dcc.Tab(label='Trendline',style={'fontSize':20, 'fontWeight':'bold'}, children=[

        html.Div([
            dcc.Graph(id='live-update-graph'),
            dcc.Interval(
                id='interval-component',
                interval=18/179*1000, # 2000 milliseconds = 2 seconds
                n_intervals=0
            )
        ])
        ]),


    # Conclusion
    dcc.Tab(label='Conclusion',style={'fontSize':20, 'fontWeight':'bold'}, children=[
                html.Div([
            dcc.Markdown(children=markdown_text)
        ])
        ])
    ], colors={'primary':'gold','background':'snow'})
    ])

@app.callback(
    dash.dependencies.Output('singleday_map', 'figure'),
    [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('pitch-level','value'),
    dash.dependencies.Input('style-option','value'),
    dash.dependencies.Input('days-away','value'),
    dash.dependencies.Input('color-opacity','value')])

def update_singleday_map(picker_date, pitch_level,style_option,days_away,col_opacity):
    date = dt.strptime(picker_date, '%Y-%m-%d')
    if days_away != '':
        passed_days = int(days_away)
        end_date = date + datetime.timedelta(passed_days)
        if end_date > date:
            dff = df[(df['DATE']>=date) & (df['DATE']<=end_date)]
        else:
            dff = df[(df['DATE']>=end_date) & (df['DATE']<=date)]
    else:
        dff = df[df['DATE']==date]
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
                opacity=float(col_opacity)
            ),
            text=temp['TYPE'] + " at " + temp['NEIGHBOURHOOD'],
            name=crime_type)
        data.append(temp_data)
    return {
        'data': data,
        'layout': go.Layout(
            autosize=True,
            height=700,
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
    dash.dependencies.Input('year-range', 'value'),
    dash.dependencies.Input('bar_plot','hoverData')])
def update_crime_map(crime_name, opacity_value, year_range, hover_data):
    if hover_data == None:
        if crime_name != 'All':
            subset_df = df[df['TYPE'] == crime_name]
        else:
            subset_df = df
        start_year = int(year_range[0])
        end_year = int(year_range[1])
        dff = subset_df[(pd.DatetimeIndex(subset_df['DATE']).year >=start_year) & (pd.DatetimeIndex(subset_df['DATE']).year <= end_year)]
    else:
        if crime_name != 'All':
            subset_df = df[df['TYPE'] == crime_name]
        else:
            subset_df = df
        start_year = int(year_range[0])
        end_year = int(year_range[1])
        dff = subset_df[(pd.DatetimeIndex(subset_df['DATE']).year >=start_year) & (pd.DatetimeIndex(subset_df['DATE']).year <= end_year)]
        dff = dff[dff['NEIGHBOURHOOD']==hover_data['points'][0]['x']]
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
            height=600,
            width = 850,
            hovermode='closest',
            margin={'l': 10, 'b': 10, 't':10, 'r': 10},
            legend={'x': 0, 'y': 1},
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(
                lat=49.257,
                lon=-123.12
                ),
            pitch=0,
            zoom=11)
        )
}

@app.callback(
    dash.dependencies.Output('bar_plot', 'figure'),
    [dash.dependencies.Input('crime', 'value'),
    dash.dependencies.Input('year-range', 'value')])
def update_barplot(crime_name,year_range):
    if crime_name != 'All':
        subset_df = df[df['TYPE'] == crime_name]
    else:
        subset_df = df
    start_year = int(year_range[0])
    end_year = int(year_range[1])
    dff = subset_df[(pd.DatetimeIndex(subset_df['DATE']).year >=start_year) & (pd.DatetimeIndex(subset_df['DATE']).year <= end_year)]
    n_df = dff.groupby("NEIGHBOURHOOD").aggregate({"TYPE":"count"})
    n_df.columns = ['Count']
    n_df.reset_index(inplace=True)
    n_df.sort_values(by='Count',ascending=False,inplace=True)
    top_df = n_df.head(5)
    percent = round(top_df['Count']/n_df['Count'].sum()*100,1)
    percent = list(map(str, percent))
    percent = ['{}%'.format(x) for x in percent]
    return {
        'data': [
            go.Bar(
                x=top_df['NEIGHBOURHOOD'],
                y=top_df['Count'],
                text=percent,
                textposition='auto',
                textfont=dict(
                size=14,
                color='black'
                ),
                marker=dict(
                color='rgb(158, 161, 225)')
                )
        ],
        'layout': go.Layout(
            xaxis=dict(
            tickangle=0,
            tickfont=dict(
                size=10.5
                ),
            tickwidth=1.2
            ),
            title=crime_name + " <br>"+"Top 5 (out of 24) Neighbourhoods",
            titlefont=dict(
                size=20
                )
        )
}

@app.callback(
    dash.dependencies.Output('table-paging-and-sorting', 'data'),
    [dash.dependencies.Input('table-paging-and-sorting', 'pagination_settings'),
     dash.dependencies.Input('table-paging-and-sorting', 'sorting_settings'),
     dash.dependencies.Input('crime','value'),
     dash.dependencies.Input('year-range','value')
     ])
def update_graph(pagination_settings, sorting_settings, crime_name, year_range):
    if crime_name != 'All':
        subset_df = df[df['TYPE'] == crime_name]
    else:
        subset_df = df
    start_year = int(year_range[0])
    end_year = int(year_range[1])
    new_df = subset_df[(pd.DatetimeIndex(subset_df['DATE']).year >=start_year) & (pd.DatetimeIndex(subset_df['DATE']).year <= end_year)]

    new_df = new_df.groupby("NEIGHBOURHOOD").aggregate({"TYPE":"count"})
    new_df.columns=['Counts']
    new_df.reset_index(inplace=True)
    new_df.sort_values(by='Counts',ascending=False,inplace=True)
    top_df = new_df.head(5)
    new_df['% Among Neighbourhoods'] = round(new_df['Counts']/new_df['Counts'].sum()*100,2)

    t2_df = df[(pd.DatetimeIndex(df['DATE']).year >=start_year) & (pd.DatetimeIndex(df['DATE']).year <= end_year)]
    table = t2_df.groupby(["NEIGHBOURHOOD","TYPE"]).aggregate({"YEAR":'count'})
    table.columns=['Counts']
    table.reset_index(inplace=True)
    by_crime = table.groupby("TYPE").aggregate({"Counts":'sum'})
    by_crime.reset_index(inplace=True)
    by_crime['Avg Percentage'] = round(by_crime['Counts']/by_crime['Counts'].sum()*100,2)
    table2 = table.groupby('NEIGHBOURHOOD').aggregate({"Counts":'sum'})
    table2.columns=['Total Crimes']
    table2.reset_index(inplace=True)
    n_df = new_df.merge(table2,how='left',on='NEIGHBOURHOOD')
    n_df['Percentage among total crimes'] = round(n_df['Counts']/n_df['Total Crimes']*100,2)
    n_df.insert(0,column='Rank',value=range(1,len(n_df)+1))
    n_df.columns = ['Rank', 'Neighbourhoods', 'Counts', '% Among Neighbourhoods', 'Total Crimes', '% Among Total Crimes']


    if len(sorting_settings):
        dff = n_df.sort_values(
            sorting_settings[0]['column_id'],
            ascending=sorting_settings[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff = n_df

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('rows')

@app.callback(
    dash.dependencies.Output('table-paging-and-sorting', 'style_data_conditional'),
    [dash.dependencies.Input('bar_plot', 'hoverData'),
    dash.dependencies.Input('crime','value'),
    dash.dependencies.Input('year-range','value')])

def update_style(hover_data, crime_name, year_range):
    if hover_data != None:
        if crime_name != 'All':
            subset_df = df[df['TYPE'] == crime_name]
        else:
            subset_df = df
        start_year = int(year_range[0])
        end_year = int(year_range[1])
        new_df = subset_df[(pd.DatetimeIndex(subset_df['DATE']).year >=start_year) & (pd.DatetimeIndex(subset_df['DATE']).year <= end_year)]

        new_df = new_df.groupby("NEIGHBOURHOOD").aggregate({"TYPE":"count"})
        new_df.columns=['Counts']
        new_df.reset_index(inplace=True)
        new_df.sort_values(by='Counts',ascending=False,inplace=True)
        top_df = new_df.head(5)
        top_df.reset_index(inplace=True)
        index = top_df[top_df['NEIGHBOURHOOD']==hover_data['points'][0]['x']].index.values[0]
        style_data_conditional=[{
        'if': {'column_id': 'Neighbourhoods'},
            'backgroundColor': '#f3f7a5',
        "if": {"row_index": index},
            "backgroundColor": "#35ce96",
            'color': 'white',
            'fontSize':'15',
        }]
    else:
        style_data_conditional=[{
        'if': {'column_id': 'Neighbourhoods'},
            'backgroundColor': '#f3f7a5',
        }]
    return style_data_conditional

@app.callback(
    dash.dependencies.Output('time-series', 'figure'),
    [dash.dependencies.Input('crime','value'),
    dash.dependencies.Input('year-range','value'),
    dash.dependencies.Input('bar_plot','hoverData')])

def update_time_series(crime_name, year_range, hover_data):
    if hover_data == None:
        if crime_name != 'All':
            subset_df = df[df['TYPE'] == crime_name]
        else:
            subset_df = df
        start_year = int(year_range[0])
        end_year = int(year_range[1])
        n_dff = subset_df[(pd.DatetimeIndex(subset_df['DATE']).year >=start_year) & (pd.DatetimeIndex(subset_df['DATE']).year <= end_year)]
    else:
        if crime_name != 'All':
            subset_df = df[df['TYPE'] == crime_name]
        else:
            subset_df = df
        start_year = int(year_range[0])
        end_year = int(year_range[1])
        n_dff = subset_df[(pd.DatetimeIndex(subset_df['DATE']).year >=start_year) & (pd.DatetimeIndex(subset_df['DATE']).year <= end_year)]
        n_dff = n_dff[n_dff['NEIGHBOURHOOD']==hover_data['points'][0]['x']]

    July = dt.strptime('2017-07-01', '%Y-%m-%d')
    dff = n_dff.groupby(["TYPE","YEAR","MONTH"]).aggregate({"NEIGHBOURHOOD":"count"})
    dff.columns=['Count']
    dff.reset_index(inplace=True)
    dff = dff.assign(DATE=pd.to_datetime(dff[['YEAR', 'MONTH']].assign(day=1)))
    dff = dff[dff['DATE']<July]

    dff = dff.merge(color_df,how='left',on=['TYPE'])

    data = []
    for i in dff['TYPE'].unique():
        temp_df = dff[dff['TYPE']==i]
        trace = go.Scatter(
                    x=temp_df.DATE,
                    y=temp_df['Count'],
                    name = i,
                    line = dict(color = dff[dff['TYPE']==i]['Color'].unique()[0]),
                    opacity = 0.8)
        data.append(trace)

    return {
    'data': data,
    'layout': dict(
        title='Time Series from {} to {}'.format(start_year, end_year),
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=2,
                         label='2yr',
                         step='year',
                         stepmode='backward'),
                    dict(count=1,
                         label='1yr',
                         step='year',
                         stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(
                visible = True
            ),
            type='date'
        )
        )

    }

@app.callback(
    dash.dependencies.Output('time-plots', 'figure'),
    [dash.dependencies.Input('crime','value'),
    dash.dependencies.Input('year-range','value'),
    dash.dependencies.Input('select-timeplot','value'),
    dash.dependencies.Input('bar_plot','hoverData')])

def time_plot(crime_name, year_range,selection, hover_data):
    if hover_data == None:
        if crime_name != 'All':
            subset_df = df[df['TYPE'] == crime_name]
        else:
            subset_df = df
        start_year = int(year_range[0])
        end_year = int(year_range[1])
        n_dff = subset_df[(pd.DatetimeIndex(subset_df['DATE']).year >=start_year) & (pd.DatetimeIndex(subset_df['DATE']).year <= end_year)]
    else:
        if crime_name != 'All':
            subset_df = df[df['TYPE'] == crime_name]
        else:
            subset_df = df
        start_year = int(year_range[0])
        end_year = int(year_range[1])
        n_dff = subset_df[(pd.DatetimeIndex(subset_df['DATE']).year >=start_year) & (pd.DatetimeIndex(subset_df['DATE']).year <= end_year)]
        n_dff = n_dff[n_dff['NEIGHBOURHOOD']==hover_data['points'][0]['x']]

    if selection == 'bar_chart':
        month_df = n_dff.groupby("MONTH").aggregate({"TYPE":"count"})
        month_df.columns=['Count']
        month_df.reset_index(inplace=True)
        max_month = month_df[month_df['Count']==max(month_df['Count'])]['MONTH'].values[0]
        color = ['#53dbd1']*12
        color[max_month-1]='#ef9bd3'
        color2 = ['#4a86ef']*12
        color2[max_month-1]='#f2186f'

        Bar = go.Bar(
            x=month_df['MONTH'],
            y=month_df['Count'],
            marker=dict(
                color=color),
            name='Bar'
            )

        Line = go.Scatter(
            x=month_df['MONTH'],
            y=month_df['Count'],
            marker=dict(
                color=color2,
                size=12),
            name='Line'
                )

        data = [Bar,Line]
        layout = go.Layout(
        xaxis=dict(
            tickangle=0,
            tickfont=dict(
                size=10.5
                ),
            tickwidth=1.2,
            tickvals=month_df['MONTH'],
            title='Month'
            ),
        yaxis=dict(title='Crime Counts'),
        title='Crime Distribution by Month'
        )
        return {
        'data':data,
        'layout':layout
        }

    else:
        dof_hr = n_dff.groupby(['DAY_OF_WEEK','HOUR']).aggregate({"DATE":'count'})
        dof_hr.columns=['Count']
        dof_hr.reset_index(inplace=True)
        x=list(range(1,25))
        y=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday','Sunday']
        z = []
        for i in dof_hr['DAY_OF_WEEK'].unique():
            z.append(list(dof_hr[dof_hr['DAY_OF_WEEK']==i]['Count']))
        trace = go.Heatmap(z=z, x=x,y=y,colorscale='Hot',reversescale=True)
        data=[trace]
        layout = go.Layout(
        dict(
            showlegend = True,
            xaxis=dict(
            tickvals=x,
            title='Hours in Day'
            ),
            autosize = True,
            title='Crime Distribution Heatmap',
            )
        )
        return {
        'data':data,
        'layout':layout
        }

@app.callback(
    dash.dependencies.Output('live-update-graph', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')])
def update_plot(n):
        if n < 182:
            x = l_df['index']
            y = l_df['Count']

            x = np.array(x)
            y = np.array(y)
            x = x[:n]
            y = y[:n]

            if (n-1)%12==0:
                t_val.append(n)
                t_lab.append(l_df['YEAR'][n])
            # calculate polynomial
            z = np.polyfit(x, y, 3)
            f = np.poly1d(z)


            # calculate new x's and y's
            x_new = np.linspace(x[0], x[-1], len(x)*10)
            y_new = f(x_new)

            # Creating the dataset, and generating the plot
            trace1 = go.Scatter(
                                 x=x,
                                 y=y,
                                 mode='markers',
                                 marker=go.Marker(color='rgb(255, 127, 14)'),
                                 name='Data'
                                 )

            trace2 = go.Scatter(
                                  x=x_new,
                                  y=y_new,
                                  mode='lines',
                                  marker=go.Marker(color='rgb(31, 119, 180)'),
                                  name='Fit'
                                  )

            layout = go.Layout(
                                title='Overall Crime Trend in Vancouver',
                                titlefont=dict(size=22),
                                plot_bgcolor='rgb(248, 249, 247)',
                                 xaxis=go.XAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)', title='Time', titlefont=dict(size=16),
                                 tickvals=t_val, ticktext=t_lab, tickfont=dict(size=14, color='blue')),
                                 yaxis=go.YAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)', title='Crime Counts',titlefont=dict(size=16))
                                )

            data = [trace1, trace2]
            return{
                'data':data,
                'layout':layout
            }


if __name__ == '__main__':
    app.run_server(debug=True)
