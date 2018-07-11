from flask import Flask, Blueprint
sample_page = Blueprint('sample_page', __name__, template_folder='templates')
@sample_page.route('/hello/<page>')
def show(page):
    return page