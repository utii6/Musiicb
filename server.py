from flask import Flask, request, jsonify, send_from_directory
from youtubesearchpython import VideosSearch
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'يجب ادخال نص البحث'})
    try:
        videosSearch = VideosSearch(query, limit=5)
        result = videosSearch.result()
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
