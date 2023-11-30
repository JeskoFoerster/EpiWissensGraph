from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
# from Subgraphs.CompanyNodes import
from IndustryNodes import  FinancialServices_Data
class FinancialServicesGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.financial_services_sub_graph(graph, parent_node)

    def financial_services_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_financial_services = Node(FinancialServices_Data.CONTENT, FinancialServices_Data.TITEL,
                                       FinancialServices_Data.IMAGE_NAME, radius=8, color=[204, 51, 255])
        node_b = Node("LEER 1", "LEER 11")

        parent_node.connect(node_financial_services)
        node_financial_services.connect(node_b)

        graph.add_new_node_to_graph(node_financial_services)
        graph.add_new_node_to_graph(node_b)