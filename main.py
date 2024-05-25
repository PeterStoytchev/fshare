import logging
from flask import Flask, redirect

logging.basicConfig(level=logging.INFO)

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/", methods=["GET"])
def main():
    return redirect("index.html", code=302)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)