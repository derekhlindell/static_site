# tag = string
# value = string
# children = list
# props = dict


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
    def __init__(self, tag:str, children:list, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self, current_nodes=[]):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        
        '''
        Otherwise, it should return a string representing the HTML tag of the node and its children. 
        This should be a recursive method (albeit with each recursion using a new node instance). 
        I iterated over all the children and called to_html on each, concatenating the results 
        and injecting them between the opening and closing tags of the parent.
        '''
        nodes = []

        for node in self.children:
            if isinstance(node, LeafNode):
                new_node = LeafNode(node.tag, node.value, node.props)
                nodes.append(new_node.to_html())
            else:
                new_node = ParentNode(node.tag, node.children)
                nodes.extend(self.to_html(current_nodes))
        
        return nodes

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"

node = ParentNode(
    "p",
    [
        LeafNode("b", "LeafNode 1"),
        ParentNode(
            "p",
            [
                LeafNode("b", "LeafNode 2a"),
                LeafNode(None, "LeafNode 2b"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "LeafNode 3a"),
                        LeafNode(None, "LeafNode 3b"),
                    ],
                )
            ],
        )
    ],
)

print(node.to_html())