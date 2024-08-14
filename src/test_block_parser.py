import unittest
from block_parser import markdown_to_blocks, block_to_block_type, block_type_unordered_list, block_type_heading, block_type_paragraph

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
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_block_to_block_type_code(self):
        block = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_block_to_block_type_unordered_list(self):
        block = "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)

if __name__ == "__main__":
    unittest.main()