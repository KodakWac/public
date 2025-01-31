from textnode import *



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
        else:
            if delimiter in node.text:
                parts = node.text.split(delimiter)
                new_list.append(TextNode(parts[0], TextType.PLAIN))
                new_list.append(TextNode(parts[1], text_type))
                new_list.append(TextNode(parts[2], TextType.PLAIN))
            else:
                new_list.append(node)
    return new_list
