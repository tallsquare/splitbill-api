from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Testing home page'

app.run(port=5000, debug=True)