# autors Valdis Arelis 231RMC177

# NESTRĀDĀ NESTRĀDĀ NESTRĀDĀ NESTRĀDĀ NESTRĀDĀ NESTRĀDĀ NESTRĀDĀ NESTRĀDĀ NESTRĀDĀ 

from flask import Flask, render_template
from functions.classes import *

POSTS_FILE = "txt_files/posts.txt"

app = Flask(__name__)
posts = PostList()

@app.route('/')
def index():
    posts.load_from_file(POSTS_FILE)
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)