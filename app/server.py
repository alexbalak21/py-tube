from flask import Flask, request, send_from_directory, after_this_request
from flask import render_template
from downloader.main import download_convert
import os
import time


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html', title="Home")

@app.get('/convert')
def request_convert():
   url = request.args.get('url', default="")
   if url == "":
      url = "empty"
      return url
   else:
      audio_file = download_convert(url)
      return render_template("download.html", link=f'download/{audio_file}.mp3', name=audio_file)

@app.route('/download/<file_name>')
def download_file(file_name):
  file_path = "./audio/" + file_name
  @after_this_request
  def afetr_request(response):
    print("FILE DOWNLADED")
    return response
  return send_from_directory('audio', file_name)

@app.route('/test')
def test():
   return render_template("test.html")

if __name__ == "__main__":
  app.run(debug=True)

