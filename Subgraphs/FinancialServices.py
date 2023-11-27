from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
# EXAMPLE from Subgraphs.CompanyNodes import SpaceX_Data

class FinancialServicesGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.financial_services_sub_graph(graph, parent_node)

    def financial_services_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_financial_services = Node("node_financial_services", "node_financial_services")
        node_b = Node("LEER 1", "LEER 11")

        parent_node.connect(node_financial_services)
        node_financial_services.connect(node_b)

        graph.add_new_node_to_graph(node_financial_services)
        graph.add_new_node_to_graph(node_b)