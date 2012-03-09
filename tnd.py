from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Tiles and Dudes! Are you Robot or Samurai?"

if __name__ == "__main__":
    app.run()
