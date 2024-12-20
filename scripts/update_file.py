from utils import github_api_request

def update_file(path, new_content, message):
    # Get file SHA
    file_info = github_api_request(f"contents/{path}", "GET")
    sha = file_info["sha"]

    # Encode new content
    encoded_content = base64.b64encode(new_content.encode()).decode()

    payload = {
        "message": message,
        "content": encoded_content,
        "sha": sha,
        "branch": "main"
    }
    response = github_api_request(f"contents/{path}", "PUT", payload)
    return response

if __name__ == "__main__":
    file_path = "src/config/app/settings.json"
    new_content = '{"key": "new_value"}'
    commit_message = "Update settings.json with new content"
    result = update_file(file_path, new_content, commit_message)
    print(result)