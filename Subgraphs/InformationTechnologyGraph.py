from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from CompanyNodes import ElectronicArts_Data, Netcologne_Data
from CompanyNodes import Coseon_Data, Google_Data, SchneiderElectric_Data, SAP_Data, Zeiss_Data, ParcIT_Data, \
    ReweDigital_Data
from IndustryNodes import InformationTechnology_Data


class InformationTechnologySubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.information_technology_create_sub_graph(graph, parent_node)

    def information_technology_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_information_technology = Node(InformationTechnology_Data.CONTENT, InformationTechnology_Data.TITEL, InformationTechnology_Data.IMAGE_NAME, radius=8, color=[204, 51, 255])
        node_schneiderelectric = Node(SchneiderElectric_Data.CONTENT, SchneiderElectric_Data.TITEL, SchneiderElectric_Data.IMAGE_NAME)
        node_coseon = Node(Coseon_Data.CONTENT, Coseon_Data.TITEL, Coseon_Data.IMAGE_NAME)
        node_electronicarts = Node(ElectronicArts_Data.CONTENT, ElectronicArts_Data.TITEL, ElectronicArts_Data.IMAGE_NAME)
        node_google = Node(Google_Data.CONTENT, Google_Data.TITEL, Google_Data.IMAGE_NAME)
        node_rewe_digital = Node(ReweDigital_Data.CONTENT, ReweDigital_Data.TITEL, ReweDigital_Data.IMAGE_NAME)
        node_parcIT = Node(ParcIT_Data.CONTENT, ParcIT_Data.TITEL, ParcIT_Data.IMAGE_NAME)
        node_zeiss = Node(Zeiss_Data.CONTENT, Zeiss_Data.TITEL, Zeiss_Data.IMAGE_NAME)
        node_sap = Node(SAP_Data.CONTENT, SAP_Data.TITEL, SAP_Data.IMAGE_NAME)
        node_netcologne= Node(Netcologne_Data.CONTENT, Netcologne_Data.TITEL, Netcologne_Data.IMAGE_NAME)

        parent_node.connect(node_information_technology)
        node_information_technology.connect(node_coseon)
        node_information_technology.connect(node_schneiderelectric)
        node_information_technology.connect(node_electronicarts)
        node_information_technology.connect(node_google)
        node_information_technology.connect(node_rewe_digital)
        node_information_technology.connect(node_parcIT)
        node_information_technology.connect(node_zeiss)
        node_information_technology.connect(node_sap)
        node_information_technology.connect(node_netcologne)


        graph.add_new_node_to_graph(node_information_technology)
        graph.add_new_node_to_graph(node_coseon)
        graph.add_new_node_to_graph(node_schneiderelectric)
        graph.add_new_node_to_graph(node_electronicarts)
        graph.add_new_node_to_graph(node_google)
        graph.add_new_node_to_graph(node_rewe_digital)
        graph.add_new_node_to_graph(node_parcIT)
        graph.add_new_node_to_graph(node_zeiss)
        graph.add_new_node_to_graph(node_sap)
        graph.add_new_node_to_graph(node_netcologne)
