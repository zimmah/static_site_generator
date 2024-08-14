import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node, markdown_to_html_node
from textnode import TextNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(tag="a", value="google", props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_children(self):
        node = HTMLNode(tag="a", value="google", props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        node2 = HTMLNode(tag="li", children=[node])
        self.assertEqual(node2.children, [node])

    def test_tag(self):
        node = HTMLNode(tag="a", value="google", props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        self.assertEqual(node.tag, "a")

    def test_tag2(self):
        node = HTMLNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual(node.tag, "p")

    def test_tag3(self):
        node = HTMLNode(tag="b", value="This is bold text.")
        node2 = HTMLNode(tag="p", value="This is a paragraph. This is the last sentence</p>", children=[node])
        self.assertEqual(node2.tag, "p")

    def test_leafnode(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_leafnode_with_attributes(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_parent_node_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    def test_textnode_to_leafnode_bold(self):
        node = TextNode("This is a text node", "bold")
        htmlnode = text_node_to_html_node(node)
        html = htmlnode.to_html()
        self.assertEqual(html, "<b>This is a text node</b>")

    def test_textnode_to_leafnode_img(self):
        node = TextNode("This is alt text", "image", "https://some.img.url")
        htmlnode = text_node_to_html_node(node)
        html = htmlnode.to_html()
        self.assertEqual(html, '<img src="https://some.img.url" alt="This is alt text"></img>')

    def test_markdown_to_html(self):
        block = "* list\n* items"
        self.assertEqual(markdown_to_html_node(block).to_html(), "<div><ul><li>list</li><li>items</li></ul></div>")
        block = "###### this is a header 6"
        self.assertEqual(markdown_to_html_node(block).to_html(), "<div><h6>this is a header 6</h6></div>")
    

    def test_paragraph(self):
        md = """
        This is **bolded** paragraph text in a p tag here
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """This is **bolded** paragraph text in a p tag here\n\nThis is another paragraph with *italic* text and `code` here"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        self.maxDiff = None
        md = """- This is a list\n- with items\n- and *more* items\n\n1. This is an `ordered` list\n2. with items\n3. and more items
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """# this is an h1\n\nthis is paragraph text\n\n## this is an h2\n"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """> This is a\n> blockquote block\n\nthis is paragraph text"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

if __name__ == "__main__":
    unittest.main()