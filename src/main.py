from statictopublic import static_to_public
from mdtohtml import generate_page
from textnode import TextNode
from textnode import TextType
import sys
import os

def main():
    if len(sys.argv) > 0:
        basepath = sys.argv[1]
    else: basepath = "/"
    static_to_public()
    generate_page("./content", "./template.html", "./public", basepath)

main()