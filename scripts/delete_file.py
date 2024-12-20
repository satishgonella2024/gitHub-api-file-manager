from utils import github_api_request

def delete_file(path, message):
    # Get file SHA
    file_info = github_api_request(f"contents/{path}", "GET")
    sha = file_info["sha"]

    payload = {
        "message": message,
        "sha": sha,
        "branch": "main"
    }
    response = github_api_request(f"contents/{path}", "DELETE", payload)
    return response

if __name__ == "__main__":
    file_path = "src/config/app/settings.json"
    commit_message = "Delete settings.json"
    result = delete_file(file_path, commit_message)
    print(result)