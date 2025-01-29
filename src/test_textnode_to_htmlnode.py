import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from textnode import *


def test_text_node_to_html_node():
    node = TextNode("This is plain text", TextType.PLAIN)
    html_node = text_node_to_html_node(node)
    assert html_node.tag == ""
    assert html_node.value == "This is plain text"
    assert html_node.props == {}

def test_bold_text_node_to_html_node():
    node = TextNode("This is bold text", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    assert html_node.tag == "b"
    assert html_node.value == "This is bold text"
    assert html_node.props == {}

def test_italic_text_node_to_html_node():
    node = TextNode("This is italic text", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    assert html_node.tag == "i"
    assert html_node.value == "This is italic text"
    assert html_node.props == {}

def test_code_text_node_to_html_node():
    node = TextNode("This is code", TextType.CODE)
    html_node = text_node_to_html_node(node)
    assert html_node.tag == "code"
    assert html_node.value == "This is code"
    assert html_node.props == {}

def test_link_text_node_to_html_node():
    node = TextNode("This is a link", TextType.LINK, "https://example.com")
    html_node = text_node_to_html_node(node)
    assert html_node.tag == "a"
    assert html_node.value == "This is a link"
    assert html_node.props == {"href": "https://example.com"}

def test_image_text_node_to_html_node():
    node = TextNode("alt text for image", TextType.IMAGE, "https://example.com")
    html_node = text_node_to_html_node(node)
    assert html_node.tag == "img"
    assert html_node.value == ""
    assert html_node.props == {"src": "https://example.com", "alt": "alt text for image"}

def test_invalid_text():
    try:
        node = TextNode("some text", None)  
        html_node = text_node_to_html_node(node)
        assert False, "Should have raised an exception"
    except ValueError:
        assert True