import re
from activity_tracker import request_activity


def validate_username(username):
    #use github username validation regex
    username = username.lower().strip()
    if not username:
        return False

    pattern = r"^[a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38}$"
    if not re.match(pattern, username):
        return False

    return username



def main():
    while True:
        print("\n ===== User Activity Tracker =====")
        username = validate_username(input("> "))
        if not username:
            print("Invalid username. Please try again.")
            continue

        request_activity(username)

if __name__ == "__main__":
    main()