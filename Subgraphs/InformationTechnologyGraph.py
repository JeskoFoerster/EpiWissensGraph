from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from Subgraphs.CompanyNodes import Coseon_Data, SchneiderElectric_Data, ElectronicArts_Data


class InformationTechnologySubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.information_technology_create_sub_graph(graph, parent_node)

    def information_technology_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_information_technology = Node("information technology", "information technology")
        node_b = Node("Text", "Google")
        node_c = Node("Text", "amazon")
        node_d = Node("Text", "Tesla")
        node_e = Node("Text", "Nvidia")
        node_schneiderelectric = Node(SchneiderElectric_Data.CONTENT, SchneiderElectric_Data.TITEL, SchneiderElectric_Data.IMAGE_NAME)
        node_coseon = Node(Coseon_Data.CONTENT, Coseon_Data.TITEL, Coseon_Data.IMAGE_NAME)
        node_electronicarts = Node(ElectronicArts_Data.CONTENT, ElectronicArts_Data.TITEL, ElectronicArts_Data.IMAGE_NAME)

        parent_node.connect(node_information_technology)
        node_information_technology.connect(node_b)
        node_information_technology.connect(node_c)
        node_information_technology.connect(node_d)
        node_information_technology.connect(node_e)
        node_information_technology.connect(node_coseon)
        node_information_technology.connect(node_schneiderelectric)
        node_information_technology.connect(node_electronicarts)

        graph.add_new_node_to_graph(node_information_technology)
        graph.add_new_node_to_graph(node_b)
        graph.add_new_node_to_graph(node_c)
        graph.add_new_node_to_graph(node_d)
        graph.add_new_node_to_graph(node_e)
        graph.add_new_node_to_graph(node_coseon)
        graph.add_new_node_to_graph(node_schneiderelectric)
        graph.add_new_node_to_graph(node_electronicarts)
