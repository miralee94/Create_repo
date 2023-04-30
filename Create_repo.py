import argparse
from github import Github, GithubException


#Parses command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description='Create a new private repository on GitHub')
    parser.add_argument('repo', type=str, help='Name of the new repository')
    parser.add_argument('--label', type=str, default=None, help='Name of the team to set as a label')
    return parser.parse_args()


#Reads GitHub access token from a config file
def get_github_token():
    with open('config.txt', 'r') as f:
        token = f.read().strip()
    return token


#Creates a new private repository on GitHub.
def create_github_repository(token, repo_name):
    # Create PyGithub object using the access token
    g = Github(token)

    # Get the authenticated user
    user = g.get_user()
    try:
        # Create the new repository
        repo = user.create_repo(repo_name, private=True)
        print(f'Repository {repo_name} created successfully.')
        return repo
    except GithubException as e:
        print(f'Error creating repository: {e}')


#def add_team_label_to_repository(token, repo_name, team_name):
#    """Adds a team as a label for the repository."""
#    # Create PyGithub object using the access token
#    g = Github(token)
#
#    # Get the authenticated user
#    user = g.get_user()
#
#    # Get the repository
#    repo = user.get_repo(repo_name)
#
#    # Get the specified team
#    teams = g.get_user().get_teams()
#    for team in teams:
#        if team.name == team_name:
#            repo.add_to_topics(team_name)
#            print(f'Team "{team_name}" added as a label for the repository')
#            break
#    else:
#        print(f'Could not find a team with the name "{team_name}"')


def create_issue_label(token, repo, label_name):
    g = Github(token)
    label = g.get_user().get_repo(repo).create_label(label_name, "FFC0CB")
    return label


def main():
    # Parse command-line arguments
    args = parse_args()

    # Get GitHub access token from a config file
    token = get_github_token()

    # Create the new repository
    create_github_repository(token, args.repo)
    # Add the specified team as a label for the repository
    if args.label:
        create_issue_label(token, args.repo, args.label)
        print(f"Label created with team name {args.label}")


if __name__ == '__main__':
    main()