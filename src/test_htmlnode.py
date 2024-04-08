import unittest
from htmlnode import HTMLNODE, LeafNode, ParentNode


class TestHTMLNODE(unittest.TestCase):
	def test_repr(self):
		node = HTMLNODE("This is a text node", "bold")
		self.assertEqual(repr(node), "HTMLNODE(This is a text node, bold, None, None)")
	
	def test_no_props(self):
		node = HTMLNODE("This is a text node", "bold")
		self.assertIsNone(node.props, "Props should be None")
	
	def test_props_to_html(self):
		node = HTMLNODE("This is a text node", "bold", props={"class": "bold", "id": "1"})
		self.assertEqual(node.props_to_html(), 'class="bold" id="1"')
	
	def test_props_to_html_no_props(self):    
		node = HTMLNODE("This is a text node", "bold")
		self.assertEqual(node.props_to_html(), "")
class TestLeafNode(unittest.TestCase):
	def test_to_html_no_children(self):
		node = LeafNode("h1", "This is a header")
		self.assertEqual(node.to_html(), "<h1>This is a header</h1>")

	def test_to_html_no_tag(self):
		node = LeafNode(None, "This is a header")
		self.assertEqual(node.to_html(), "This is a header")
	
	def test_to_html_no_value(self):
		node = LeafNode("h1")
		self.assertRaises(ValueError, node.to_html)

class TestParentNode(unittest.TestCase):
	def test_to_html_no_tag(self):
		node = ParentNode([LeafNode("h1", "This is a header")])
		self.assertRaises(ValueError, node.to_html)
	
	def test_to_html_no_children(self):
		node = ParentNode(None, "div")
		self.assertRaises(ValueError, node.to_html)
	
	def test_to_html(self):
		node = ParentNode([LeafNode("h1", "This is a header")], "div")
		self.assertEqual(node.to_html(), "<div><h1>This is a header</h1></div>")


if __name__ == "__main__":
    unittest.main()