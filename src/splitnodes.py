from textnode import TextNode, TextType

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