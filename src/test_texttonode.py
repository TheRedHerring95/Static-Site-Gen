import unittest
from texttonode import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToNode(unittest.TestCase):
    def test(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.PLAIN),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.PLAIN),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )

    def test2(self):
        text = "How does _this_ now handles _not just one_ but **two instances** for both _italic_ **and bold** text. And let's throw `two more` _italics_ and a `few` of `codes` in there too."
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("How does ", TextType.PLAIN),
                TextNode("this", TextType.ITALIC),
                TextNode(" now handles ", TextType.PLAIN),
                TextNode("not just one", TextType.ITALIC),
                TextNode(" but ", TextType.PLAIN),
                TextNode("two instances", TextType.BOLD),
                TextNode(" for both ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" ", TextType.PLAIN),
                TextNode("and bold", TextType.BOLD),
                TextNode(" text. And let's throw ", TextType.PLAIN),
                TextNode("two more", TextType.CODE),
                TextNode(" ", TextType.PLAIN),
                TextNode("italics", TextType.ITALIC),
                TextNode(" and a ", TextType.PLAIN),
                TextNode("few", TextType.CODE),
                TextNode(" of ", TextType.PLAIN),
                TextNode("codes", TextType.CODE),
                TextNode(" in there too.", TextType.PLAIN)
            ],
            nodes
        )