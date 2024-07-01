
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
            raise NotImplementedError
        
        prop_items = ""
        for k, v in self.props.items():
            item = f'{k}="{v}"'
            prop_items += item + " "

        return prop_items


node1 = HTMLNode()
node2 = HTMLNode()

test_node = HTMLNode("h1", "h1 title", [node1, node2],{"href": "https://www.google.com", "target": "_blank", "blah": "blah blah"})
print(repr(test_node))
