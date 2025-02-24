def markdown_to_blocks(markdown):
    res = map(str.strip, markdown.split('\n\n'))
    return list(filter(None, res))

