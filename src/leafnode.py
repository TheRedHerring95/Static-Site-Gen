from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag:str, value:str, props:dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("No value listed on leaf")
        if self.tag == None:
            return self.value
        else:
            if self.props != None:
                properties = ""
                for key, value in self.props.items():
                    properties = properties+" "+str(key)+str(value)
                htm = f"<{self.tag}{properties}>{self.value}</{self.tag}>"
                return htm
            else:
                htm = f"<"+self.tag+">"+str(self.value)+"</"+self.tag+">"
                return htm

    def __repr__(self, other):
        rep = f"LeafNode(<{self.tag}{self.props}>{self.value}</{self.tag}>)"
        return rep