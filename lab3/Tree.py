import unittest

class Tree:
  def __init__(self, value):
    self.value = value
    self.children = []
  def __str__ (self):
    nodes_to_visit = [self]
    string = "TreeClass("
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      string = string+'current_node.value=' + str(current_node.value) + ' '
      nodes_to_visit += current_node.children
    return string+")"
  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node) 
  def remove_child(self, child_node):
    print("Removing " + str(child_node.value) + " from " + str(self.value))
    self.children = [child for child in self.children 
                     if child is not child_node]
  def traverse(self):
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children
  @property
  def node_value(self, node_index):
    nodes_to_visit = [self]
    return nodes_to_visit[node_index].node_value
  @node_value.setter
  def node_value(self, node_index, new_value):
    self._children[node_index] = new_value
class TestCalculations(unittest.TestCase):
    def test_traverse(self):
        node1 = Tree("12")
        node2 = Tree("22")
        node3 = Tree("32")
        node4 = Tree("42")

        tree = Tree(100)
        tree.add_child(node1)
        tree.add_child(node2)
        tree.add_child(node3)
        tree.add_child(node4)
        tree.remove_child(node4)
        tree.traverse()
        self.assertEqual(tree.__str__(), "TreeClass(current_node.value=100 current_node.value=32 current_node.value=22 current_node.value=12 )", "traverse works wrong")
        #tree.node_value
        #tree.node_value = "2"
if __name__ == '__main__':
    unittest.main()        
#print(tree.__str__())
