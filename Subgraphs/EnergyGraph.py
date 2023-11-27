from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from Subgraphs.CompanyNodes import NextKraftwerke_Data


class EnergySubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.energy_create_sub_graph(graph, parent_node)

    def energy_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_a = Node("energy description", "energy")
        node_nextkraftwerke = Node(NextKraftwerke_Data.CONTENT, NextKraftwerke_Data.TITEL, NextKraftwerke_Data.IMAGE_NAME)


        parent_node.connect(node_a)
        node_a.connect(node_nextkraftwerke)

        graph.add_new_node_to_graph(node_a)
        graph.add_new_node_to_graph(node_nextkraftwerke)