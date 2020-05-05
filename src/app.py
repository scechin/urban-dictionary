import requests, os

# Retrieve your API credentials from the .env file
if os.getenv("API_KEY") is None or os.getenv("API_KEY") == "":
    print("ERROR! Make sure you have created your .env file with your API credentials (look for the .evn.example as an example and replace it with your own API credentials that you got from RapidAPI)")
    exit(1)

# Get credentials from the .env file
API_HOST = os.getenv("API_HOST")
API_KEY = os.getenv("API_KEY")

# continue with your application here
#import requests

#querystring = {"term":"wat"}
term = input("What word are you looking for?")
headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "cedaa06fa5mshba41d17e1cd8779p13246bjsn7f0823653c3b"
    }

response = requests.get(API_HOST+"/define?term="+term, headers=headers)
body = response.json()
print(body)
