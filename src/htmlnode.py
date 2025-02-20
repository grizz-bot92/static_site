class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        formatted_list = [f'{key}="{value}"' for key, value in self.props.items()]
         
        return " " + " ".join(formatted_list)
    
    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
            )

    def __repr__(self):
        return f'HTMLNode(TAG: {self.tag}, VALUE: {self.value}, CHILDREN: {self.children}, PROP:{self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    
    def to_html(self):
        if self.value == None:
            raise ValueError('All Leaf Nodes must have a value')
        
        if self.tag == None:
            return f'{self.value}'
        
        if self.props != None:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
        return f'<{self.tag}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)

    
    def to_html(self):
        result = ''

        if not self.tag:
            raise ValueError('Empty tag provided...')
        
        if not self.children:
            raise ValueError('Empty children provided...')
        
        for child in self.children:
            result += child.to_html()
        
        return f'<{self.tag}>{result}</{self.tag}>'
