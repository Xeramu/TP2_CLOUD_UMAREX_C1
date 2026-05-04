from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

nama = os.getenv("NAMA", "Unknown")
nim = os.getenv("NIM", "000000")

playlist_data = {
    "nama_musik": "Playlist Favorite",
    "nama": nama,
    "nim": nim,
    "musik": [
        "Self Esteem - The Offspring",
        "House of the Rising Sun - The Animals",
        "Still Got the Blues - Gary Moore"
    ]
}

@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify(playlist_data)

@app.route('/api/add-musik', methods=['POST'])
def add_menu():
    new_item = request.json.get('item')
    if new_item:
        playlist_data["musik"].append(new_item)
        return jsonify({"message": "Musik berhasil ditambah!", "musik": playlist_data["musik"]}), 201
    return jsonify({"error": "Data tidak valid"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)