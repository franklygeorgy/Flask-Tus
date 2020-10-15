# A local directory - "uploads" must be present for this demo to work
#
from flask import Flask, render_template, send_from_directory, current_app
from flask_tus_cont import TusManager

import os

app = Flask(__name__)
tm = TusManager(app, upload_url='/file-upload')


@app.route("/")
def demo():
	return render_template("demo.html", upload_url = tm.upload_url )

# serve the uploaded files
@app.route('/uploads/<path:filename>', methods=['GET'])
def download(filename):
	uploads = os.path('./uploads')
	return send_from_directory(directory=uploads, filename=filename)

if __name__ == '__main__':
  app.run( host='0.0.0.0', debug=True )

