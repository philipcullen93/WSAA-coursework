from github import Github, Auth
from config import config as cfg  # import the dictionary

# Load API key
apiKey = cfg["githubkey"]

# Connect using PyGithub
g = Github(auth=Auth.Token(apiKey))

# Test: get your user info
user = g.get_user()
print(f"Logged in as: {user.login}")

# Get the repository
repo = g.get_repo("philipcullen93/aprivateone")

# Print the clone URL
print(f"Clone URL: {repo.clone_url}")

# Get the file content object
file_content = repo.get_contents("test.txt")

# Print download URL
print(f"Download URL: {file_content.download_url}")

# print(f"Logged in as: {user.login}")
# print(f"Clone URL: {repo.clone_url}")
# print(f"Download URL: {file_content.download_url}")