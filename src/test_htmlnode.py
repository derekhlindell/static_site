import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank", "blah": "blah blah"})
        result = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank" blah="blah blah"'
        self.assertEqual(result, expected)

    def test_props_to_html_empty(self):
        # Create an instance of HTMLNode without props
        node = HTMLNode(None)
        result = node.props_to_html()
        expected = ''
        self.assertEqual(result, expected)

    def test_repr(self):
        node1 = HTMLNode()
        test_node = HTMLNode("h1", "h1 title", [node1],{"href": "https://www.google.com"})
        self.assertEqual(
            "HTMLNode(tag=h1, value=h1 title, children=[HTMLNode(tag=None, value=None, children=None, props=None)], props={'href': 'https://www.google.com'})"
            , repr(test_node)
        )

class TestLeafNode(unittest.TestCase):
    def test_to_html_empty(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()
        
    def test_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        result = node.to_html()
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(result, expected)

    def test_to_html_a(self):
        node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        result = node.to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(result, expected)

class TestParentNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        node = ParentNode(None, [])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        result = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(result, expected)
        
if __name__ == "__main__":
    unittest.main()
