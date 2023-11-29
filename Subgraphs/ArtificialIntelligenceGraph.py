from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
# EXAMPLE from Subgraphs.CompanyNodes import SpaceX_Data

class ArtificialIntelligenceGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.artificial_intelligence_create_sub_graph(graph, parent_node)

    def artificial_intelligence_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_artificial_intelligence = Node("artificial_intelligence", "artificial_intelligence", radius=8, color=[204, 51, 255])
        node_b = Node("LEER 1", "LEER 11")

        parent_node.connect(node_artificial_intelligence)
        node_artificial_intelligence.connect(node_b)

        graph.add_new_node_to_graph(node_artificial_intelligence)
        graph.add_new_node_to_graph(node_b)