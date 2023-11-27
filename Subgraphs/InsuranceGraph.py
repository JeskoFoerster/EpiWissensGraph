from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from Subgraphs.CompanyNodes import AldiNord_Data


class InsuranceSubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.Insurance_create_sub_grapgh(graph, parent_node)

    def Insurance_create_sub_grapgh(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_Insurance = Node("Ausgewählte Firmen die Versicherungen anbieten.", "Versicherungen", "insurance.png")

        parent_node.connect(node_Insurance)

        graph.add_new_node_to_graph(node_Insurance)

