from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "LocalBot Cloud Run test — success!"
