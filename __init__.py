from flask import Flask
from api.routes import api
from view.routes import view

app = Flask(__name__)

if __name__ == "__main__":
    app.register_blueprint(api)
    app.register_blueprint(view)
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
