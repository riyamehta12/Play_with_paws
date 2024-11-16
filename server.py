from flask import Flask, request, render_template

app = Flask(__name__)

# Directory to save submitted data
DATA_FILE = 'adoption_data.txt'

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/save-data', methods=['POST'])
def save_data():
    full_name = request.form['full_name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    living_situation = request.form['living_situation']
    experience = request.form['experience']
    age_group = request.form['age_group']
    size = request.form['size']
    gender = request.form['gender']
    breed = request.form.get('breed', '')  # Optional field
    street_address = request.form['street_address']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']

    # Append data to a file
    with open(DATA_FILE, 'a') as f:
        f.write(
            f"Full Name: {full_name}, Email: {email}, Phone Number: {phone_number}, "
            f"Living Situation: {living_situation}, Experience: {experience}, "
            f"Age Group: {age_group}, Size: {size}, Gender: {gender}, "
            f"Breed: {breed}, Address: {street_address}, {city}, {state}, {zip_code}\n"
        )

    return f"Thank you, {full_name}. Your data has been saved!"

if __name__ == '__main__':
    app.run(debug=True)
