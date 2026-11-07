import unittest
from splitblocks import markdown_to_blocks

class TestMDToBlock(unittest.TestCase):
    def test(self):
        markdown = """
Let's have a look at the way this breaks things up, or if it does at all.

Are we having this break in the spots that it's supposed to?
Or is it breaking only where I'm wanting it to?

       

Did it clear that whitespace and remove the entry, or is it sitting above this one?

And how about when I do a weird hybrid splitting?\n
Did it just break then?
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "Let's have a look at the way this breaks things up, or if it does at all.",
                "Are we having this break in the spots that it's supposed to?\nOr is it breaking only where I'm wanting it to?",
                "Did it clear that whitespace and remove the entry, or is it sitting above this one?",
                "And how about when I do a weird hybrid splitting?",
                "Did it just break then?"
            ]
        )
        self.assertEqual(5, len(blocks))

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )