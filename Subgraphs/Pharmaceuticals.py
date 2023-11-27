from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
# EXAMPLE from Subgraphs.CompanyNodes import SpaceX_Data

class PharmaceuticalsGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.pharmaceuticals_create_sub_graph(graph, parent_node)

    def pharmaceuticals_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_pharmaceuticals = Node("node_pharmaceuticals", "node_pharmaceuticals")
        node_b = Node("LEER 1", "LEER 11")

        parent_node.connect(node_pharmaceuticals)
        node_pharmaceuticals.connect(node_b)

        graph.add_new_node_to_graph(node_pharmaceuticals)
        graph.add_new_node_to_graph(node_b)