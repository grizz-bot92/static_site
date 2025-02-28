import unittest
from block_markdown import markdown_to_blocks
from blocktypes import block_to_block_type, BlockType


class TestBlocks(unittest.TestCase):
    def test_split_block(self):
        text = '# This is a heading.\n\n This is a paragraph.'
        block = markdown_to_blocks(text)

        self.assertListEqual(
                [
                    '# This is a heading.',
                    'This is a paragraph.'
                ], block
        )

    def test_split_empty_string(self):
        text = ''
        block = markdown_to_blocks(text)

        self.assertListEqual(
                [
                    
                ], block
        )
    
    def test_space_around(self):
        text = ' leading and trailing space should be stripped.    \n\nlike this!'
        block = markdown_to_blocks(text)

        self.assertListEqual([
            'leading and trailing space should be stripped.',
            'like this!'
        ], block
        )
    
    def test_many_newlines(self):
        text = 'how many\n\n\n\nmany\n\nnewlines\n\n\n\ndo i need?'
        block = markdown_to_blocks(text)

        self.assertListEqual([
            'how many',

            'many',
            'newlines',

            'do i need?'

        ], block)

    def test_block_to_block_type(self):
        block = ('# heading')
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = ('```\ncode\n```')
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = ('> quote\n> quote')
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = ('1. Hello\n2. World')
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = ('- Un\n- Ordered')
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = ('This is a paragraph. It has no starting special char.')
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

