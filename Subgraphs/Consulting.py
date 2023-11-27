from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
# EXAMPLE from Subgraphs.CompanyNodes import SpaceX_Data

class ConsultingGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.consulting_create_sub_graph(graph, parent_node)

    def consulting_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_consulting = Node("node_consulting", "node_consulting")
        node_b = Node("LEER 1", "LEER 11")

        parent_node.connect(node_consulting)
        node_consulting.connect(node_b)

        graph.add_new_node_to_graph(node_consulting)
        graph.add_new_node_to_graph(node_b)