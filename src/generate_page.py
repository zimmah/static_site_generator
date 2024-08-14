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

def generate_page(source_path, template_path, destination):
    print(f"Generating page from {source_path} to {destination} using {template_path}.")
    markdown = get_file(source_path)
    template = get_file(template_path)
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    html = template.replace("{{ Content }}", content).replace("{{ Title }}", title)
    with open(os.path.join(destination, "index.html"), "w", encoding="utf-8") as index:
         index.write(html)

def generate_pages_recursive():
     pass