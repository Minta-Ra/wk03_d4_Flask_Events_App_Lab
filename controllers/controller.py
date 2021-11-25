from flask import render_template, request
from app import app

@app.route('/events')
def index():
    return render_template('index.html', title="Events")