from app import app
from flask import render_template, redirect
from app.forms import ShortyForm
import requests


@app.route('/index', methods=['GET', 'POST'])
def index():
    api_location = 'http://127.0.0.1:6000/new/'
    my_location = 'http://127.0.0.1:5000/'
    form = ShortyForm()

    if form.validate_on_submit():
        code = requests.get(api_location+form.url.data).json()
        final = my_location+str(code)
        return render_template('result.html', coded_url=final)

    return render_template('main.html', form=form)


@app.route('/<code>', methods=['GET'])
def forward(code):
    api_location = 'http://127.0.0.1:6000/find/'
    link = requests.get(api_location+code).json()
    return redirect('http://'+link)
