from flask import Flask, render_template, request
import os
from model.model import match_resume

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

@app.route("/", methods=["GET", "POST"])
def index():
    results = []

    if request.method == "POST":
        files = request.files.getlist("resumes")
        job_desc = request.form["job"]

        for file in files:
            if file and file.filename != "":
                path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(path)

                result = match_resume(path, job_desc)
                result["name"] = file.filename

                results.append(result)

        results = sorted(results, key=lambda x: x["score"], reverse=True)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)