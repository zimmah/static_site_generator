import unittest
from block_parser import markdown_to_blocks, block_to_block_type, block_type_code, block_type_quote, block_type_ordered_list, block_type_unordered_list, block_type_heading1, block_type_paragraph

class TestHTMLNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        blocks = ["# This is a heading",
                 "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                 "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                 ]
        self.assertEqual(markdown_to_blocks(markdown), blocks)

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), block_type_heading1)

    def test_block_to_block_type_code(self):
        block = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_block_to_block_type_unordered_list(self):
        block = "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading1)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()