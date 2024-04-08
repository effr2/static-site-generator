from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode ():

	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other_node):
		return (self.text == other_node.text 
		  and self.text_type == other_node.text_type 
		  and self.url == other_node.url)
	
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
	if text_type_text == text_node.text_type: 
		return LeafNode(None, text_node.text)
	elif text_type_bold == text_node.text_type:
		return LeafNode("b", text_node.text)
	elif text_type_italic == text_node.text_type:
		return LeafNode("i", text_node.text)
	elif text_type_code == text_node.text_type:
		return LeafNode("code", text_node.text)
	elif text_type_link == text_node.text_type:
		return LeafNode("a", text_node.text, {"href": text_node.url})
	elif text_type_image == text_node.text_type:
		return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
	else:
		raise ValueError(f"Invalid text type : {text_node.text_type}")
	
