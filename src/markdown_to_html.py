from delimiter import *
from enum import Enum
from htmlnode import *
from markdown_extract import *
from textnode import *
from block_to_block import *
from text_to_textnode import *
from markdown_block import *
from markdown_extract import *

def markdown_to_html_node(markdown):
    new_list = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        new_nodes = block_to_block_type(block)
        if new_nodes == "paragraph":
            content = HTMLNode("p", None, text_to_children(block))
            new_list.append(content)

        elif new_nodes == "heading":
            level = block.count('#')  
            tag = f"h{level}"
            content = HTMLNode(tag, None, text_to_children(block))
            new_list.append(content)

        elif new_nodes == "quote":
            block = block.lstrip("> ")
            content = HTMLNode("blockquote", None, text_to_children(block))
            new_list.append(content)

        elif new_nodes == "code":
            block = block.strip("`")
            code_node = HTMLNode("code", None, text_to_children(block))
            content = HTMLNode("pre", None, [code_node])
            new_list.append(content)

        elif new_nodes == "unordered_list":
            items = block.split("\n")
            list_items = []
            for item in items:
                item = item.lstrip("* -")
                li_node = HTMLNode("li", None, text_to_children(item))
                list_items.append(li_node)
            content = HTMLNode("ul", None, list_items)
            new_list.append(content)

        elif new_nodes == "ordered_list":
            items = block.split("\n")
            list_items = []
            for item in items:
                item = item.lstrip("0123456789. ")
                li_node = HTMLNode("li", None, text_to_children(item))
                list_items.append(li_node)
            content = HTMLNode("ol", None, list_items)
            new_list.append(content)

        else:
            raise ValueError(f"Unknown block type: {new_nodes}")
        
    div_node = HTMLNode("div", None, new_list)
    return div_node


def text_to_children(text):
    new_list = []

    nodes = text_to_textnodes(text)
    for node in nodes:
        html_nodes = text_node_to_html_node(node)
        new_list.append(html_nodes)
    return new_list
    