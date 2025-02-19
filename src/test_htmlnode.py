import unittest
from htmlnode import HTMLNode

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
    

if __name__ == "__main__":
    unittest.main()