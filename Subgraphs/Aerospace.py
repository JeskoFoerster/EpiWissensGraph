from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from Subgraphs.CompanyNodes import SpaceX_Data, Boeing_Data
from Subgraphs.IndustryNodes import Aerospace_Data
class AerospaceSubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.aerospace_create_sub_graph(graph, parent_node)

    def aerospace_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_aerospace = Node(Aerospace_Data.CONTENT, Aerospace_Data.TITEL, Aerospace_Data.IMAGE_NAME, radius=8, color=[204, 51, 255])
        node_spacex = Node(SpaceX_Data.CONTENT, SpaceX_Data.TITEL, SpaceX_Data.IMAGE_NAME)
        node_boeing = Node(Boeing_Data.CONTENT, Boeing_Data.TITEL, Boeing_Data.IMAGE_NAME)

        parent_node.connect(node_aerospace)
        node_aerospace.connect(node_spacex)
        node_aerospace.connect(node_boeing)

        graph.add_new_node_to_graph(node_aerospace)
        graph.add_new_node_to_graph(node_spacex)
        graph.add_new_node_to_graph(node_boeing)
