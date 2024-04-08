class TextNode ():

	def __init__(self, text, textType, url=None):
		self.text = text
		self.textType = textType
		self.url = url

	def __eq__(self, other_node):
		return (self.text == other_node.text 
		  and self.textType == other_node.textType 
		  and self.url == other_node.url)
	
	def __repr__(self):
		return f"TextNode({self.text}, {self.textType}, {self.url})"