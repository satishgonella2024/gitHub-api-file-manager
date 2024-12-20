from utils import github_api_request

def retrieve_file(path):
    response = github_api_request(f"contents/{path}", "GET")
    return response

if __name__ == "__main__":
    file_path = "src/config/app/settings.json"
    file_info = retrieve_file(file_path)
    print(f"File SHA: {file_info['sha']}")
    print(f"File Content (Base64): {file_info['content']}")