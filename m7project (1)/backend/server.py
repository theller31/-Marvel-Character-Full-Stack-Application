from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:YOUR_PASSWORD@localhost/marvel'
db = SQLAlchemy(app)

@app.route('/characters')
def get_characters():
    return jsonify([])

if __name__ == '__main__':
    app.run()
