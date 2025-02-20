import unittest
from htmlnode import HTMLNode, LeafNode

class testHTMLNode(unittest.TestCase):

    def test_eq_single_prop(self):
        node = HTMLNode(props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')
    
    def test_eq_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def not_eq_tag(self):
        node = HTMLNode(tag='a')
        self.assertNotEqual(node.tag,'p')

class TestLeafNode(unittest.TestCase):
    
    def test_eq(self):
        node = LeafNode("p", "Hello, World")
        self.assertEqual(node.to_html(), '<p>Hello, World</p>') 
    
    def not_eq_tag(self):
        node = LeafNode("a")
        self.assertNotEqual(node.tag, 'p')

    def test_no_children(self):
        node = LeafNode(None, "Hello")
        self.assertEqual(node.to_html(), "Hello")

if __name__ == "__main__":
    unittest.main()