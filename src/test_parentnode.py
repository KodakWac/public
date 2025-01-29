import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestParentNode(unittest.TestCase):

    def test_parent_node_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("p", "Sample text")])
    
    def test_parent_node_no_child(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None)

    def test_parent_node_with_valid_children(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
        ])
        expected_html = "<p><b>Bold text</b>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_parent_node_with_nested_children(self):
        node = ParentNode("div", [
            ParentNode("p", [
                LeafNode(None, "First paragraph."),
                LeafNode(None, "Another sentence."),
            ]),
            ParentNode("ul", [
                LeafNode("li", "Item 1"),
                LeafNode("li", "Item 2"),
            ]),
        ])
        expected_html = (
            "<div>"
            "<p>First paragraph.Another sentence.</p>"
            "<ul><li>Item 1</li><li>Item 2</li></ul>"
            "</div>"
        )
        self.assertEqual(node.to_html(), expected_html)



if __name__ == '__main__':
    unittest.main()