from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from CompanyNodes import Axa_Data, Hdi_Data
from IndustryNodes import Insurance_Data


class InsuranceSubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.Insurance_create_sub_grapgh(graph, parent_node)

    def Insurance_create_sub_grapgh(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_Insurance = Node(Insurance_Data.CONTENT, Insurance_Data.TITEL, Insurance_Data.IMAGE_NAME, radius=8, color=[204, 51, 255])
        node_Axa = Node(Axa_Data.CONTENT, Axa_Data.TITEL, Axa_Data.IMAGE_NAME)
        node_Hdi = Node(Hdi_Data.CONTENT, Hdi_Data.TITEL, Hdi_Data.IMAGE_NAME)

        parent_node.connect(node_Insurance)
        node_Insurance.connect(node_Axa)
        node_Insurance.connect(node_Hdi)

        graph.add_new_node_to_graph(node_Insurance)
        graph.add_new_node_to_graph(node_Axa)
        graph.add_new_node_to_graph(node_Hdi)

