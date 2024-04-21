from flask import Flask, request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html', title="Home")

@app.get('/download')
def download():
   url = request.args.get('url', default="")
   if url == "":
      url = "empty"
   return url

if __name__ == "__main__":
  app.run(debug=True)

