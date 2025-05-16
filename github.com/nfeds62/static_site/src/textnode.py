from enum import Enum

class TextType(Enum):
    """
    Enum to represent the type of text.
    """
    NORMAL_TEXT = "Normal Text"
    BOLD_TEXT = "Bold Text"
    ITALIC_TEXT = "Italic Text"
    CODE_TEXT = "Code"
    LINK_TEXT = "link" 
    IMAGES = "image"

class TextNode:
    """
    Class to represent a text node.
    """
    def __init__(self, text: str, text_type: TextType, url: str = None):
        """
        Initialize the TextNode with text and its type.
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        """
        Check if the text node is equal to another value.
        """
        if isinstance(value, TextNode):
            return (self.text == value.text and self.text_type == value.text_type and self.url == value.url)
        return False
        
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"