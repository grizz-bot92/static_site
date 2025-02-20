import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):

    def test_no_children(self):
        node = ParentNode("p", [])
        self.assertEqual(node.to_html(), '<p></p>')
    
    def test_one_child(self):
        node = ParentNode(
            "p", [
                LeafNode("b", "Bold text")
            ]
        )

        self.assertEqual(node.to_html(), '<p><b>Bold text</b></p>')

    def test_many_children(self):
        node = ParentNode("div", [
            ParentNode("p", [
                LeafNode("i", "Italic text")
            ]),

            ParentNode("p", [
                LeafNode("b", "Bold text")
            ])
        ])

        self.assertEqual(node.to_html(), '<div><p><i>Italic text</i></p><p><b>Bold text</b></p></div>')
    
    def raise_error(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None)
            node.to_html()
            
if __name__ == "__main__":
    unittest.main()