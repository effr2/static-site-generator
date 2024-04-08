from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image
import re
def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for old_node in old_nodes:
		if delimiter in old_node.text and old_node.text_type == text_type_text:
			delimiter_count = old_node.text.count(delimiter)
			
			if delimiter_count % 2 != 0 :
				raise ValueError(f"Invalid delimiter count: {delimiter_count}")
			
			text_split = old_node.text.split(delimiter)
			split_nodes = []

			for i in range(len(text_split)):
				if text_split[i] == "":
					continue
				
				if i % 2 != 0:
					split_nodes.append(TextNode(text_split[i], text_type))
				else:
					split_nodes.append(TextNode(text_split[i], text_type_text))

			new_nodes.extend(split_nodes)
		else:
			new_nodes.append(old_node)
	return new_nodes

def extract_markdown_images(text):
	regex_pattern = r"!\[(.*?)\]\((.*?)\)"
	return re.findall(regex_pattern, text)

def extract_markdown_links(text):
	regex_pattern = r"\[(.*?)\]\((.*?)\)"
	return re.findall(regex_pattern, text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes