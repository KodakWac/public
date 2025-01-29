class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError


    def props_to_html(self):
        if self.props is None:
            return ""
        
        prop_list = []
        for key, value in self.props.items():
            prop_list.append(f' {key}="{value}"')

        return "".join(prop_list)
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
            if self.value is None:
                raise ValueError("A leaf node must have a value")
            
            if self.tag is None:
                return self.value
            
            if self.props is None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:  # Check `tag` is valid
            raise ValueError("A parent node must have a tag")
        if not children or len(children) == 0:  # Check `children` are valid
            raise ValueError("A parent node must have children")
        super().__init__(tag, None, children, props)

    def to_html(self):
        children_html = ""  

        children_html = ''.join(child.to_html() for child in self.children)

        if self.props is None: 
            return f"<{self.tag}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
