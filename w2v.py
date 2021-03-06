import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import pickle
from gensim.models import KeyedVectors

from w2v_functions import *



# set styling
external_stylesheets = [dbc.themes.CERULEAN]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# a useful variable
source_list = ['plato', 'aristotle', 'capitalism', 'communism',
                'continental', 'empiricism', 'german_idealism', 
                'phenomenology', 'rationalism', 'analytic', 'Locke', 
                'Hume', 'Berkeley', 'Spinoza','Leibniz', 'Descartes', 
                'Malebranche', 'Russell', 'Moore', 'Wittgenstein', 
                'Lewis', 'Quine', 'Popper', 'Kripke', 'Foucault',
                'Derrida', 'Deleuze', 'Merleau-Ponty', 'Husserl', 
                'Heidegger', 'Kant', 'Fichte', 'Hegel', 'Marx', 
                'Lenin', 'Smith', 'Ricardo','Keynes']



# overall layout
app.layout = html.Div([
  dcc.Dropdown(id="w2v-selection-1", 
                  options=get_dropdown_list_w2v(),
                  style={'width': '95%'},
                  placeholder='Start typing to search...'),
      dbc.Input(id='w2v-text-bar-1',
                placeholder="Enter text to see what words are used in similar contexts", 
                type="text", 
                n_submit=0,
                style={'width': '90%'}),
      dbc.Button("SUBMIT", id="w2v-submit-button-1", color="primary", className="mr-1", n_clicks=0),
      html.Div(id="w2v-output-1", children=[]),

  # dbc.Row([
  #   dbc.Col(html.Div([
  #     dcc.Dropdown(id="w2v-selection-1", 
  #                 options=get_dropdown_list_w2v(),
  #                 style={'width': '90%'},
  #                 placeholder='Start typing to search...'),
  #     dbc.Input(id='w2v-text-bar-1',
  #               placeholder="Enter text to see what words are used in similar contexts", 
  #               type="text", 
  #               n_submit=0,
  #               style={'width': '90%'}),
  #     dbc.Button("SUBMIT", id="w2v-submit-button-1", color="primary", className="mr-1", n_clicks=0),
  #     html.Div(id="w2v-output-1", children=[])
  #   ])),
  #   dbc.Col(html.Div([
  #     dcc.Dropdown(id="w2v-selection-2", 
  #                 options=get_dropdown_list_w2v(),
  #                 style={'width': '90%'},
  #                 placeholder='Start typing to search...'),
  #     dbc.Input(id='w2v-text-bar-2',
  #               placeholder="Enter text to see what words are used in similar contexts", 
  #               type="text", 
  #               n_submit=0,
  #               style={'width': '90%'}),
  #     dbc.Button("SUBMIT", id="w2v-submit-button-2", color="primary", className="mr-1", n_clicks=0),
  #     html.Div(id="w2v-output-2", children=[])
  #   ])),
  #   dbc.Col(html.Div([
  #     dcc.Dropdown(id="w2v-selection-3", 
  #                 options=get_dropdown_list_w2v(),
  #                 style={'width': '90%'},
  #                 placeholder='Start typing to search...'),
  #     dbc.Input(id='w2v-text-bar-3',
  #               placeholder="Enter text to see what words are used in similar contexts", 
  #               type="text", 
  #               n_submit=0,
  #               style={'width': '90%'}),
  #     dbc.Button("SUBMIT", id="w2v-submit-button-3", color="primary", className="mr-1", n_clicks=0),
  #     html.Div(id="w2v-output-3", children=[])
  #   ]))
  # ])
])




# callbacks, tripled
@app.callback(Output(component_id="w2v-output-1", component_property="children"),
              [Input(component_id="w2v-submit-button-1", component_property="n_clicks"),
              Input(component_id="w2v-text-bar-1", component_property="n_submit"),
              Input(component_id='w2v-selection-1', component_property='value')],
              [State(component_id="w2v-text-bar-1", component_property="value")])
def generate_similarity_1(n_clicks, n_submit, source_selection, word):
  # with open('w2v.pkl', 'rb') as w2v_d:
  #   w2v_dict = pickle.load(w2v_d)
  # w2v = KeyedVectors.load(f'w2v_models/{source_selection}_w2v.wordvectors')
  if n_clicks < 1 and n_submit < 1:
    return None
  else:
    try:
      w2v = KeyedVectors.load(f'w2v_models/{source_selection}_w2v.wordvectors')

      similar_words = w2v.most_similar(word.lower())
      heading = f'Words Most Similar to {word.title()}  '
      formatted = [f'{x[0].title()} - {round(x[1], 3)}  ' for x in similar_words]
      head_and_list = [dcc.Markdown([heading]), dcc.Markdown(formatted)]
      return head_and_list
    except:
      return 'Sorry, that word or phrase is not in the vocabulary'

# @app.callback(Output(component_id="w2v-output-2", component_property="children"),
#               [Input(component_id="w2v-submit-button-2", component_property="n_clicks"),
#               Input(component_id="w2v-text-bar-2", component_property="n_submit"),
#               Input(component_id='w2v-selection-2', component_property='value')],
#               [State(component_id="w2v-text-bar-2", component_property="value")])
# def generate_similarity_2(n_clicks, n_submit, source_selection, word):
#   # with open('w2v.pkl', 'rb') as w2v_d:
#   #   w2v_dict = pickle.load(w2v_d)
#   w2v = KeyedVectors.load(f'w2v_models/{source_selection}_w2v.wordvectors')
#   if n_clicks < 1 and n_submit < 1:
#     return None
#   else:
#     try:
#       similar_words = w2v.most_similar(word.lower())
#       heading = f'Words Most Similar to {word.title()}  '
#       formatted = [f'{x[0].title()} - {round(x[1], 3)}  ' for x in similar_words]
#       head_and_list = [dcc.Markdown([heading]), dcc.Markdown(formatted)]
#       return head_and_list
#     except:
#       return 'Sorry, that word or phrase is not in the vocabulary'

# @app.callback(Output(component_id="w2v-output-3", component_property="children"),
#               [Input(component_id="w2v-submit-button-3", component_property="n_clicks"),
#               Input(component_id="w2v-text-bar-3", component_property="n_submit"),
#               Input(component_id='w2v-selection-3', component_property='value')],
#               [State(component_id="w2v-text-bar-3", component_property="value")])
# def generate_similarity_3(n_clicks, n_submit, source_selection, word):
#   w2v = KeyedVectors.load(f'w2v_models/{source_selection}_w2v.wordvectors')
#   if n_clicks < 1 and n_submit < 1:
#     return None
#   else:
#     try:
#       similar_words = w2v.most_similar(word.lower())
#       heading = f'Words Most Similar to {word.title()}  '
#       formatted = [f'{x[0].title()} - {round(x[1], 3)}  ' for x in similar_words]
#       head_and_list = [dcc.Markdown([heading]), dcc.Markdown(formatted)]
#       return head_and_list
#     except:
#       return 'Sorry, that word or phrase is not in the vocabulary'


server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)