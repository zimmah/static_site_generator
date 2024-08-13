from textnode import TextNode, text_type_text

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
    