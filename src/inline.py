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
     pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
     matches = re.findall(pattern, text)
     return matches

def extract_markdown_links(text):
     pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
     matches = re.findall(pattern, text)
     return matches

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue

        remaining = node.text

        for image in images:
            image_markdown = f'![{image[0]}]({image[1]})'
            before, remaining = remaining.split(image_markdown, 1)

            if before.strip():
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
        
        if remaining.strip():
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    
    return new_nodes
    
def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        
        remaining = node.text

        for link in links:
            link_markdown = f'[{link[0]}]({link[1]})'
            before, remaining = remaining.split(link_markdown, 1)

            if before.strip():
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
        
        if remaining.strip():
            new_nodes.append(TextNode(remaining, TextType.TEXT))
        
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes  = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '*', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE) 
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes