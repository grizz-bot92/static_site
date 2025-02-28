from enum import Enum
from htmlnode import HTMLNode

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_block_type(markdown):
    current_num = 1
    lines = markdown.split('\n')
    first_line = lines[0]
    last_line = lines[-1]

    if not markdown.strip():
        return BlockType.PARAGRAPH
    
    for line in lines:
        if not line.startswith(f'{current_num}. '):
            break
        current_num +=1
    else:
        return BlockType.ORDERED_LIST

    if all(line.startswith('* ') or line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST
    
    if all(line.startswith('> ') for line in lines):
        return BlockType.QUOTE
    
    if first_line == ('```') and last_line == ('```') and len(lines) > 2:
        return BlockType.CODE
    
    count = 0

    for char in first_line:
        if char == '#':
            count +=1
        else:
            break
    
    if 1 <= count <= 6 and first_line[count] == ' ':
        return BlockType.HEADING
    
    return BlockType.PARAGRAPH






