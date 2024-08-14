import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"

def copy_static():
    if os.path.exists(dir_path_public):
        print(f"deleting {dir_path_public}")
        shutil.rmtree(dir_path_public)
    print(f"creating empty {dir_path_public}")
    os.mkdir(dir_path_public)
    copy_files(dir_path_static)

def copy_files(source_path, destination=dir_path_public):
    if os.path.isfile(source_path):
        print(f"copying {source_path} to {destination}")
        shutil.copy(source_path, destination)
    else:
        directory = source_path.split("/")[-1]
        new_destination = os.path.join(destination, directory)
        if not os.path.exists(new_destination):
            print(f"creating directory: {directory}")
            os.mkdir(new_destination)
        print(f"copying {os.listdir(source_path)} from {source_path}")
        for item in os.listdir(source_path):
            copy_files(os.path.join(source_path, item), new_destination)
