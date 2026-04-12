# Author: Philip Cullen
# assignment04-github.py

# This program takes file from a repository and replace each instance of the word "Andrew" with "Philip"
# The repository is located in an encrypted file and therefore an API key is required to access the files within the repository
# The API key is stored within a file labelled config

from github import Github, Auth
from config import config as cfg  # API key is stored securely here
import base64

# 1. Load API key from config.py
apiKey = cfg["githubkey"]

# 2. Connect to GitHub
g = Github(auth=Auth.Token(apiKey))

# 3. Select repository
repo_name = "philipcullen93/aprivateone"  # change if different
repo = g.get_repo(repo_name)

# 4. Define file to modify
file_path = "test.txt"  # make sure this exists in repo root
your_name = "Philip"    # replace with your name

try:
    # 5. Try to get the file content
    file_content = repo.get_contents(file_path)
    content_str = file_content.decoded_content.decode("utf-8")
    print(f"Original file content:\n{content_str}\n")

except Exception as e:
    # 6. If file doesn't exist, create it
    print(f"{file_path} not found. Creating a new file.")
    content_str = ""
    file_content = None

# 7. Replace all instances of "Andrew" with your name
new_content_str = content_str.replace("Andrew", your_name)

# 8. Commit the changes
commit_message = f"Replace 'Andrew' with {your_name}"
if file_content:  # file exists, update it
    repo.update_file(
        path=file_path,
        message=commit_message,
        content=new_content_str,
        sha=file_content.sha
    )
else:  # file did not exist, create it
    repo.create_file(
        path=file_path,
        message=commit_message,
        content=new_content_str
    )

print(f"Updated {file_path} and pushed changes to {repo_name}!")