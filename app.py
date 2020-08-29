import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction.round(decimals=2)

    return render_template('main.html', prediction_text='Bleep bloop... home price predicted to be ${}'.format(output))

@app.route('/visualizations')
def visualizations():    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)