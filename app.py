# app.py
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello from Flask in Docker! Running on port {os.environ.get('FLASK_RUN_PORT', '5000')}"

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port) 
