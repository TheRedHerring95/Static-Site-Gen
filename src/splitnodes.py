from textnode import TextNode, TextType
from extraction import *

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    node_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            node_list.append(old_node)
            continue
        text_list = old_node.text.split(delimiter,2)
        if len(text_list) <3:
            raise Exception("Invalid Markdown syntax")
        node1 = TextNode(text_list[0], TextType.PLAIN)
        node2 = TextNode(text_list[1], text_type)
        node3 = TextNode(text_list[2], TextType.PLAIN)
        node_list.append(node1)
        node_list.append(node2)
        node_list.append(node3)
        continue
    return node_list

def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    node_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            node_list.append(old_node)
            continue
        current_text = old_node.text
        while True:
            images = extract_markdown_images(current_text)
            if not images:
                if current_text:
                    node_list.append(TextNode(current_text, TextType.PLAIN))
                break
            image = images[0]
            marker = f"![{image[0]}]({image[1]})"
            parts = current_text.split(marker, 1)
            if parts[0]:
                node_list.append(TextNode(parts[0], TextType.PLAIN))
            node_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
            current_text = parts[1]
    return node_list

def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    node_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            node_list.append(old_node)
            continue
        current_text = old_node.text
        while True:
            links = extract_markdown_links(current_text)
            if not links:
                if current_text:
                    node_list.append(TextNode(current_text, TextType.PLAIN))
                break
            link = links[0]
            marker = f"[{link[0]}]({link[1]})" # Fixed the ! typo here
            parts = current_text.split(marker, 1)
            if parts[0]:
                node_list.append(TextNode(parts[0], TextType.PLAIN))
            node_list.append(TextNode(link[0], TextType.LINK, link[1]))
            current_text = parts[1]
    return node_list