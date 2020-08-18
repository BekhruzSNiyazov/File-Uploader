from flask import Flask, request, redirect
import pyrebase

app = Flask(__name__)

config = {
	"apiKey": "AIzaSyCn_EXyZysUSuhD4nvWtFCSC05c9eT5rGc",
	"authDomain": "image-upload-74c76.firebaseapp.com",
	"databaseURL": "https://image-upload-74c76.firebaseio.com",
	"projectId": "image-upload-74c76",
	"storageBucket": "image-upload-74c76.appspot.com",
	"messagingSenderId": "413560089163",
	"appId": "1:413560089163:web:94d48cad9693507af0bbce",
	"measurementId": "G-42E0S384TL"
}
firebase = pyrebase.initialize_app(config=config)
storage = firebase.storage()

@app.route("/", methods=["POST", "GET"])
def index():
    return """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Upload a File</title>
</head>
<body>
	<h1>Upload a File</h1>
	<form method="POST" enctype="multipart/form-data" action="/upload">
		<input type="file" name="file">
		<button type="submit">Upload</button>
	</form>
</body>
</html>"""

@app.route("/upload", methods=["POST", "GET"])
def uupload():
    if "file" not in request.files:
        print("File upload error")
        return redirect("/")
    file = request.files["file"]
    storage.child("/" + file.filename).put(file)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
