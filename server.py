from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# dữ liệu lưu tạm
data_store = {
    "temperature": 0,
    "object_count": 0
}

@app.route('/update', methods=['POST'])
def update_data():
    global data_store
    data = request.json
    
    data_store["temperature"] = data.get("temperature", 0)
    data_store["object_count"] = data.get("object_count", 0)
    
    return jsonify({"status": "updated"})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)