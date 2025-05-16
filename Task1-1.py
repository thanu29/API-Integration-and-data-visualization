import requests # fetch the data from web servers i.e HTTP

# Fetch the data using HealthCare.gov API
req = requests.get('https://www.healthcare.gov/api/index.json')

# Check if the request was successful
if req.status_code == 200:
    data = req.json()  # Parse JSON response
    print(data)             # Display the fetched data
else:
    print(f"Failed to fetch data. Status code: {req.status_code}")
