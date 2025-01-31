from enum import Enum
from htmlnode import LeafNode
from markdown_extract import *

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise ValueError("Invalid tex type")
    
    if text_node.text_type == TextType.PLAIN:
        node = LeafNode("", text_node.text)
        return node
    
    if text_node.text_type == TextType.BOLD:
        node = LeafNode("b", text_node.text)
        return node
    
    if text_node.text_type == TextType.ITALIC:
        node = LeafNode("i", text_node.text)
        return node
    
    if text_node.text_type == TextType.CODE:
        node = LeafNode("code", text_node.text)
        return node
    
    if text_node.text_type == TextType.LINK:
        node = LeafNode("a", text_node.text, {"href": text_node.url})
        return node
    
    if text_node.text_type == TextType.IMAGE:
        node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        return node


def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:

        if node.text_type != TextType.PLAIN:
            new_list.append(node)
        else:
            images = extract_markdown_images(node)  
            if not images:
                new_list.append(node)
            else:
           
                remaining_text = node.text  
                for image_alt, image_link in images:  
                    parts = remaining_text.split(f"![{image_alt}]({image_link})", 1)

               
                    if parts[0].strip():
                        new_list.append(TextNode(parts[0], TextType.PLAIN))
                
                    new_list.append(TextNode(image_alt, TextType.IMAGE, image_link))
                
                    remaining_text = parts[1]
                
                if remaining_text.strip():
                    new_list.append(TextNode(remaining_text, TextType.PLAIN))

    return new_list

def split_nodes_links(old_nodes):
    new_list = []

    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_list.append(node)
        else:
            links = extract_markdown_links(node)
            if not links:
                new_list.append(node)
            else:
                remaining_text = node.text
                for link_text, link_url in links:
                    parts = remaining_text.split(f"[{link_text}]({link_url})", 1)

                    if parts[0].strip():
                        new_list.append(TextNode(parts[0], TextType.PLAIN))

                    new_list.append(TextNode(link_text, TextType.LINK, link_url))
                
                    remaining_text = parts[1]
                
                if remaining_text.strip():
                    new_list.append(TextNode(remaining_text, TextType.PLAIN))

    return new_list





