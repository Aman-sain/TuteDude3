from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'message': 'Backend is running'})

@app.route('/submit', methods=['POST'])
def handle_form():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'success': False, 'message': 'Missing fields'}), 400

    print(f"🔔 Received form submission:\n  Name: {name}\n  Email: {email}")
    return jsonify({'success': True, 'message': 'Data received'})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
