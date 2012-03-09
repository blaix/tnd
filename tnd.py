from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def game():

  return render_template("game.html")

if __name__ == "__main__":
  app.debug = True
  app.run()
