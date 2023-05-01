from github import Github
import utils


def delete_repo(repo, token):
    g = Github(token)
    g.get_user().get_repo(repo).delete()


def main():
    u = utils
    args = u.parse_args()
    token = u.get_github_token()
    delete_repo(args.repo, token)


if __name__ == '__main__':
    main()
