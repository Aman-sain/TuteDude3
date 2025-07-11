from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__, template_folder='../mFrontend/templates')
app.secret_key = 'your_secret_key'  # Required for flashing messages

MONGO_URI = "mongodb+srv://aman:amanS@aman.p3ktdpe.mongodb.net/?retryWrites=true&w=majority&appName=Aman"
client = MongoClient(MONGO_URI)
db = client['your_database']
collection = db['your_collection']

@app.route('/', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        try:
            collection.insert_one({'name': name, 'email': email})
            return redirect(url_for('success'))
        except PyMongoError as e:
            flash(f"Error: {str(e)}")  
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
