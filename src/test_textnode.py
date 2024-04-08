import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", "bold")
		node2 = TextNode("This is a text node", "bold")
		self.assertEqual(node, node2)
        
	def test_textnode_url_not_eq(self):
		node = TextNode("This is a text node", "bold")
		node2 = TextNode("This is a text node", "bold", "http://example.com")
		self.assertNotEqual(node, node2)
	
	def test_textnode_text_not_eq(self):
		node = TextNode("This is a text node", "bold")
		node2 = TextNode("This is a text node2", "bold")
		self.assertNotEqual(node, node2)

	def test_textnode_text_type_not_eq(self):
		node = TextNode("This is a text node", "bold")
		node2 = TextNode("This is a text node", "bold2")
		self.assertNotEqual(node, node2)
	
	def test_no_url(self):
		node = TextNode("This is a text node", "bold")
		self.assertIsNone(node.url, "URL should be None")
	
	def test_repr(self):
		node = TextNode("This is a text node", "bold")
		self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")


if __name__ == "__main__":
    unittest.main()
    