import unittest
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test(self):
        node = LeafNode("a", "This link should be a friendly one", {"href":"http://www.bestfriendsforever.com", "target":"_blank"})
        self.assertIsNotNone(node.props)

    def test2(self):
        node2 = LeafNode("p", "This is absolutely going to drive me insane typing HTML like this")
        self.assertIsNone(node2.props)

    def test3(self):
        node3 = LeafNode("h1", "One of these days I'm going to turn this into a real static site")
        self.assertIsNotNone(node3.value)
        self.assertIsNotNone(node3.tag)

    def test4(self):
        node4 = LeafNode("h3", "Let's see if I've got the HTML muscle memory still around for this one...")
        self.assertEqual(node4.to_html(), "<h3>Let's see if I've got the HTML muscle memory still around for this one...</h3>")