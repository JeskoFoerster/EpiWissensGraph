from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
# EXAMPLE from Subgraphs.CompanyNodes import SpaceX_Data
from CompanyNodes import Microsoft_Data
from IndustryNodes import CloudComputing_Data


class CloudComputingGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.cloud_computing_create_sub_graph(graph, parent_node)

    def cloud_computing_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_cloud_computing = Node(CloudComputing_Data.CONTENT, CloudComputing_Data.TITEL,
                                    CloudComputing_Data.IMAGE_NAME, radius=8, color=[204, 51, 255])
        node_microsoft = Node(Microsoft_Data.CONTENT, Microsoft_Data.TITEL, Microsoft_Data.IMAGE_NAME)

        parent_node.connect(node_cloud_computing)
        node_cloud_computing.connect(node_microsoft)

        graph.add_new_node_to_graph(node_cloud_computing)
        graph.add_new_node_to_graph(node_microsoft)