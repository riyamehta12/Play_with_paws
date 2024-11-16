import pandas as pd
import random
import uuid

# Define possible values for each attribute
names = ['Bella', 'Max', 'Lucy', 'Charlie', 'Daisy', 'Buddy', 'Rocky', 'Molly', 'Bailey', 'Lola', 'Leo', 'Luna', 'Milo', 'Coco', 'Teddy']
sizes = ['Small', 'Medium', 'Large']
genders = ['Male', 'Female']
breeds = ['Beagle', 'Labrador', 'Pug', 'German Shepherd', 'Pomeranian', 'Bulldog', 'Shih Tzu', 'Golden Retriever', 'Boxer', 'Dalmatian']
cities = ['Delhi', 'Mumbai', 'Bangalore', 'Pune', 'Chennai', 'Hyderabad', 'Ahmedabad', 'Kolkata', 'Jaipur', 'Surat']

# Generate random data for 100 pets
num_samples = 100
data = {
    'Pet Name': [random.choice(names) for _ in range(num_samples)],
    'Unique ID': [str(uuid.uuid4())[:8] for _ in range(num_samples)], # Generating a unique 8-character ID
    'Age': [random.randint(1, 12) for _ in range(num_samples)],       # Age between 1 to 10 years
    'Size': [random.choice(sizes) for _ in range(num_samples)],
    'Gender': [random.choice(genders) for _ in range(num_samples)],
    'Breed': [random.choice(breeds) for _ in range(num_samples)],
    'City': [random.choice(cities) for _ in range(num_samples)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv('dog_dataset.csv', index=False)

print("Hypothetical dog dataset created successfully!")
print(df.head())  # Display the first few rows of the dataset
