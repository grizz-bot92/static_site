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

    def __repr__(self):
        return f'HTMLNode(TAG: {self.tag}, VALUE: {self.value}, CHILDREN: {self.children}, PROP:{self.props})'

        