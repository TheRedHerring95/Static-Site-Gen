from blocknode import block_to_blocktype, BlockType
from parentnode import ParentNode
from splitblocks import markdown_to_blocks
from textnode import text_node_to_html_node, TextNode, TextType
from texttonode import text_to_textnodes
from htmlnode import HTMLNode

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    nodes =[]
    for block in blocks:
        typed = (block_to_blocktype(block))
        if typed != BlockType.CODE:
            text_nodes = text_to_textnodes(block)
            html_nodes = []
            for text_node in text_nodes:
                html_nodes.append(text_node_to_html_node(text_node))
        if typed == BlockType.PARA:
            block_node = ParentNode("p", html_nodes)
            nodes.append(block_node)
        elif typed == BlockType.HEAD:
            count = 1
            while block[count] == "#":
                count +=1
            block_node = ParentNode(f"h{count}", html_nodes)
            nodes.append(block_node)
        elif typed == BlockType.CODE:
            text_node = TextNode(block, TextType.CODE)
            html_node = text_node_to_html_node(text_node)
            block_node = ParentNode("pre", [html_node])
            nodes.append(block_node)
        elif typed == BlockType.QUOTE:
            block_node == ParentNode("blockquote", html_nodes)
            nodes.append(block_node)
        elif typed == BlockType.UNORDERED:
            block_node = ParentNode("ul", html_nodes)
            nodes.append(block_node)
        elif typed == BlockType.ORDERED:
            block_node = ParentNode("ol", html_nodes)
            nodes.append(block_nodes)
        else: raise Exception("Invalid block")
    parent = ParentNode("div", nodes)
    return parent