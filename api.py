import flask
from flask_cors import CORS
import json
import storage

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/trends/<last_x_hours>', methods=['GET'])
def get_trends(last_x_hours):
    last_x_hours = int(last_x_hours)
    return json.dumps(storage.getTrends(last_x_hours=last_x_hours))


app.run()
