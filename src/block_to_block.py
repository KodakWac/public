from delimiter import *
from enum import Enum
from htmlnode import *
from markdown_extract import *

def block_to_block_type(block):
    count = 0
    
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    if 1 <= count <=6 and len(block)> count and block[count] == " ":
        return "heading"
    
    if block.startswith("```") and block.endswith("```"):
        return "code"
    
    lines = block.split("\n")

    if all(line.startswith(">") for line in lines):
        return "quote"

    if all(line.startswith("* ") or line.startswith("- ") for line in lines):
        return "unordered list"

    counter = 1
    for line in lines:
        if not line.startswith(f"{counter}. "):
            return "paragraph"
        counter += 1
    return "ordered list"

