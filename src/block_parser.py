import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    return [*filter(lambda block: block is not "", (markdown.strip().split("\n\n")))]

def block_to_block_type(block):
    heading_pattern = r"^#{1,6}\s.*$"
    code_pattern = r"^`{3}[\s\S]*`{3}$"
    quote_pattern = r"^>(?:.*\n>.*)*$"
    unordered_list_pattern = r"^[*-] (?:.*\n[*-] .*)*$"
    ordered_list_pattern = r"^1. (?:.*\n\d. .*)*$"
    if re.match(heading_pattern, block):
        return block_type_heading
    if re.match(code_pattern, block):
        return block_type_code
    if re.match(quote_pattern, block):
        return block_type_quote
    if re.match(unordered_list_pattern, block):
        return block_type_unordered_list
    if re.match(ordered_list_pattern, block):
        return block_type_ordered_list
    return block_type_paragraph
    