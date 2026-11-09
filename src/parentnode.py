from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:[HTMLNode], props:str = None):
        super().__init__(tag,None,children,props)

    def to_html(self) -> str:
        if self.tag == None:
            raise ValueError("ParentNode has no tag")
        if self.children == None:
            raise ValueError("ParentNode has no children")
        child_html = ""
        for child in self.children:
            child_html = child_html+child.to_html()
        if self.props != None:
            properties = ""
            for key, value in self.props.items():
                properties = properties+" "+str(key)+'"'+str(value)+'"'
            parent = "<"+self.tag+properties+">"+child_html+"</"+self.tag+">"
            return parent
        if self.props == None:
            parent = "<"+self.tag+">"+child_html+"</"+self.tag+">"
            return parent

    def __repr__(self, other):
        rep = f"LeafNode(<{self.tag}{self.props}>{self.children}</{self.tag}>)"
        return rep