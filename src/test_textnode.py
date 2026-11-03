import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This text is italic", TextType.ITALIC)
        self.assertEqual(node, node2)
        
    def test2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is different bold text", TextType.BOLD)
        self.assertNotEqual(node,node4)
    
    def test3(self):
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This text is italic", TextType.ITALIC)
        self.assertNotEqual(node2,node3)

    def test4(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

    def test5(self):
        node5 = TextNode("I've got a URL", TextType.LINK, "https://ImADummy.com")
        self.assertIsNotNone(node5.url)

    def test6(self):
        node6 = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node6)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test7(self):
        node7 = TextNode("How's this translating the bold text?", TextType.BOLD)
        htm = text_node_to_html_node(node7)
        self.assertEqual(htm.tag, "b")
        self.assertEqual(htm.value, "How's this translating the bold text?")


if __name__ == "__main__":
    unittest.main()