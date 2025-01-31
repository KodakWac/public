from delimiter import *
from enum import Enum
from htmlnode import *
from markdown_extract import *


def markdown_to_blocks(markdown):
    new_list = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        clean_block = block.strip()
        new_list.append(clean_block)
    return new_list