import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from delimiter import *
from textnode import *

def test_split_nodes_delimiter_italic():
    node = TextNode("Hello *world* there", TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)

    assert len(new_nodes) == 3

    assert new_nodes[0].text == "Hello "
    assert new_nodes[0].text_type == TextType.PLAIN

    assert new_nodes[1].text == "world"
    assert new_nodes[1].text_type == TextType.ITALIC

    assert new_nodes[2].text == " there"
    assert new_nodes[2].text_type == TextType.PLAIN

def test_split_nodes_delimiter_bold():
    node = TextNode("Hello **world** there", TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    assert len(new_nodes) == 3

    assert new_nodes[0].text == "Hello "
    assert new_nodes[0].text_type == TextType.PLAIN

    assert new_nodes[1].text == "world"
    assert new_nodes[1].text_type == TextType.BOLD

    assert new_nodes[2].text == " there"
    assert new_nodes[2].text_type == TextType.PLAIN

def test_split_nodes_delimiter_code():
    node = TextNode("Hello `code` there", TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    assert len(new_nodes) == 3

    assert new_nodes[0].text == "Hello "
    assert new_nodes[0].text_type == TextType.PLAIN

    assert new_nodes[1].text == "code"
    assert new_nodes[1].text_type == TextType.CODE

    assert new_nodes[2].text == " there"
    assert new_nodes[2].text_type == TextType.PLAIN

def test_split_nodes_no_delimiter():
    # Test when there's no delimiter in the text
    node = TextNode("Hello world there", TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
    
    assert len(new_nodes) == 1
    assert new_nodes[0].text == "Hello world there"
    assert new_nodes[0].text_type == TextType.PLAIN

def test_split_nodes_different_type():
    # Test when node is already a different type (not TEXT)
    node = TextNode("Hello world there", TextType.BOLD)
    new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
    
    assert len(new_nodes) == 1
    assert new_nodes[0].text == "Hello world there"
    assert new_nodes[0].text_type == TextType.BOLD


if __name__ == '__main__':
    unittest.main()