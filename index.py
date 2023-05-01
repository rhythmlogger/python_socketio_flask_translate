
from flask import Flask, json, request
from flask_socketio import SocketIO
from googletrans import Translator  # pip install googletrans==3.1.0a0
from flask_cors import CORS
app = Flask(__name__)
app.config['SECRET_KEY'] = '비밀번호 설정'
socketio = SocketIO(app)
CORS(app, resources={r"/translate": {"origins": "*"}})
translator = Translator(service_urls=['translate.googleapis.com'])


@app.route('/translate', methods=['GET', 'POST'])
def summary():
    text = request.args.get('text')
    r = translator.translate(text, dest='en')
    data = {
        'result': r.text
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    socketio.run(app, debug=True)
