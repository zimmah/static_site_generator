import shutil
import os

def main():
    def copy_static():
        if os.path.exists("./public"):
            print("deleting ./public")
            shutil.rmtree("./public")
        print("creating empty ./public")
        os.mkdir("./public")
        copy_files("./static")
    
    def copy_files(path, destination="./public/"):
        if os.path.isfile(path):
            print(f"copying {path} to {destination}")
            shutil.copy(path, destination)
        else:
            directory = path.split("/")[-1]
            if directory != "static":
                print(f"creating directory: {directory}")
                os.mkdir(os.path.join(destination, directory))
            if len(path.split("./static/")) > 1:
                destination = os.path.join(destination, directory)
            print(f"copying {os.listdir(path)} from {path}")
            for item in os.listdir(path):
                copy_files(os.path.join(path, item), destination)

    copy_static()

main()