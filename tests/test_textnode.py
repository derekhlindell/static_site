import unittest

from src.textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "Boot.dev")
        node2 = TextNode("This is a text node", "bold", "Boot.dev")
        self.assertEqual(node, node2)

    def test_different_url(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", "Boot.dev")
        self.assertNotEqual(node, node2)
    
    def test_different_text(self):
        node = TextNode("This is a text node", "bold",)
        node2 = TextNode("This is also a text node", "bold",)
        self.assertNotEqual(node, node2)

    def test_different_style(self):
        node = TextNode("This is a text node", "bold",)
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "text", "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()
