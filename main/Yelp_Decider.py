# Dependencies
import requests
import json

# Yelp developer API key
from config import ykey

# Counter for number of users
users = int(input("How many people are choosing: "))

# Base URL
base_url = "https://api.yelp.com/v3/businesses/search"

# Parameter definitions
# If statements for price index
target_price = str(input("How much do you want to spend (1-4, low to high): "))
if target_price == "4":
    target_price = "1,2,3,4"
elif target_price == "3":
    target_price = "1,2,3"
elif target_price == "2":
    target_price = "1,2"
else :
    target_price = "1"

target_location = str(input("Enter your city: "))
target_radius = (int(input("How far are you willing to drive (number of miles): ")))*1609
target_category = (str(input("What kind of cuisine are you craving?: "))).lower()

# Parameters for URL
params = {
    "location": target_location,
    "radius": target_radius,
    "price": target_price,
    "categories": target_category,
    "term": "restaurants",
}

# Authentification
headers= {"Authorization": "bearer %s" % ykey}

# Run request and convert to JSON
response = requests.get(url=base_url, params=params, headers=headers)
print(response)
results = response.json()

# Pretty print JSON
print(json.dumps(results, indent=4, sort_keys=True))