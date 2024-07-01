
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


test_node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank", "blah": "blah blah"})
