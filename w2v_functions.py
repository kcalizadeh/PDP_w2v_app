import json
from gensim.models import KeyedVectors

def get_dropdown_list_w2v():
    dropdown_list = [
            {'label': 'All Texts', 'value': 'general'},
            {'label': 'Analytic', 'value': 'analytic'},
            {'label': 'Aristotle', 'value': 'aristotle'},
            {'label': 'Berkeley', 'value': 'Berkeley'},
            {'label': 'Capitalism', 'value': 'capitalism'},
            {'label': 'Communism', 'value': 'communism'},
            {'label': 'Continental', 'value': 'continental'},
            {'label': 'Deleuze', 'value': 'Deleuze'},
            {'label': 'Derrida', 'value': 'Derrida'},
            {'label': 'Descartes', 'value': 'Descartes'},
            {'label': 'Empiricism', 'value': 'empiricism'},
            {'label': 'Everyday English', 'value': 'everyday'},
            {'label': 'Fichte', 'value': 'Fichte'},
            {'label': 'Foucault', 'value': 'Foucault'},
            {'label': 'German Idealism', 'value': 'german_idealism'},
            {'label': 'Hegel', 'value': 'Hegel'},
            {'label': 'Heidegger', 'value': 'Heidegger'},            
            {'label': 'Hume', 'value': 'Hume'},
            {'label': 'Husserl', 'value': 'Husserl'},
            {'label': 'Kant', 'value': 'Kant'},
            {'label': 'Keynes', 'value': 'Keynes'},
            {'label': 'Kripke', 'value': 'Kripke'},
            {'label': 'Leibniz', 'value': 'Leibniz'},
            {'label': 'Lenin', 'value': 'Lenin'},
            {'label': 'Lewis', 'value': 'Lewis'},
            {'label': 'Locke', 'value': 'Locke'},
            {'label': 'Malebranche', 'value': 'Malebranche'},
            {'label': 'Marx', 'value': 'Marx'},
            {'label': 'Merleau-Ponty', 'value': 'Merleau-Ponty'},
            {'label': 'Moore', 'value': 'Moore'},
            {'label': 'Phenomenology', 'value': 'phenomenology'},
            {'label': 'Plato', 'value': 'plato'},
            {'label': 'Popper', 'value': 'Popper'},
            {'label': 'Quine', 'value': 'Quine'},
            {'label': 'Rationalism', 'value': 'rationalism'},
            {'label': 'Ricardo', 'value': 'Ricardo'},
            {'label': 'Russell', 'value': 'Russell'},
            {'label': 'Smith', 'value': 'Smith'},
            {'label': 'Spinoza', 'value': 'Spinoza'},
            {'label': 'Wittgenstein', 'value': 'Wittgenstein'},
            
      ]
    return dropdown_list


# def get_keys(path):
#     with open(path) as f:
#         return json.load(f)

# def get_w2v(input):
#     w2v = KeyedVectors.load(f'https://philosophydata.s3-us-west-1.amazonaws.com/w2v_models/{input}_w2v.wordvectors')
#     return w2v
