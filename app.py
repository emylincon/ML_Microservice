from flask import Flask, jsonify, request
from tensorflow import keras
import numpy as np
import json

app = Flask(__name__)


class TimeSeriesPredict:
    def __init__(self):
        self.model = keras.models.load_model('model/lstm_model.h5')
        self.shape = (1, 10, 1)
        self.last_input = np.array([[1, 0, 1] + [0] * 7]).reshape(1, 10, 1)

    def data_prepare(self, my_input):
        return np.array([my_input]).reshape(*self.shape)

    def get_output(self, last_input):
        raw_prediction = self.model.predict(self.data_prepare(last_input))
        prediction = list(raw_prediction[0])
        return [round(i) for i in prediction]

# a = TimeSeriesPredict().get_output([0] * 10)
# print(a)


Predictor = TimeSeriesPredict()


@app.route('/')
def index():
    return jsonify({'msg': 'Welcome to age and gender Time series Predictor Microservice'}), 200


@app.route('/predict',  methods=["POST", "GET"])
def predict():
    # float(request.args.get('temperature')), humidity=float(request.args.get('humidity'))
    obj = request.get_json()
    last = json.loads(obj)['last']
    output = Predictor.get_output(last)
    return jsonify({'next': output}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
