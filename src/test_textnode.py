import unittest
from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD_TEXT)
		node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
		self.assertEqual(node, node2)

	def test_not_eq(self):
		node = TextNode("Testing", TextType.ITALIC_TEXT)
		node2 = TextNode("Testing...", TextType.NORMAL_TEXT)
		self.assertNotEqual(node, node2)

	def test_eq_format(self):
		node = TextNode("Images", TextType.IMAGES)
		node2 = TextNode("Images", TextType.IMAGES)
		self.assertEqual(node, node2)

	def equal_url(self):
		node = TextNode("TESTING URL..", TextType.NORMAL, 'www.test.com')
		node2 = TextNode("TESTING URL..", TextType.NORMAL, 'www.test.com')
		self.assertEqual(node, node2)

if __name__ == "__main__":
	unittest.main()
