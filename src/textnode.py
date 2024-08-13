class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(a, b):
        if a.text != b.text:
            return False
        if a.text_type != b.text_type:
            return False
        if a.url != b.url:
            return False
        return True
    
    def __repr__(textnode):
        return f"TextNode({textnode.text}, {textnode.text_type}, {textnode.url})"
    
def main():
    return

main()