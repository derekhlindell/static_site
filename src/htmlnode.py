# tag = string
# value = string
# children = list
# props = dict

from textnode import TextNode, text_type

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ''
        
        prop_items = ""
        for k, v in self.props.items():
            item = f' {k}="{v}"'
            prop_items += item

        return prop_items


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        
        if self.tag is None:
            return str(self.value)
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(value={self.value}, tag={self.tag}, props={self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        
        html = []
        
        for node in self.children:
            if isinstance(node, LeafNode):
                html.append(node.to_html())
            else:
                html.append(node.to_html())

        return f"<{self.tag}>" + "".join(html) + f"</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children} {self.props})"

def text_node_to_html_node(text_node):
    match text_node:
        case "text":
            return LeafNode(None, text_node.text_type)
        case "bold":
            return "bold"
        case text_type.italic:
            return "italic"
        case text_type.code:
            return "code"
        case text_type.link:
            return "link"
        case text_type.image:
            return "image"

        case _:
            raise Exception(f"Invalid type: '{text_node}' is not a valid text_type")

TextNode("cool text", text_type.text)
text_node_to_html_node("text_type_text")