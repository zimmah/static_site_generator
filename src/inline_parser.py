from textnode import TextNode, text_type_text, text_type_image, text_type_link, text_type_bold, text_type_code, text_type_italic
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        nodes_text = old_node.text.split(delimiter)
        if len(nodes_text) % 2 == 0:
            raise ValueError("Invalid Markdown, formatted section not closed.")
        i = 0
        for node_text in nodes_text:
            i += 1
            if not node_text:
                continue
            if i % 2 == 1:
                split_nodes.append(TextNode(node_text, text_type_text))
            else:
                split_nodes.append(TextNode(node_text, text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue
        for image in images:
            alt_text, img_href = image
            first_section, original_text = original_text.split(f"![{alt_text}]({img_href})", 1)
            if first_section != "":
                new_nodes.append(TextNode(first_section, text_type_text))
            new_nodes.append(TextNode(alt_text, text_type_image, img_href))
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
    
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue
        for link in links:
            link_text, link_href = link
            first_section, original_text = original_text.split(f"[{link_text}]({link_href})", 1)
            if first_section != "":
                new_nodes.append(TextNode(first_section, text_type_text))
            new_nodes.append(TextNode(link_text, text_type_link, link_href))
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes