import shutil
import os
from git_helper import clone_repository_from_git

OUTPUT_BUILD_FOLDER = "cached_project_builds/"
REPO_DOWNLOAD_FOLDER = "/downloaded_repository"


def get_and_build_repository(repo_url: str):

    # Folder where download the repository to be built
    repo_dir = os.getcwd() + REPO_DOWNLOAD_FOLDER

    clone_repository_from_git(repo_url, repo_dir)

    # Retrieve repository name based on github.com/<user>/<repo_name> url
    repo_name = repo_url.split("/")[-1]
    zip_filename = repo_name + "_build"

    return __build_and_zip_downloaded_project(repo_dir, zip_filename)


def __build_and_zip_downloaded_project(repo_dir: str, zip_filename):
    root_wd = os.getcwd()

    # Move to repo dir to build the project
    os.chdir(repo_dir)

    # Build the project using cmake
    if os.system("mkdir build; cd build; cmake ../; cmake --build .") > 0:
        os.chdir(root_wd)
        os.system(f"rm -rf {repo_dir}")
        return ""

    # Build ZIP from build folder
    archived = shutil.make_archive(
        root_wd + "/" + OUTPUT_BUILD_FOLDER + zip_filename,
        "zip",
        os.getcwd() + "/build",
    )

    os.chdir(root_wd)
    os.system(f"rm -rf {repo_dir}")

    return archived
