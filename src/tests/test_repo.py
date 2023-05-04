#import create_repo as cr_re
#import utils
from create_repo import create_github_repository
import utils
from github import Github
from delete_repo import delete_repo


def test_create_and_delete_github_repository():
    u = utils
    token = u.get_github_token()
    g = Github(token)
    repository = "my_new_repo"
    assert create_github_repository(g, repository) == repository

    assert delete_repo(repository, token) == f"Repo {repository} deleted"