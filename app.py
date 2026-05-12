from flask import Flask, render_template, request
from yt_dlp import YoutubeDL
import threading
import os

app = Flask(__name__)

# Create downloads folder automatically
os.makedirs("downloads", exist_ok=True)

# Function to download single video
def download_video(link):

    options = {
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }

    with YoutubeDL(options) as ydl:
        ydl.download([link])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():

    data = request.form['links']

    # Clean links properly
    links = [l.strip() for l in data.split('\n') if l.strip()]

    threads = []

    for link in links:

        thread = threading.Thread(
            target=download_video,
            args=(link,)
        )

        thread.daemon = True   # IMPORTANT FIX (prevents freezing)
        threads.append(thread)

        thread.start()

    # ❌ REMOVED thread.join() completely (THIS WAS THE PROBLEM)

    return "Downloads started successfully! Check downloads folder."


if __name__ == '__main__':
    app.run(debug=True, threaded=True)