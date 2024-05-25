import os, logging
from flask import Flask, redirect, request, flash, url_for, send_file
from werkzeug.utils import secure_filename

logging.basicConfig(level=logging.INFO)

app = Flask(__name__, static_url_path="", static_folder="static")


@app.route("/data/<file>", methods=["GET"])
def data(file):
    path = os.path.join("data", file)
    return send_file(path)

# Could have used jinja, but this is easier for now
@app.route("/list", methods=["GET"])
def list_files():
    title = "Uploaded files"


    html = f"""<!DOCTYPE html>
    <html>
        <head>
            <meta charset='utf-8'>
            <title>{title}</title>
            <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
        </head>
    <h1>{title}</h1>
    """

    for x in os.listdir("data"):
        url = url_for("data", file=x, _external=True)
        html = html + f"<a href={url}>{x}</a><br><br>"

    html = html + """
    </body>
    </html>
    """

    return html

@app.route("/", methods=["GET"])
def index():
    title = "Main menu"

    html = f"""<!DOCTYPE html>
    <html>
        <head>
            <meta charset='utf-8'>
            <title>{title}</title>
            <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
        </head>
    <h1>{title}</h1>

    <div class="upl">
    """

    html = html + f"<a href={url_for("list_files")}>Files list</a>"
    html = html + "<br><br>"
    html = html + f"<a href={url_for("upload_ui")}>Upload</a>"


    html = html + """
    </div>
    </body>
    </html>
    """

    return html

@app.route("/upload", methods=["GET"])
def upload_ui():
    return redirect("upload.html", code=302)

@app.route("/upload", methods=["POST"])
def upload_post():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
        
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join("data", filename))

        url = url_for("data", file=filename, _external=True)
        
        html = f"<a href={url}>{filename}</a>"
        html = html + "<br><br>"
        html = html + f"<a href={url_for("index")}>Main menu</a>"
        return html

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)