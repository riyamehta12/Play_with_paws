from flask import Flask, request, render_template, redirect
import pandas as pd
import os

app = Flask(__name__)

# Excel file where the data will be saved
EXCEL_FILE = "form_data.xlsx"

@app.route('/')
def index():
    return render_template('form.html')  # Renders the HTML form

@app.route('/save-data', methods=['POST'])
def save_data():
    # Get the form data from the POST request
    full_name = request.form['full_name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    living_situation = request.form['living_situation']
    experience = request.form['experience']
    age_group = request.form['age_group']
    size = request.form['size']
    gender = request.form['gender']
    breed = request.form['breed']
    street_address = request.form['street_address']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']

    # Check if the Excel file exists, if not, create it
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
    else:
        df = pd.DataFrame(columns=['Full Name', 'Email', 'Phone Number', 'Living Situation', 
                                   'Experience', 'Age Group', 'Size', 'Gender', 'Breed', 
                                   'Street Address', 'City', 'State', 'Zip Code'])

    # Add new row of data
    new_data = pd.DataFrame({
        'Full Name': [full_name],
        'Email': [email],
        'Phone Number': [phone_number],
        'Living Situation': [living_situation],
        'Experience': [experience],
        'Age Group': [age_group],
        'Size': [size],
        'Gender': [gender],
        'Breed': [breed],
        'Street Address': [street_address],
        'City': [city],
        'State': [state],
        'Zip Code': [zip_code]
    })

    # Append new data to the existing Excel file
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False)

    return redirect('/')  # Redirect back to the form page after submission

if __name__ == '__main__':
    app.run(debug=True)
