from flask import Flask
from functions import *

app = Flask(__name__)


@app.route('/')
def print_candidates():
    return main_page(get_all())


@app.route('/candidate/<int:pk>')
def print_candidate(pk):
    return f'<img src="{get_by_pk(pk)["picture"]}">\n{main_page([get_by_pk(pk)])}'

@app.route('/skills/<skill>')
def print_skils(skill):
    return f'<pre>{main_page(get_by_skill(skill))}</pre>'


app.run()