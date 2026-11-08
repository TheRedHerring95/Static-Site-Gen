import unittest
from mdtohtml import markdown_to_html_node
from parentnode import *

class TestMDToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_all(self):
        md = """
_This_ text **should** be `all` just paragraph, for as long as it may be.

```
This one, however, should be a code block, with nothing else.
```

> And this one here should be a quote of some kind, there to be quote

- This time we've got a list, and it's unordered
- And it's got two items in it

1. Here's an ordered list now
2. And it's got two items
"""
        nodes = markdown_to_html_node(md)
        html = nodes.to_html()
        self.assertEqual(
            html,
            "<div><pre><p><i>This</i> text <b>should</b> be <code>all</code> just paragraph, for as long as it may be.</p><code>This one, however, should be a code block, with nothing else.</code></pre><blockquote>And this one here should be a quote of some kind, there to be quote</blockquote><ul><li>This time we've got a list, and it's unordered</li><li>And it's got two items in it</li></ul><ol><li>Here's an ordered list now</li><li>And it's got two items</li></ol></div"
        )
