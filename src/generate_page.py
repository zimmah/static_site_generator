from htmlnode import markdown_to_html_node
import os

def extract_title(markdown):
    first_line = markdown.split("\n")[0]
    if not first_line.startswith("# "):
        raise ValueError("The provided Markdown does not have a title.")
    title = first_line[2:].strip()
    return title

def get_file(file_path):
        with open(f"{file_path}") as file:
            return file.read()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Generating pages from {dir_path_content} to {dest_dir_path} using {template_path}.")
    directory_items = os.listdir(dir_path_content)
    for item in directory_items:
        current_path = os.path.join(dir_path_content, item)
        if item.endswith(".md"):
            markdown = get_file(current_path)
            template = get_file(template_path)
            filename = item[:-3] + ".html"
            title = extract_title(markdown)
            content = markdown_to_html_node(markdown).to_html()
            html = template.replace("{{ Content }}", content).replace("{{ Title }}", title)
            with open(os.path.join(dest_dir_path, filename), "w", encoding="utf-8") as file:
                file.write(html)
        else:
             destination = os.path.join(dest_dir_path, item)
             if not os.path.exists(destination):
                  os.mkdir(destination)
             generate_pages_recursive(current_path, template_path, destination)
