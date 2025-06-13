# GitHub User Activity Tracker

A simple Python CLI tool that fetches and displays a GitHub user's recent public activity using the GitHub REST API.

## Features

- Fetches public events for any GitHub user
- Supports key event types:
  - Pushes (with commit count)
  - Issues (with accurate verb handling)
  - Pull requests
  - Stars
  - Forks
  - Branch/repo creation
- Handles invalid usernames, network errors, and GitHub rate limiting
- No dependencies — uses Python standard library only

## Usage

Run from the command line:

```bash
python main.py
```

You’ll be prompted to enter a GitHub username:

```
===== User Activity Tracker =====
> torvalds
torvalds pushed 3 commits to torvalds/linux.
torvalds opened a pull request in torvalds/linux.
...
```

## Requirements

- Python 3.7 or higher

## Project Structure

```
.
├── main.py               # CLI interface and username validation
├── activity_tracker.py   # Makes requests and prints activity summaries
```

## Notes

- Uses the unauthenticated GitHub API (limit: 60 requests/hour)
- Response is printed to the terminal in a readable format
- Events are displayed in the order GitHub returns them (most recent first)