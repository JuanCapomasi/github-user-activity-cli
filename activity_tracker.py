from urllib import request, error
import json

def parse_activity(html,username):
    events = json.loads(html)
    custom_actions = {
        "review_requested": "requested a review on",
        "review_request_removed": "removed a review request from",
        "assigned": "was assigned to",
        "unassigned": "was unassigned from",
        "labeled": "added a label to",
        "unlabeled": "removed a label from"
    }
    for event in events:
        repo_name = event["repo"]["name"]
        if event["type"] == "PushEvent":
            commit_count = len(event["payload"]["commits"])
            commit_label = "commit" if commit_count == 1 else "commits"
            print(f"{username} pushed {commit_count} {commit_label} to {repo_name}.")
            continue

        if event["type"] == "IssuesEvent":
            action = event["payload"]["action"]
            verb = custom_actions.get(action, f"{action}")
            print(f"{username} {verb} an issue in {repo_name}.")
            continue

        if event["type"] == "WatchEvent":
            print(f"{username} starred {repo_name}.")
            continue

        if event["type"] == "CreateEvent":
            ref_type = event["payload"]["ref_type"]
            print(f"{username} created a new {ref_type} in {repo_name}.")
            continue

        if event["type"] == "PullRequestEvent":
            action = event["payload"]["action"]
            verb = custom_actions.get(action, f"{action}")
            print(f"{username} {verb} a pull request in {repo_name}.")
            continue

        if event["type"] == "ForkEvent":
            fork_name = event["payload"]["forkee"]["full_name"]
            print(f"{username} forked {repo_name} repo to {fork_name}.")
            continue


def request_activity(username):
    print(f"Requesting recent activity from {username}.")
    url = f"https://api.github.com/users/{username}/events"
    try:
        response = request.urlopen(url)
        html = response.read().decode('utf-8')
        parse_activity(html, username)
        return html
    except error.HTTPError as e:
        if e.code == 404:
            print("User not found.")
        elif e.code == 403:
            print("Rate limit exceeded. Please try again later.")
        else:
            print(f"HTTP error {e.code}: {e.reason}")
    except error.URLError as e:
        print(f"Network error: {e.reason}")
    except json.JSONDecodeError:
        print("Failed to decode response from GitHub.")

    return None