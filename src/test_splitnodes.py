import unittest
from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test(self):
        node = [TextNode("I'm very much hoping this is going to _work_ the way it fucking should.", TextType.PLAIN)]
        split = split_nodes_delimiter(node, "_", TextType.ITALIC)
        self.assertEqual(len(split), 3)
        self.assertEqual(split[0].text, "I'm very much hoping this is going to ")
        self.assertEqual(split[0].text_type, TextType.PLAIN)
        self.assertEqual(split[1].text, "work")
        self.assertEqual(split[1].text_type, TextType.ITALIC)
        self.assertEqual(split[2].text, " the way it fucking should.")
        self.assertEqual(split[2].text_type, TextType.PLAIN)

    def test2(self):
        node2 = [TextNode("**Okay**, so if that one passed, how does it handle this different challenge?", TextType.PLAIN)]
        split2 = split_nodes_delimiter(node2, "**", TextType.BOLD)
        self.assertEqual(split2[0].text, "")
        self.assertEqual(split2[1].text, "Okay")
        self.assertEqual(split2[1].text_type, TextType.BOLD)
        self.assertEqual(split2[2].text, ", so if that one passed, how does it handle this different challenge?")
        self.assertEqual(split2[2].text_type, TextType.PLAIN)
