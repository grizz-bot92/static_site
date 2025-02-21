import unittest
from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_not_eq(self):
		node = TextNode("Testing", TextType.ITALIC)
		node2 = TextNode("Testing...", TextType.TEXT)
		self.assertNotEqual(node, node2)

	def test_eq_format(self):
		node = TextNode("Images", TextType.IMAGE)
		node2 = TextNode("Images", TextType.IMAGE)
		self.assertEqual(node, node2)

	def equal_url(self):
		node = TextNode("TESTING URL..", TextType.TEXT, 'www.test.com')
		node2 = TextNode("TESTING URL..", TextType.TEXT, 'www.test.com')
		self.assertEqual(node, node2)

if __name__ == "__main__":
	unittest.main()
