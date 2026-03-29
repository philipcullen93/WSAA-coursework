import requests
import json
from config import config as cfg

# Load API key from config.py
apiKey = cfg["githubkey"]

# URL of your private repo
url = 'https://api.github.com/repos/philipcullen93/aprivateone'

# Request using auth
response = requests.get(url, auth=('token', apiKey))

# Check response
if response.status_code == 200:
    repoJSON = response.json()
    # Save JSON to file
    with open("repo_info.json", "w") as fp:
        json.dump(repoJSON, fp, indent=4)
    print("Repo information saved to repo_info.json")
else:
    print(f"Error {response.status_code}: {response.text}")