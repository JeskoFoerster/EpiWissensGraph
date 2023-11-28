from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
# EXAMPLE from Subgraphs.CompanyNodes import SpaceX_Data
from Subgraphs.CompanyNodes import  Secunet_Data
class CybersecurityGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.cybersecurity_create_sub_graph(graph, parent_node)

    def cybersecurity_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_cybersecurity = Node("node_cybersecurity", "node_cybersecurity")
        node_secunet = Node(Secunet_Data.CONTENT, Secunet_Data.TITEL, Secunet_Data.IMAGE_NAME)

        parent_node.connect(node_cybersecurity)
        node_cybersecurity.connect(node_secunet)

        graph.add_new_node_to_graph(node_cybersecurity)
        graph.add_new_node_to_graph(node_secunet)