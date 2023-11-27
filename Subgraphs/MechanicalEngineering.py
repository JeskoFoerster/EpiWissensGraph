from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
# EXAMPLE from Subgraphs.CompanyNodes import SpaceX_Data

class MechanicalEngineeringGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.mechanical_engineering_create_sub_graph(graph, parent_node)

    def mechanical_engineering_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_mechanical_engineering = Node("node_mechanical_engineering", "node_mechanical_engineering")
        node_b = Node("LEER 1", "LEER 11")

        parent_node.connect(node_mechanical_engineering)
        node_mechanical_engineering.connect(node_b)

        graph.add_new_node_to_graph(node_mechanical_engineering)
        graph.add_new_node_to_graph(node_b)