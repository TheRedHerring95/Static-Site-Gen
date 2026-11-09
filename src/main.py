from statictopublic import static_to_public
from mdtohtml import generate_page
from textnode import TextNode
from textnode import TextType

def main():
    static_to_public()
    generate_page("./content/index.md", "./template.html", "./public/index.html")

main()