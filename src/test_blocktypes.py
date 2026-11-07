import unittest
from blocknode import *

class TestBlockType(unittest.TestCase):
    def test(self):
        block = "# This should be a heading"
        typed = block_to_blocktype(block)
        self.assertEqual(typed, BlockType.HEAD)

    def test2(self):
        block = """```
This one should be a code block
```"""
        typed = block_to_blocktype(block)
        self.assertEqual(typed, BlockType.CODE)

    def test3(self):
        block = "```This one shouldn't be a code block, but it  wants to be.```"
        typed = block_to_blocktype(block)
        self.assertEqual(typed, BlockType.PARA)

    def test4(self):
        block = """
```
This also wants to be code but isn't
"""
        typed = block_to_blocktype(block)
        self.assertEqual(typed, BlockType.PARA)

    def test5(self):
        block = "> This is a quote"
        typed = block_to_blocktype(block)
        self.assertEqual(typed, BlockType.QUOTE)

    def test6(self):
        block = "- This list is unordered"
        typed = block_to_blocktype(block)
        self.assertEqual(typed, BlockType.UNORDERED)

    def test7(self):
        block = "1. This list is ordered at 1"
        typed = block_to_blocktype(block)
        self.assertEqual(typed, BlockType.ORDERED)

    def test8(self):
        block = "6. This is ordered at 6"
        typed = block_to_blocktype(block)
        self.assertEqual(typed, BlockType.ORDERED)

    def test9(self):
        block = "458946. This is much higher number ordered list"
        typed = block_to_blocktype(block)
        self.assertEqual(typed, BlockType.ORDERED)

    def test10(self):
        block = "And this should just be a normal paragraph"
        typed = block_to_blocktype(block)
        self.assertEqual(typed, BlockType.PARA)