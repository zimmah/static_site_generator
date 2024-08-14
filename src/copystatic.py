import os
import shutil

def copy_static(source_path, destination):
    if os.path.exists(destination):
        print(f"deleting {destination}")
        shutil.rmtree(destination)
    print(f"creating empty {destination}")
    os.mkdir(destination)
    copy_files(source_path, destination)

def copy_files(source_path, destination):
    if os.path.isfile(source_path):
        print(f"copying {source_path} to {destination}")
        shutil.copy(source_path, destination)
    else:
        directory = source_path.split("/")[-1]
        if directory == source_path[2:]:
            new_destination = destination
        else:
            new_destination = os.path.join(destination, directory)
        if not os.path.exists(new_destination):
            print(f"creating directory: {directory}")
            os.mkdir(new_destination)
        print(f"copying {os.listdir(source_path)} from {source_path}")
        for item in os.listdir(source_path):
            copy_files(os.path.join(source_path, item), new_destination)
