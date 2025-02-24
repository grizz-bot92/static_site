import unittest
from block_markdown import (
    markdown_to_blocks,
)

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
