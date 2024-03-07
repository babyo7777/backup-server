from flask import Flask, send_file, request
from pytube import YouTube
import os

app = Flask(__name__)


def download_video(video_id):
    file_path = f"music/{video_id}.mp3"

    if os.path.exists(file_path):
        # File already exists, no need to download again
        return file_path
    else:
        yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        audio_stream = yt.streams.get_audio_only().download(
            output_path="music/", filename=f"{video_id}.mp3")
        return file_path


@app.route('/s')
def stream_audio():
    video_id = request.args.get('id')
    if video_id:
        audio_file_path = download_video(video_id)
        return send_file(audio_file_path, as_attachment=False)
    else:
        return "Error: Missing 'id' parameter in the URL", 400


if __name__ == "__main__":
    app.run(debug=false)
