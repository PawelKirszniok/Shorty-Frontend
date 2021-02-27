from app import app
from flask import render_template, redirect
from app.forms import ShortyForm
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
new_location = config['PATHS']['BackendPathNew']
find_location = config['PATHS']['BackendPathFind']
self_location = config['PATHS']['SelfPath']


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():

    form = ShortyForm()

    if form.validate_on_submit():
        code = requests.get(new_location+form.url.data).json()
        final = self_location+str(code)
        return render_template('result.html', coded_url=final)

    return render_template('main.html', form=form)


@app.route('/<code>', methods=['GET'])
def forward(code):

    link = requests.get(find_location+code).json()
    if 'http' in link:
        return redirect(link)

    return redirect('http://'+str(link))
