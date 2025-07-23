# FastAPI Git Project

## Overview

This project demonstrates a simple FastAPI application and provides a comprehensive guide to using Git and GitHub (with GitHub Desktop) for version control and collaboration.

---

## FastAPI Application

### Features
- **GET /items/{item_id}**: Retrieve an item by its ID (path parameter, 404 error if not found).
- **GET /search/?q=...**: Search with a query parameter.
- **POST /items/**: Create an item using a Pydantic model (request body).
- **POST /upload/**: Upload a file (returns filename).
- **Error Handling**: Returns 404 for missing items.

### Running the API

**Why use a virtual environment?**  
A virtual environment keeps your project’s dependencies isolated from your global Python installation. This prevents version conflicts and makes your project easier to manage and share.

1. **Clone the repository** (see GitHub section below).
2. **Set up a virtual environment:**
   ```sh
   python -m venv fastapienv
   fastapienv\Scripts\activate  # On Windows
   source fastapienv/bin/activate  # On macOS/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the FastAPI app:**
   ```sh
   uvicorn main:app --reload
   ```
5. **Access the API docs:**
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## What is Version Control?
Version control lets you track and manage changes to your code over time. It helps individuals and teams:
- Revert to previous versions if something breaks
- Collaborate without overwriting each other's work
- Understand who made which changes and why
- Ensure reproducibility and traceability

---

## Introduction to Git
- **Distributed system**: Every developer has a full copy of the repository.
- **Snapshots, not diffs**: Git stores the state of your files at each commit.
- **Core concepts:**
  - **Repository**: The project folder tracked by Git
  - **Commit**: A snapshot of your changes
  - **Branch**: A parallel line of development
  - **Merge**: Combining changes from different branches

---

## Introduction to GitHub
- **Cloud-based hosting** for Git repositories
- Enables **collaboration**, code review, and social coding
- Provides issue tracking, pull requests, and more

---

## Introduction to GitHub Desktop
- **Why use it?**
  - Visual interface for Git commands
  - Simplifies complex workflows
  - Great for beginners and teams
- **Download & Install:** [https://desktop.github.com/](https://desktop.github.com/)
- **Authenticate** with your GitHub account after installation

---

## Creating a Repository

### Initialize a new local repo
1. Open GitHub Desktop
2. File > New Repository
3. Set the local path to your project folder
4. Click "Create Repository"

### Clone an existing repository
1. In GitHub Desktop, go to File > Clone Repository
2. Choose a repository from GitHub
3. Pick a folder to save it on your computer

---

## Git Workflow in GitHub Desktop (with FastAPI project)

### Making changes
- Edit your project files like `main.py` using your code editor.

### Staging changes
- GitHub Desktop shows you the files that changed.
- Select the files you want to include in your commit.

### Committing changes
- Write a short message like “added POST endpoint”.
- Click the button that says “Commit to main”.

### Pushing changes
- Click “Push origin” to upload your changes to GitHub.

### Pulling changes
- If others have made changes, click “Pull origin” to download them.

---

## Branching and Merging

### Why branch?
- To work on a new feature without changing the main code.
- To test something without affecting the rest of the project.

### Creating a branch
1. In GitHub Desktop, click on "Current Branch" and then "New Branch".
2. Name it something like `feature/file-upload`.

### Switching branches
- Select the branch you want to work on from the branch menu.

### Merging branches
1. Switch back to the `main` branch.
2. Go to Branch > Merge into Current Branch.
3. Select the branch you want to merge.

---

## Understanding Pull Requests

### What is a pull request?
A pull request (PR) is a way to ask others to review your code before merging it into the main branch.

### Creating a pull request
- Go to your repository on GitHub.com.
- Click on the branch you want to merge.
- Click “New Pull Request”.

### Reviewing and approving PRs
- Others can leave comments or approve your changes.
- Once ready, click “Merge Pull Request” to add it to the main branch.

---

## Stashing Changes

### What is stashing?
- Temporarily saves uncommitted changes so you can switch branches or work on something else.

### Stashing in GitHub Desktop
- Go to Branch > Stash Changes
- Later, apply or pop the stash to restore your work

---

## Basic Conflict Resolution
- Conflicts happen when two branches change the same part of a file (e.g., both edit `main.py`)
- GitHub Desktop highlights conflicts and helps you choose which changes to keep
- Edit the file to resolve the conflict, then mark as resolved in GitHub Desktop

---

## Ignoring Files with `.gitignore`
- Prevents unnecessary or sensitive files from being tracked by Git
- Common ignores for FastAPI projects:
  - `__pycache__/`
  - `fastapienv/` (your virtual environment)
  - `.env` (environment variables)
  - `*.pyc` (compiled Python files)
  - `.DS_Store` (macOS)
  - `.vscode/` (editor settings)

---

## Best Practices for Git/GitHub
- Commit frequently with clear messages (e.g., “add file upload endpoint”)
- Use branches for features and bugfixes
- Keep pull requests small and focused
- Use issues to track bugs and feature requests
- Always pull before you push to avoid conflicts

---

## Project Structure

```
fastapi_git_project/
├── .gitignore               # Configuration for Git to ignore files
├── requirements.txt         # Python package dependencies
├── main.py                  # FastAPI application
└── README.md                # Documentation
```
