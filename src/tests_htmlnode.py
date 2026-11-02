import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test(self):
        node = HTMLNode("a", "This is definitely not the standard formatting", None, {"href":"http://www.willthiswork.com", "target":"_blank"})
        self.assertIsNone(node.children)

    def test2(self):
        node2 = HTMLNode("p", "This is absolutely going to drive me insane typing HTML like this")
        self.assertIsNone(node2.props)

    def test3(self):
        node3 = HTMLNode("H1", "One of these days I'm going to turn this into a real static site")
        self.assertIsNotNone(node3.value)
        self.assertIsNotNone(node3.tag)