import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a text node", "bold")
        node2 = HTMLNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_url(self):
        node = HTMLNode("This is a text node", "bold", "Boot.dev")
        node2 = HTMLNode("This is a text node", "bold", "Boot.dev")
        self.assertEqual(node, node2)

    def test_different_url(self):
        node = HTMLNode("This is a text node", "bold", None)
        node2 = HTMLNode("This is a text node", "bold", "Boot.dev")
        self.assertNotEqual(node, node2)
    
    def test_different_text(self):
        node = HTMLNode("This is a text node", "bold",)
        node2 = HTMLNode("This is also a text node", "bold",)
        self.assertNotEqual(node, node2)

    def test_none(self):
        node = HTMLNode(tag=None, value=None, children=None, props=None)
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_repr(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        test_node = HTMLNode("h1", "h1 title", [node1, node2],{"href": "https://www.google.com", "target": "_blank", "blah": "blah blah"})
        self.assertEqual(
            "HTMLNode(tag=h1, value=h1 title, children=[HTMLNode(tag=None, value=None, children=None, props=None), HTMLNode(tag=None, value=None, children=None, props=None)], props={'href': 'https://www.google.com', 'target': '_blank', 'blah': 'blah blah'})"
            , repr(test_node)
        )

if __name__ == "__main__":
    unittest.main()
