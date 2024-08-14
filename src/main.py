from copystatic import copy_static
from generate_page import generate_pages_recursive

path_content_index = "./content/index.md"
path_template = "./template.html"
dir_path_static = "./static"
dir_path_public = "./public"

def main():
    copy_static(dir_path_static, dir_path_public)
    generate_pages_recursive(path_content_index, path_template, dir_path_public)

main()