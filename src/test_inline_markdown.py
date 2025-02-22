import unittest
import re
from inline import *

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_bold(self):
        node = TextNode('This is text with a **bolded phrase** in the middle', TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)

        self.assertListEqual(
            [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bolded phrase", TextType.BOLD),
    TextNode(" in the middle", TextType.TEXT),
    ], new_nodes
        )

    def test_multi_bolded(self):
        node = TextNode('This is **text** with **many** bold words', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '**', TextType.BOLD)

        self.assertListEqual(
            [
                TextNode('This is ', TextType.TEXT),
                TextNode('text', TextType.BOLD),
                TextNode(' with ', TextType.TEXT),
                TextNode('many', TextType.BOLD),
                TextNode(' bold words', TextType.TEXT)
            ], new_node
        )
    
    def test_italic(self):
        node = TextNode('This is text with a *italic* word in the middle', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '*', TextType.ITALIC)
        
        self.assertListEqual(
            [
                TextNode('This is text with a ', TextType.TEXT),
                TextNode('italic', TextType.ITALIC),
                TextNode(' word in the middle', TextType.TEXT)
            ],
            new_node

        )
    def test_bold_italic(self):
        node = TextNode('This is text with **bold** word and *italic* word', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '**', TextType.BOLD)
        new_node = split_nodes_delimiter(new_node, '*', TextType.ITALIC)

        self.assertListEqual(
            [
                TextNode('This is text with ', TextType.TEXT),
                TextNode('bold', TextType.BOLD),
                TextNode(' word and ', TextType.TEXT),
                TextNode('italic', TextType.ITALIC),
                TextNode(' word', TextType.TEXT)
            ], new_node
        )

class TestLinks(unittest.TestCase):
    
    def test_extract_image(self):
        text = "![alt text](url)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt text", "url")])

    def test_extract_link(self):
        text = "[anchor](url)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("anchor", "url")])

    def test_many_images(self):
        text = "this is first ![alt text](url) and this is the second ![alt text2](url2)" 
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt text", "url"), ("alt text2", "url2")])

    def test_many_links(self):
        text = "this is the first [anchor](url) and this is the second [anchor2](url2)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("anchor", "url"), ("anchor2", "url2")])

    def test_no_images(self):
        text = "There are no images"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])