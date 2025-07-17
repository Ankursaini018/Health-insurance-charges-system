from flask import Flask, render_template, request, redirect, url_for, flash
import joblib
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

MODEL_PATH = 'model.joblib'
HISTORY_CSV = 'prediction_history.csv'

# Load the trained model
model = joblib.load(MODEL_PATH)

# Helper: Save prediction to history
def save_history(data):
    df = pd.DataFrame([data])
    if os.path.exists(HISTORY_CSV):
        df.to_csv(HISTORY_CSV, mode='a', header=False, index=False)
    else:
        df.to_csv(HISTORY_CSV, mode='w', header=True, index=False)

# Helper: Load prediction history
def load_history():
    if os.path.exists(HISTORY_CSV):
        df = pd.read_csv(HISTORY_CSV)
        return df.to_dict(orient='records')[::-1]  # Most recent first
    return []

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get form data
        age = int(request.form['age'])
        sex = request.form['sex']
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = request.form['smoker']
        # Encode categorical variables
        sex_dict = {'female': 1, 'male': 2}
        smoker_dict = {'no': 1, 'yes': 2}
        input_df = pd.DataFrame({
            'age': [age],
            'sex': [sex_dict[sex]],
            'bmi': [bmi],
            'children': [children],
            'smoker': [smoker_dict[smoker]]
        })
        # Predict
        premium = model.predict(input_df)[0]
        prediction = f"{premium:,.2f}"
        # Save to history
        save_history({
            'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'age': age,
            'sex': sex,
            'bmi': bmi,
            'children': children,
            'smoker': smoker,
            'premium': prediction
        })
    return render_template('index.html', prediction=prediction)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project', methods=['GET', 'POST'])
def project():
    prediction = None
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = request.form['sex']
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = request.form['smoker']
        # Encode categorical variables
        sex_dict = {'female': 1, 'male': 2}
        smoker_dict = {'no': 1, 'yes': 2}
        input_df = pd.DataFrame({
            'age': [age],
            'sex': [sex_dict[sex]],
            'bmi': [bmi],
            'children': [children],
            'smoker': [smoker_dict[smoker]]
        })
        premium = model.predict(input_df)[0]
        prediction = f"{premium:,.2f}"
    return render_template('project.html', prediction=prediction)

@app.route('/history')
def history():
    history = load_history()
    return render_template('history.html', history=history)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success = False
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # For demo: just flash a message, or you could save to a file/db
        flash('Thank you for contacting us!')
        success = True
    return render_template('contact.html', success=success)

if __name__ == '__main__':
    app.run(debug=True)
