from flask import Flask

app = Flask(__name__)
# You're creating a website object and saving it in the variable app.

@app.route("/")
# This means:"When someone visits the homepage, run the function below."(The / means the home page.)

def home():
    return """
    # Everything inside the triple quotes is sent to the browser.(returning HTML)

    <h1>Rock Paper Scissors</h1>

    <a href="/play/Rock">
        <button>Rock</button>
    </a>

    <a href="/play/Paper">
        <button>Paper</button>
    </a>

    <a href="/play/Scissors">
        <button>Scissors</button>
    </a>
    """

from rockpapersci1 import RockPaperScissors

@app.route("/play/<choice>")
def play(choice):
    result, computer = RockPaperScissors(choice)
    return f"""
    <h1>{result}</h1>
    <h2>You have {choice} while your enermy has {computer} </h2>
    <a href="/">
      <button>Play Again?</button>
    </a>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0")