from functools import reduce
from block_parser import markdown_to_blocks, block_to_block_type
from inline_parser import text_to_textnodes

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return ''.join(map(lambda key: ' ' + key + '="' + self.props[key] + '"', self.props))
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value in Leaf Node.")
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML: no tag in Parent Node.")
        if not self.children:
            raise ValueError("Invalid HTML: no children in Parent Node.")
        children = reduce(lambda acc, child: acc + child.to_html(), self.children, "")
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid text type.")
        
def markdown_to_html_node(markdown):
    # this function should be refactored
    # using helper functions, also it can utilize block_to_html_node
    # headers and list can be cleaner
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case "quote":
                lines = block.split("\n")
                new_lines = []
                for line in lines:
                    new_lines.append(line[1:])
                cleaned_block = "".join(new_lines).strip()
                children.append(LeafNode("blockquote", cleaned_block))
            case "ordered_list":
                lines = block.split("\n")
                grandchildren = []
                for line in lines:
                    greatgrandchildren = []
                    greatgrandchildren_textnodes = text_to_textnodes(line[3:])
                    for greatgrandchildren_textnode in greatgrandchildren_textnodes:
                        greatgrandchildren.append(text_node_to_html_node(greatgrandchildren_textnode))
                    grandchildren.append(ParentNode("li", greatgrandchildren))
                children.append(ParentNode("ol", grandchildren))
            case "unordered_list":
                lines = block.split("\n")
                grandchildren = []
                for line in lines:
                    greatgrandchildren = []
                    greatgrandchildren_textnodes = text_to_textnodes(line[2:])
                    for greatgrandchildren_textnode in greatgrandchildren_textnodes:
                        greatgrandchildren.append(text_node_to_html_node(greatgrandchildren_textnode))
                    grandchildren.append(ParentNode("li", greatgrandchildren))
                children.append(ParentNode("ul", grandchildren))
            case "heading1":
                children.append(LeafNode("h1", block[2:]))
            case "heading2":
                children.append(LeafNode("h2", block[3:]))
            case "heading3":
                children.append(LeafNode("h3", block[4:]))
            case "heading4":
                children.append(LeafNode("h4", block[5:]))
            case "heading5":
                children.append(LeafNode("h5", block[6:]))
            case "heading6":
                children.append(LeafNode("h6", block[7:]))
            case "paragraph":
                grandchildren = []
                grandchildren_textnodes = text_to_textnodes(block)
                for grandchildren_textnode in grandchildren_textnodes:
                    grandchildren.append(text_node_to_html_node(grandchildren_textnode))
                children.append(ParentNode("p", grandchildren))
            case "code":
                block = block[3:-3]
                children.append(ParentNode("pre", [LeafNode("code", block)]))

    return ParentNode("div", children)