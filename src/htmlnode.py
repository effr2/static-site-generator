class HTMLNODE() :
	def __init__(self, tag=None, value=None, children=None, props=None) :
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self) :
		raise NotImplementedError()
	
	def props_to_html(self) :
		if self.props is None :
			return ""
		else:
			return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
	
	def __repr__(self):
		return f"HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNODE) :
	def __init__(self, tag=None, value=None, props=None) :
		super().__init__(tag, value, None, props)

	def to_html(self) :
		if self.value is None :
			raise ValueError("Leaf nodes must have a value")
		return f"{"" if self.tag is None else "<"+self.tag+" "}{self.props_to_html() + ">" if self.tag is not None else ""}{self.value}{"" if self.tag is None else "</"+self.tag+">"}"
	