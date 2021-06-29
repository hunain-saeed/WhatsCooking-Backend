import route
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "Hello, World from app.py"


# Route test
app.add_url_rule('/routefunc', view_func=route.routefunc)

# Routes
app.add_url_rule('/query', view_func=route.prediction, methods=['POST'])


if __name__ == "__main__":
    app.run(debug=True)
