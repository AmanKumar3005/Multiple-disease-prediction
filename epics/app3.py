import pickle
import numpy as np
from flask import Flask, request, render_template, redirect

app = Flask(__name__,template_folder='templates')

# Load the model
with open('svm_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the symptom index dictionary
with open('symptom_index.pkl', 'rb') as f:
    symptom_index = pickle.load(f)

# Load the predictions classes
with open('predictions_classes.pkl', 'rb') as f:
    predictions_classes = pickle.load(f)

@app.route('/')
def home():
    return render_template('epics/Frontend page/index.html')

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form
    username = request.form['username']
    password = request.form['password']

    # Perform authentication or other desired operations
    # You can add your own logic here

    # Redirect to symptom input page after successful login
    return redirect('/symptoms')

@app.route('/symptoms')
def symptoms():
    return render_template('symptoms.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the symptoms from the form
    symptom1 = request.form['symptom1']
    symptom2 = request.form['symptom2']
    symptom3 = request.form['symptom3']

    # Create the input data for the model
    input_data = [0] * len(symptom_index)
    input_data[symptom_index[symptom1]] = 1
    input_data[symptom_index[symptom2]] = 1
    input_data[symptom_index[symptom3]] = 1
    input_data = np.array(input_data).reshape(1, -1)

    # Generate the prediction
    prediction = predictions_classes[model.predict(input_data)[0]]

    # Pass the prediction to the frontend
    return render_template('symptoms.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
