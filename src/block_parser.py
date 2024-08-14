import re

block_type_paragraph = "paragraph"
block_type_heading1 = "heading1"
block_type_heading2 = "heading2"
block_type_heading3 = "heading3"
block_type_heading4 = "heading4"
block_type_heading5 = "heading5"
block_type_heading6 = "heading6"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    return [*filter(lambda block: block is not "", (markdown.strip().split("\n\n")))]

def block_to_block_type(block):
    heading1_pattern = r"^#{1}\s.*$"
    heading2_pattern = r"^#{2}\s.*$"
    heading3_pattern = r"^#{3}\s.*$"
    heading4_pattern = r"^#{4}\s.*$"
    heading5_pattern = r"^#{5}\s.*$"
    heading6_pattern = r"^#{6}\s.*$"
    code_pattern = r"^`{3}[\s\S]*`{3}$"
    quote_pattern = r"^>(?:.*(?:\n>)?.*)*$"
    unordered_list_pattern = r"^[*-] (?:.*\n[*-] .*)*$"
    ordered_list_pattern = r"^1. (?:.*\n\d. .*)*$"
    if re.match(heading1_pattern, block):
        return block_type_heading1
    if re.match(heading2_pattern, block):
        return block_type_heading2
    if re.match(heading3_pattern, block):
        return block_type_heading3
    if re.match(heading4_pattern, block):
        return block_type_heading4
    if re.match(heading5_pattern, block):
        return block_type_heading5
    if re.match(heading6_pattern, block):
        return block_type_heading6
    if re.match(code_pattern, block):
        return block_type_code
    if re.match(quote_pattern, block):
        return block_type_quote
    if re.match(unordered_list_pattern, block):
        return block_type_unordered_list
    if re.match(ordered_list_pattern, block):
        return block_type_ordered_list
    return block_type_paragraph
    