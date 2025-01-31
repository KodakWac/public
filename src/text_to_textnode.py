from delimiter import *
from enum import Enum
from htmlnode import *
from markdown_extract import *

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.PLAIN)]
    nodes = split_nodes_delimiter(nodes,"**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes,"`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)
    return nodes