import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test(self):
        node = ParentNode("a", [LeafNode("b", "Best"), LeafNode(None, " friends "), LeafNode("i", "forever")], {"href":"http://www.bestfriendsforever.com", "target":"_blank"})
        self.assertIsNotNone(node.props)

    def test4(self):
        node = ParentNode("a", [LeafNode("b", "Best"), LeafNode(None, " friends "), LeafNode("i", "forever")], {"href":"http://www.bestfriendsforever.com", "target":"_blank"})
        string = "<a href=http://www.bestfriendsforever.com target=_blank><b>Best</b> friends <i>forever</i></a>"
        self.assertEqual(node.to_html(), string)
