from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Get the absolute path to the data file
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
