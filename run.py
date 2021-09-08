import os

from app import app

port = int(os.environ.get("FLASK_PORT", 5000))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)