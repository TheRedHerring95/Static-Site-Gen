import unittest
from splitnodes import *
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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://thefirst.link) and another [link too](https://thesecond.link)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://thefirst.link"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("link too", TextType.LINK, "https://thesecond.link"),
            ],
            new_nodes,
        )

    def test_split_mixed(self):
        node = TextNode(
            "This is some **bold text** with a [link](https://thefirst.link) and ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        bold_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        image_nodes = split_nodes_images(bold_nodes)
        all_nodes = split_nodes_links(image_nodes)

        self.assertListEqual(
            [
                TextNode("This is some ", TextType.PLAIN),
                TextNode("bold text", TextType.BOLD),
                TextNode(" with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://thefirst.link"),
                TextNode(" and ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            all_nodes,
        )