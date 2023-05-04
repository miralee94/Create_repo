from github import Github, GithubException
import utils


# Creates a new private repository on GitHub.
def create_github_repository(g, repo_name):

    # Get the authenticated user
    user = g.get_user()
    try:
        # Create the new repository
        repo = user.create_repo(repo_name, private=True)
        print(f'Repository {repo_name} created successfully.')
        return repo
    except GithubException as e:
        print(f'Error creating repository: {e}')
        exit()

# Creates a label
def create_issue_label(g, repo, label_name, color):
    try:
        label = g.get_user().get_repo(repo).create_label(label_name, color)
        return label
    except GithubException as e:
        print(f'Error creating label: {e}')
        exit()

# Validare color input
def validate_color(color):
    colors = {
    "red": "FF0000",
    "green": "00FF00",
    "blue": "0000FF",
    "white": "FFFFFF",
    "black": "000000",
    "pink": "FFC0CB"
    }
    if color.lower() in colors:
        color = colors[color].lower()
        return color
    else:
        print(f"Invalid choice: {color}")
        print("Available colors:")
        for c in colors:
            print(c)
        exit()

def main():
    # Assign module utils to a variable
    u = utils

    # Parse command-line arguments
    args = u.parse_args()

    # Validate color input
    color = validate_color(args.color)

    # Get GitHub access token from a config file
    token = u.get_github_token()

    # Create Github object with token as a parameter
    g = Github(token)

    # Create the new repository
    create_github_repository(g, args.repo)

    # Add the specified team as a label for the repository
    if args.label:
        create_issue_label(g, args.repo, args.label, color)
        print(f"Label created with team name {args.label} and color {args.color}")

if __name__ == '__main__':
    main()
