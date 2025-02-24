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
    

class TestSplitImages(unittest.TestCase):
    def test_image_split(self):
        node = TextNode('This is text with an ![image](image.png) image and extra words', TextType.TEXT)
        new_node = split_nodes_image([node])

        self.assertListEqual(
            [
            TextNode('This is text with an ', TextType.TEXT),
            TextNode('image', TextType.IMAGE, 'image.png'),
            TextNode(' image and extra words', TextType.TEXT)
        ], new_node
        )

    def test_multiple_images(self):
        node = TextNode('This is text with ![image](url) ![image2](url2) images', TextType.TEXT)
        new_node = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode('This is text with ', TextType.TEXT),
                TextNode('image', TextType.IMAGE, 'url'),
                TextNode('image2', TextType.IMAGE, 'url2'),
                TextNode(' images', TextType.TEXT)
            ], new_node
        )
    
    def test_no_images(self):
        node = TextNode('There are no images', TextType.TEXT)
        new_node = split_nodes_image([node])

        self.assertListEqual([
            TextNode('There are no images', TextType.TEXT)
        ], new_node
        )


class TestSplitLinks(unittest.TestCase):
    def test_split_link(self):
        node = TextNode('There is one [link](url) in this text', TextType.TEXT)
        new_node = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode('There is one ', TextType.TEXT),
                TextNode('link', TextType.LINK, 'url'),
                TextNode(' in this text', TextType.TEXT)
            ], new_node
        )

    def test_split_many_links(self):
        node = TextNode('There are [link](url) many links [link2](url2) in this text', TextType.TEXT)
        new_node = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode('There are ', TextType.TEXT),
                TextNode('link', TextType.LINK, 'url'),
                TextNode(' many links ', TextType.TEXT),
                TextNode('link2', TextType.LINK, 'url2'),
                TextNode(' in this text', TextType.TEXT)
            ], new_node
        )

    def test_no_links(self):
        node = TextNode('There are no links', TextType.TEXT)
        new_node = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode('There are no links', TextType.TEXT)
            ], new_node
        )

class TestSplitTextNodes(unittest.TestCase):
    def test_two_splits(self):
        text = 'This is text with **bold** and ![image](url) and image'
        new_node = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode('This is text with ', TextType.TEXT),
                TextNode('bold', TextType.BOLD),
                TextNode(' and ', TextType.TEXT),
                TextNode('image', TextType.IMAGE, 'url'),
                TextNode(' and image', TextType.TEXT)
            ], new_node
        )
    
    def test_italic_split(self):
        text = 'Im over this project please let me *quit*'
        new_node = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode('Im over this project please let me ', TextType.TEXT),
                TextNode('quit', TextType.ITALIC)
            ], new_node
        )

    def test_many_splits(self):
        text = 'This is **the last** test with [link](url) im *done*'
        new_node = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode('This is ', TextType.TEXT),
                TextNode('the last', TextType.BOLD),
                TextNode(' test with ', TextType.TEXT),
                TextNode('link', TextType.LINK, 'url'),
                TextNode(' im ', TextType.TEXT),
                TextNode('done', TextType.ITALIC)
            ], new_node
        )

