from flask import Flask, jsonify ,request

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/prajwal')
def inputdata():
    try:
        return jsonify({ 'success':True,'data':"i am working fine"}) ,200
    except:
        return jsonify({'error': 'something went wrong '}), 500


if __name__ == '__main__':
    app.run()