from git import Repo


def clone_repository_from_git(git_url, dest_dir):
    print(f"Fetching repository from: {git_url}")
    Repo.clone_from(git_url, dest_dir)
