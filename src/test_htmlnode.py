import unittest

from htmlnode import HTMLNode



class TestHTMLNode(unittest.TestCase):
    def test_empty_prop(self):
    
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_single_prop(self):
        node = HTMLNode(props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

    def test_multi_prop(self):
        node = HTMLNode(props={"href": "https://google.com",
                               "target": "_blank"})
        self.assertEqual(
        node.props_to_html(),
        ' href="https://google.com" target="_blank"'
    )
        


if __name__ == '__main__':
    unittest.main()