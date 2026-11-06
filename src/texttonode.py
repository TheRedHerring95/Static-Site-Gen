from textnode import TextNode
from splitnodes import *

def text_to_textnodes(text:str) -> list[TextNode]:
    node = TextNode(text, TextType.PLAIN)
    first = split_nodes_links([node])
    second = split_nodes_images(first)
    third = split_nodes_delimiter(second, "**", TextType.BOLD)
    fourth = split_nodes_delimiter(third, "_", TextType.ITALIC)
    fifth = split_nodes_delimiter(fourth, "`", TextType.CODE)
    return fifth