from GraphModel.Graph import Graph
from GraphModel.Node import Node


class SubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.create_sub_graph(graph, parent_node)

    def create_sub_graph(self, graph: Graph, parent_node: Node):

        # Create Nodes
        node_a = Node("Text", "Node A")
        node_b = Node("Text", "Node B")
        node_c = Node("Text", "Node C")
        node_d = Node("Text", "Node D")
        node_e = Node("Text", "Node E")

        parent_node.connect(node_a)
        node_a.connect(node_b)
        node_a.connect(node_c)
        node_a.connect(node_d)
        node_a.connect(node_e)

        graph.add_new_node_to_graph(node_a)
        graph.add_new_node_to_graph(node_b)
        graph.add_new_node_to_graph(node_c)
        graph.add_new_node_to_graph(node_d)
        graph.add_new_node_to_graph(node_e)
