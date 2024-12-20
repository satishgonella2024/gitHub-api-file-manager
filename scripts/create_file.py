import base64
from utils import github_api_request

def create_file(path, content, message):
    encoded_content = base64.b64encode(content.encode()).decode()
    payload = {
        "message": message,
        "content": encoded_content,
        "branch": "main"
    }
    response = github_api_request(f"contents/{path}", "PUT", payload)
    return response

if __name__ == "__main__":
    file_path = "src/config/app/settings.json"
    file_content = '{"key": "value"}'
    commit_message = "Create settings.json in nested path"
    result = create_file(file_path, file_content, commit_message)
    print(result)