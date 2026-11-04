import unittest
from extraction import extract_markdown_images, extract_markdown_links

class TestExtractions(unittest.TestCase):
    def test(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test2(self):
        matches = extract_markdown_links("And this text has [a link in it](https://thislinkin.fact)")
        self.assertListEqual([("a link in it", "https://thislinkin.fact")], matches)

    def test3(self):
        text = "Let's see if we can handle ![not only an image](https://www.instagram.com/notonly.events/), but [links too!](https://likethis.one)"
        image = extract_markdown_images(text)
        link = extract_markdown_links(text)
        self.assertListEqual([("not only an image", "https://www.instagram.com/notonly.events/")], image)
        self.assertListEqual([("links too!", "https://likethis.one")], link)
