from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from Subgraphs.CompanyNodes import SAP_Data
class SoftwareAsServiceGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.software_as_service_create_sub_graph(graph, parent_node)

    def software_as_service_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_software_as_service = Node("node_software_as_service", "node_software_as_service", radius=8, color=[204, 51, 255])
        node_sap = Node(SAP_Data.CONTENT, SAP_Data.TITEL, SAP_Data.IMAGE_NAME)

        parent_node.connect(node_software_as_service)
        node_software_as_service.connect(node_sap)

        graph.add_new_node_to_graph(node_software_as_service)
        graph.add_new_node_to_graph(node_sap)