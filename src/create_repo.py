from github import Github, GithubException
import utils


#Creates a new private repository on GitHub.
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


def create_issue_label(g, repo, label_name):

    label = g.get_user().get_repo(repo).create_label(label_name, "FFC0CB")
    return label


def main():
    u=utils
    # Parse command-line arguments
    args = u.parse_args()

    # Get GitHub access token from a config file
    token = u.get_github_token()
    g = Github(token)

    # Create the new repository
    create_github_repository(g, args.repo)
    # Add the specified team as a label for the repository
    if args.label:
        create_issue_label(g, args.repo, args.label)
        print(f"Label created with team name {args.label}")


if __name__ == '__main__':
    main()