# **GitHub API File Manager**

Welcome to the **GitHub API File Manager**, a powerful Python-based tool that leverages the GitHub REST API to manage repository content and streamline collaboration. From file operations to automating pull requests, this project showcases the versatility of the GitHub API.

---

## **✨ Features**

- **📁 Create a File**: Add files at any location, including nested directories.
- **✏️ Update a File**: Modify the content of existing files.
- **🔍 Retrieve a File**: Fetch details such as SHA and file content.
- **🗑️ Delete a File**: Remove files from the repository.
- **🚀 Create a Pull Request**: Automate pull requests to merge feature branches seamlessly.
- **⚙️ GitHub Actions**: Automate CI/CD workflows directly within this project.

---

## **📂 Project Structure**

```
github-api-file-manager/
├── .github/workflows/    # GitHub Actions workflows
│   ├── file-manager.yml  # CI/CD workflow for file manager scripts
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── scripts/
│   ├── create_file.py    # Script to create a file
│   ├── update_file.py    # Script to update a file
│   ├── retreive_file.py  # Script to retrieve file details
│   ├── delete_file.py    # Script to delete a file
│   ├── create_pull_request.py  # Script to create a pull request
│   └── utils.py          # Helper functions for API requests
└── src/
    └── config/
        └── app/
            └── settings.json   # Example file in a nested directory
```

---

## **🚀 Detailed Sample: Using the GitHub API with Nested Paths**

### **Use Case 1: Create a File in a Nested Path**

**Scenario**: Add a configuration file named `settings.json` inside the directory `src/config/app`.

**Steps**:

1. Ensure the parent directories (`src/config/app`) exist.
2. Specify the nested `path` as `src/config/app/settings.json`.
3. Encode the file content in Base64.

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

**Scenario**: Update the `settings.json` file in `src/config/app` with new content.

**Steps**:

1. Retrieve the current `sha` of the file using the [GET API](https://docs.github.com/en/rest/repos/contents#get-repository-content).
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

**Scenario**: Add a file `settings.json` in a non-existent directory `src/config/app`.

**Solution**: No need to explicitly create directories. GitHub implicitly creates the necessary directory structure when you add a file.

---

### **Use Case 4: Delete a File in a Nested Path**

**Scenario**: Delete the `settings.json` file from `src/config/app`.

**Steps**:

1. Retrieve the current `sha` of the file using the GET API.
2. Use the DELETE API to remove the file.

---

### **Use Case 5: Create a Pull Request**

**Scenario**: Open a pull request to merge `feature/add-new-feature` into `main`.

**Steps**:

1. Push the feature branch to the remote repository.
2. Use the [Create Pull Request API](https://docs.github.com/en/rest/pulls/pulls#create-a-pull-request).

**cURL Command**:

```bash
curl -X POST -H "Authorization: token YOUR_PERSONAL_ACCESS_TOKEN" \
     -H "Accept: application/vnd.github+json" \
     https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/pulls \
     -d '{
       "title": "Add new feature",
       "head": "feature/add-new-feature",
       "base": "main",
       "body": "This PR adds a new feature to the project. Please review."
     }'
```

---

## **📜 Summary Table of Operations**

| **Operation**                | **API Endpoint**                               | **Required Data**                             |
| ---------------------------- | ---------------------------------------------- | --------------------------------------------- |
| **🆕 Create a file**         | `PUT /repos/{owner}/{repo}/contents/{path}`    | `path`, `message`, `content`, `branch`        |
| **✏️ Update a file**         | `PUT /repos/{owner}/{repo}/contents/{path}`    | `path`, `message`, `content`, `branch`, `sha` |
| **🔍 Retrieve file info**    | `GET /repos/{owner}/{repo}/contents/{path}`    | `path`                                        |
| **🗑️ Delete a file**        | `DELETE /repos/{owner}/{repo}/contents/{path}` | `path`, `message`, `sha`, `branch`            |
| **🚀 Create a Pull Request** | `POST /repos/{owner}/{repo}/pulls`             | `title`, `head`, `base`, `body`               |

---

## **⚙️ Setup**

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

## **⚡ Automating with GitHub Actions**

### **CI/CD Workflow: file-manager.yml**

The project includes a GitHub Actions workflow to automate testing and integration.

**File: `.github/workflows/file-manager.yml`**

```yaml
name: File Manager CI/CD

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Run tests
      run: |
        python -m unittest discover -s tests
```

This workflow ensures code quality and reliability by running tests on every push or pull request.

---

## **🌟 Start Contributing**

Feel free to contribute to this project by adding new features, improving existing scripts, or reporting issues. Your contributions are welcome!

---

**Happy Coding!** 🚀

