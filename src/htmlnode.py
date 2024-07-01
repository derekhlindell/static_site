
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
            item = f'{k}="{v}" '
            prop_items += item

        return prop_items

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, None, None, props)
        self.value = value

    def __repr__(self):
        return f"LeafNode(value={self.value}, tag={self.tag}, props={self.props})"

    def leaf_to_html(self):
        if self.value is None:
            raise ValueError
        
        if self.tag is None:
            return str(self.value)

        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        leaf_props = self.props_to_html().rstrip()
        return f"<{self.tag} {leaf_props}>{self.value}</{self.tag}>"


test_leafnode = LeafNode("testing")
print(test_leafnode)