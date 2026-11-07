from enum import Enum

class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "codeblock"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"

def block_to_blocktype(block:str) -> BlockType:
    if block[0] == "#":
        return BlockType.HEAD
    elif block[:4] == "```\n" and block[-3:] == "```":
        return BlockType.CODE
    elif block[0] == ">":
        return BlockType.QUOTE
    elif block[0] == "-":
        return BlockType.UNORDERED
    elif block[0].isdigit():
        count = 1
        while block[count].isdigit():
            count+=1
        if block[count:count+2] == ". ":
            return BlockType.ORDERED
        else: return BlockType.PARA
    else: return BlockType.PARA