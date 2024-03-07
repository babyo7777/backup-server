from flask import Flask, request, send_file
from pytube import YouTube
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/')
def stream_audio():
    video_id = request.args.get('url')
    file_path = f"music/{video_id}.mp3"

    if video_id:
        if os.path.exists(file_path):
            # File already exists, no need to download again
            return send_file(file_path)
        else:
            try:
                yt = YouTube("https://www.youtube.com/watch?v="+str(video_id))
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_stream.download(
                    output_path="music/", filename=video_id+".mp3")
                return send_file(file_path, as_attachment=False)
            except Exception as e:
                return str(e)
    else:
        return "not found"


if __name__ == '__main__':
    app.run(debug=True)
