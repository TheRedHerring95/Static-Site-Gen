import re
from textnode import TextNode
from parentnode import ParentNode
from texttonode import text_to_textnodes
from textnode import text_node_to_html_node

def unordered_lists(markdown):
    items = markdown.split("\n")
    nodes = []
    for item in items:
        if item[0:2] == "- ":
            item = item[2:]
            text = text_to_textnodes(item)
            nodes.append(ParentNode("li", [text_node_to_html_node(t) for t in text]))
    return nodes
    
def ordered_lists(markdown):
    items = markdown.split("\n")
    nodes = []
    for item in items:
        item = re.sub(r'^\d+\.\s+', "", item)
        text = text_to_textnodes(item)
        nodes.append(ParentNode("li", [text_node_to_html_node(t) for t in text]))
    return nodes