from dash.dependencies import Input, Output
from dash_core_components import RadioItems
from dash_html_components import Div
from django_plotly_dash import DjangoDash

app = DjangoDash('tom_targets')

app.layout = Div([
    RadioItems(
        id='dropdown-color',
        options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
        value='red'
    ),
    Div(id='output-color'),
    RadioItems(
        id='dropdown-size',
        options=[{'label': i, 'value': j} for i, j in [('L', 'large'), ('M', 'medium'), ('S', 'small')]],
        value='medium'
    ),
    Div(id='output-size')
])

@app.callback(Output('output-color', 'children'), [Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    return f'The selected color is {dropdown_value}'

@app.callback(Output('output-size', 'children'), [Input('dropdown-color', 'value'), Input('dropdown-size', 'value')])
def callback_size(dropdown_color, dropdown_size):
    return f'The chosen T-shirt is a {dropdown_color} {dropdown_size} one.'