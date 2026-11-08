from blocknode import block_to_blocktype
from splitblocks import markdown_to_blocks
from htmlnode import HTMLNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks
    types = []
    for block in blocks:
        types.append(block_to_blocktype(block))
    