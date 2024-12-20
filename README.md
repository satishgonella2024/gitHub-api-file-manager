# **GitHub API File Manager**

The **GitHub API File Manager** is a Python-based project for interacting with the GitHub API to perform common file management operations, such as creating, updating, retrieving, and deleting files in a repository. This tool demonstrates the power of the GitHub REST API for managing repository content.

---

## **Features**
- **Create a File**: Add a file at any path, including nested directories.
- **Update a File**: Modify the content of an existing file.
- **Retrieve a File**: Fetch details such as SHA and content of a file.
- **Delete a File**: Remove a file from the repository.

---

## **Project Structure**
```
github-api-file-manager/
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── scripts/
    ├── create_file.py      # Script to create a file
    ├── update_file.py      # Script to update a file
    ├── retreive_file.py    # Script to retrieve file details
    ├── delete_file.py      # Script to delete a file
    └── utils.py            # Helper functions for API requests
```

---

## **Detailed Sample: Using the GitHub API with Nested Paths**

This detailed sample will walk through four common use cases for creating, updating, and deleting files with nested paths using the GitHub REST API.

### **Use Case 1: Create a File in a Nested Path**
**Scenario**: You want to add a configuration file named `settings.json` inside the nested directory `src/config/app` in your repository.

**Steps**:
1. Ensure the parent directories (`src/config/app`) exist.
2. Specify the nested `path` parameter for the file as `src/config/app/settings.json`.
3. Provide the file content in Base64 format.

**cURL Command**:
```bash
curl -X PUT -H "Authorization: token YOUR_PERSONAL_ACCESS_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/contents/src/config/app/settings.json \
  -d '{
    "message": "Add settings.json with app configuration",
    "content": "eyJrZXkiOiAidmFsdWUifQ==", 
    "branch": "main"
  }'
```

---

### **Use Case 2: Update an Existing File in a Nested Path**
**Scenario**: You need to update the `settings.json` file in the `src/config/app` directory with new content.

**Steps**:
1. Retrieve the current `sha` of the file using the [GET `/repos/{owner}/{repo}/contents/{path}`](https://docs.github.com/en/rest/repos/contents#get-repository-content) API.
2. Use the retrieved `sha` in the update request.

**Retrieve the SHA**:
```bash
curl -H "Authorization: token YOUR_PERSONAL_ACCESS_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/contents/src/config/app/settings.json
```

**Update the File**:
```bash
curl -X PUT -H "Authorization: token YOUR_PERSONAL_ACCESS_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/contents/src/config/app/settings.json \
  -d '{
    "message": "Update settings.json with new content",
    "content": "eyJuZXdfa2V5IjogIm5ld192YWx1ZSJ9", 
    "branch": "main",
    "sha": "abc12345def67890..."
  }'
```

---

### **Use Case 3: Handle Nonexistent Nested Directories**
**Scenario**: The directory `src/config/app` does not exist, but you want to create a new file `settings.json` inside it.

**Solution**:
You don’t need to explicitly create directories. GitHub implicitly creates the necessary directory structure when you add a file.

---

### **Use Case 4: Delete a File in a Nested Path**
**Scenario**: You need to delete the `settings.json` file from the `src/config/app` directory.

**Steps**:
1. Retrieve the current `sha` of the file using the GET API call.
2. Use the DELETE API to remove the file.

---

### **Summary Table of Operations**

| **Operation**        | **API Endpoint**                                                      | **Required Data**                                                                 |
|-----------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Create a file         | `PUT /repos/{owner}/{repo}/contents/{path}`                         | `path`, `message`, `content`, `branch`                                           |
| Update a file         | `PUT /repos/{owner}/{repo}/contents/{path}`                         | `path`, `message`, `content`, `branch`, `sha`                                    |
| Retrieve file info    | `GET /repos/{owner}/{repo}/contents/{path}`                         | `path`                                                                           |
| Delete a file         | `DELETE /repos/{owner}/{repo}/contents/{path}`                      | `path`, `message`, `sha`, `branch`                                              |

---

## **Setup**

### 1. Clone the Repository
```bash
git clone git@github.com:satishgonella2024/github-api-file-manager.git
cd github-api-file-manager
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
```plaintext
GITHUB_TOKEN=<your_personal_access_token>
REPO_OWNER=<your_github_username>
REPO_NAME=<your_repository_name>
BRANCH=main
```

---