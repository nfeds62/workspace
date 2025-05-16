from textnode import TextNode, TextType

def main():
    """
    Main function to demonstrate the functionality of the TextNode class.
    """
    # Create a normal text node
    node = TextNode("This is some anchor text", TextType.LINK_TEXT, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()