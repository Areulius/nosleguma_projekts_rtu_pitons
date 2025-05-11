from flask import Flask, render_template
import json
from functions.functions import *

app = Flask(__name__)

@app.route('/')
def index():
    posts = load_from_file("posts.txt")
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)