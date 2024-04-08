import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image

class TestInLineMarkdown(unittest.TestCase):
	def test_bold(self):
		nodes = split_nodes_delimiter([TextNode("Hello **world**", text_type_text)], "**", text_type_bold)
		self.assertEqual(nodes, [TextNode("Hello ", text_type_text), TextNode("world", text_type_bold)])

	def test_italic(self):
		nodes = split_nodes_delimiter([TextNode("Hello *world*", text_type_text)], "*", text_type_italic)
		self.assertEqual(nodes, [TextNode("Hello ", text_type_text), TextNode("world", text_type_italic)])
	
	def test_code(self):
		nodes = split_nodes_delimiter([TextNode("Hello `world`", text_type_text)], "`", text_type_code)
		self.assertEqual(nodes, [TextNode("Hello ", text_type_text), TextNode("world", text_type_code)])
	
	def test_double_bold(self):
		nodes = split_nodes_delimiter([TextNode("Hello **world** **world**", text_type_text)], "**", text_type_bold)
		self.assertEqual(nodes, [TextNode("Hello ", text_type_text), TextNode("world", text_type_bold), TextNode(" ", text_type_text), TextNode("world", text_type_bold)])
	
	def test_extract_markdown_images(self):
		text = "![Alt text](/path/to/img.jpg)"
		images = extract_markdown_images(text)
		self.assertEqual(images, [("Alt text", "/path/to/img.jpg")])
	
	def test_extract_markdown_links(self):
		text = "[Link text](https://www.example.com)"
		links = extract_markdown_links(text)
		self.assertEqual(links, [("Link text", "https://www.example.com")])
	
	def test_split_image(self):
		node = TextNode(
		"This is text with an ![image](https://www.example.com/image.png)",
		text_type_text)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
		[
			TextNode("This is text with an ", text_type_text),
			TextNode("image", text_type_image, "https://www.example.com/image.png"),
		],
		new_nodes)

	def test_split_image_single(self):
		node = TextNode(
		"![image](https://www.example.com/image.png)",
		text_type_text)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
		[
			TextNode("image", text_type_image, "https://www.example.com/image.png"),
		],
		new_nodes)
	
	def test_split_images(self):
		node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
			new_nodes
		)
	def test_split_links(self):
		node = TextNode(
			"This is text with a [link](https://www.example.com) and another [second link](https://www.example.com)",
			text_type_text,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with a ", text_type_text),
				TextNode("link", text_type_link, "https://www.example.com"),
				TextNode(" and another ", text_type_text),
				TextNode(
					"second link", text_type_link, "https://www.example.com"
				),
			],
			new_nodes
		)
	
	
if __name__ == "__main__":
	unittest.main()