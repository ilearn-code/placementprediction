from flask import Flask, request, jsonify
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


@app.route('/predict', methods=['POST'])
def predict():
    cgpa = request.form.get('cgpa')
    iq = request.form.get('iq')
    profile_score = request.form.get('profile_score')
    input_query = np.array([[cgpa, iq, profile_score]])
    result = model.predict(input_query)[0]
    if result==1:
        return jsonify('PLACED')
    if result ==0:
        return jsonify('NOT PLACED')


if __name__ == '__main__':
    app.run(debug=True)
