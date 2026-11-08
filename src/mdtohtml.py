from blocknode import block_to_blocktype, BlockType
from parentnode import ParentNode
from splitblocks import markdown_to_blocks
from textnode import text_node_to_html_node, TextNode, TextType
from texttonode import text_to_textnodes
from listhandling import *
from htmlnode import HTMLNode

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    nodes =[]
    for block in blocks:
        typed = (block_to_blocktype(block))
        if typed != BlockType.CODE:
            if typed == BlockType.HEAD:
                count = 1
                while block[count-1] == "#":
                    count +=1
                for i in range(count):
                    block = block.strip("#")
            elif typed == BlockType.QUOTE:
                block = block.strip("> ")
            elif typed == BlockType.UNORDERED:
                list_nodes = unordered_lists(block)
            elif typed == BlockType.ORDERED:
                num = 0
                digit = 0
                while block[digit].isdigit():
                    digit += 1
                num = int(block[:digit])
                list_nodes = ordered_lists(block)
            if typed != BlockType.UNORDERED and typed != BlockType.ORDERED:
                block = block.strip()
                block = block.replace("\n", " ")
                text_nodes = text_to_textnodes(block)
                html_nodes = []
                for text_node in text_nodes:
                    html_nodes.append(text_node_to_html_node(text_node))
        if typed == BlockType.PARA:
            block_node = ParentNode("p", html_nodes)
            nodes.append(block_node)
        elif typed == BlockType.HEAD:
            block_node = ParentNode(f"h{count}", html_nodes)
            nodes.append(block_node)
        elif typed == BlockType.CODE:
            block = block.strip("```")
            block = block[1:]
            #block = block.strip()
            text_node = TextNode(block, TextType.CODE)
            html_node = text_node_to_html_node(text_node)
            block_node = ParentNode("pre", [html_node])
            nodes.append(block_node)
        elif typed == BlockType.QUOTE:
            block_node = ParentNode("blockquote", html_nodes)
            nodes.append(block_node)
        elif typed == BlockType.UNORDERED:
            block_node = ParentNode("ul", list_nodes)
            nodes.append(block_node)
        elif typed == BlockType.ORDERED:
            block_node = ParentNode("ol", list_nodes, {"start":num})
            nodes.append(block_node)
        else: raise Exception("Invalid block")
    parent = ParentNode("div", nodes)
    return parent