import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_basic_leaf_node(self):
        node = LeafNode("p", "This is a paragraph")
        expected = "<p>This is a paragraph</p>"
        self.assertEqual(node.to_html(), expected)
        
    def test_leaf_node_with_props(self):
        node = LeafNode("p", "This is a paragraph", props={"href": "https://google.com"})
        expected = '<p href="https://google.com">This is a paragraph</p>'
        self.assertEqual(node.to_html(), expected)
        
    def test_leaf_node_no_tag(self):
        node = LeafNode(None, "Just some text")
        expected = "Just some text"
        self.assertEqual(node.to_html(), expected)
        
    def test_leaf_node_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()



if __name__ == '__main__':
    unittest.main()