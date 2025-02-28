from htmlnode import *
from block_markdown import *
from blocktypes import *
from textnode import *
from inline import *

def markdown_to_html_node(markdown):
        blocked_markdown = markdown_to_blocks(markdown)

        parent_node  = HTMLNode('div', None, None, [])

        for block in blocked_markdown:
            block_type = block_to_block_type(block)
        

        return parent_node

def text_to_children(text):
      nodes = split_nodes_delimiter(text)
      nodes = extract_markdown_images(nodes)
      nodes = extract_markdown_links(nodes)