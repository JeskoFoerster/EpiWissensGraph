from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
# EXAMPLE from Subgraphs.CompanyNodes import SpaceX_Data

class CybersecurityGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.cybersecurity_create_sub_graph(graph, parent_node)

    def cybersecurity_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_cybersecurity = Node("node_cybersecurity", "node_cybersecurity")
        node_b = Node("LEER 1", "LEER 11")

        parent_node.connect(node_cybersecurity)
        node_cybersecurity.connect(node_b)

        graph.add_new_node_to_graph(node_cybersecurity)
        graph.add_new_node_to_graph(node_b)