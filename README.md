# food_truck

This script should fetch data from the food truck API for the given timestamp, URL of the API and the password.
It should return printed list of the foot trucks that were active for the given timestamp.
The script uses python requests library for the fetching.
## Prerequisetes

userInput.json is mandatory. It should contain list of three parameters

1. url
2. timestamp (UNIX time format)
3. password

e.g. ["https://api.filtered.ai/q/foodtruck", "1602172800", "password"]

## Run
Next steps are required:

`pip install -r requirements.txt`
`python main.py`
