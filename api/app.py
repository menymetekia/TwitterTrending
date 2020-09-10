import flask
from flask_cors import CORS
import json
from storage_utils import storage

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

collection = storage.initialize_db()

@app.route('/trends/<last_x_hours>', methods=['GET'])
def get_trends(last_x_hours):
    """Get the trends for the given last couple of hours"""
    last_x_hours = int(last_x_hours)
    return json.dumps(storage.getTrends(collection, last_x_hours=last_x_hours))


app.run()
