from htmlnode import *
from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
           result.append(node)
           continue   

        split_nodes = []        
        parts = node.text.split(delimiter)
        
        if len(parts) % 2 == 0:
            raise Exception('Missing closing delimiter')

        for i in range(len(parts)):
            if parts[i] == '':
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(parts[i], text_type))
        result.extend(split_nodes)   
    return result

def extract_markdown_images(text):
     matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
     return matches

def extract_markdown_links(text):
     matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
     return matches