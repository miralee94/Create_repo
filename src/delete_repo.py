from github import Github
import utils

# Delete created repository
def delete_repo(repo, token):
    g = Github(token)
    g.get_user().get_repo(repo).delete()


def main():
    # Save module utils to a variable
    u = utils

    # Parse command-line arguments
    args = u.parse_args()

    # Get GitHub access token from a config file
    token = u.get_github_token()
    delete_repo(args.repo, token)


if __name__ == '__main__':
    main()
