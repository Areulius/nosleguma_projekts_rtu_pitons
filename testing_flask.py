from flask import Flask, render_template
import json

app = Flask(__name__)

def load_from_file():
    all_items = []
    with open("posts.txt", "r", encoding="utf-8") as f:
        for line in f:
            all_items.append(json.loads(line))
    return all_items

@app.route('/')
def index():
    posts = load_from_file()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    saved_items = load_from_file()
    app.run(debug=True)