from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
           result.append(node)
           continue

        first = node.text.find(delimiter)
        
        if first == -1:
            result.append(node)
            continue
                
        second = node.text.find(delimiter, first + 1)

        if second == -1:
            raise Exception('Missing closing delimiter')
                
        parts = node.text.split(delimiter)

        for i, part in enumerate(parts):
            if i % 2 == 0:
                node = TextNode(part, TextType.TEXT)
                result.append(node)
            else:
                node = TextNode(part, text_type)
                result.append(node)