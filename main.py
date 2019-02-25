import db
import flask 
import json

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def healthCheck():
    return flask.jsonify([])

@app.route('/happenings', methods=['GET'])
def read_happenings():
    print('backend service responding to request for happenings')
    # string is default to prevent error when jsonifying python datetime
    return json.dumps(db.get_happenings(), indent=4, sort_keys=True, default=str), 200

@app.route('/happenings/add/<id>', methods=['POST'])
def create_happening(id):
    print('backend service adding new happening')
    data = flask.request.form.to_dict(flat=True)
    doc = db.add_happening(data, id)
    return flask.jsonify({ 'id': doc }), 201

@app.route("/happening/like/<id>")
def like(id):
    print('backend service adding like to happening')
    return flask.jsonify({ 'likes': db.like_happening(id) }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)

