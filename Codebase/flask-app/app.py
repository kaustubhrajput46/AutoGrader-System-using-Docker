from flask import Flask, render_template, request, redirect, url_for
import os
import random
from werkzeug.utils import secure_filename
import compile

app = Flask(__name__)

UPLOAD_FOLDER = '/home/ubuntu/docker-curriculum/flask-app/uploads'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/compile", methods=['POST'])
def upload_file3():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        score = compile.func()
        with open('uploads/walk.cc','r') as f:
            lineList = [line.rstrip('\r\n') for line in open('uploads/walk.cc')]
        length = len(lineList)
        return render_template("compile.html", Length = length, LineList = lineList, Score = score)
    else:
        return "Something Unexpected Occured."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug = True)
