import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()