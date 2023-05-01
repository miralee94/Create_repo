import argparse


# Parses command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description='Create a new private repository on GitHub')
    parser.add_argument('repo', type=str, help='Name of the repository')
    parser.add_argument('--label', type=str, default=None, help='Name of the team to set as a label')
    parser.add_argument('--color', type=str, default=None, help='Specify the color of the label')
    return parser.parse_args()


# Reads GitHub access token from a config file
def get_github_token():
    with open('config.txt', 'r') as f:
        token = f.read().strip()
    return token
