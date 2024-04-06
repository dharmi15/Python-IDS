import requests
import json

# Load data from X.json
with open('X.json', 'r') as file:      
    all_data_content = json.load(file)

# Assuming X.json contains a list of dictionaries
for sample_data_content in all_data_content:
    # Prepare the data for the model
    input_data = {
        'X': [list(sample_data_content.values())]
    }

    # URL of your Flask app
    url = "http://127.0.0.1:5000/predict"

    # Send POST request
    response = requests.post(url, json=input_data, headers={"Content-Type": "application/json"})

    # Print the response JSON
    print(response.json())

    # Optional: If you want to introduce some delay between requests
    # import time
    # time.sleep(1)
