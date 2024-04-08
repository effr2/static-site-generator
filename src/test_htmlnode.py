import unittest
from htmlnode import HTMLNODE

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
    


if __name__ == "__main__":
    unittest.main()