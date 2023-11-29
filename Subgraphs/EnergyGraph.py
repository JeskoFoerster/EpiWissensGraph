from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from CompanyNodes import NextKraftwerke_Data
from CompanyNodes import RhenagRheinischeEnergie_Data
from IndustryNodes import Energy_Data


class EnergySubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.energy_create_sub_graph(graph, parent_node)

    def energy_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_energy = Node(Energy_Data.CONTENT, Energy_Data.TITEL, Energy_Data.IMAGE_NAME, radius=8, color=[204, 51, 255])
        node_nextkraftwerke = Node(NextKraftwerke_Data.CONTENT, NextKraftwerke_Data.TITEL, NextKraftwerke_Data.IMAGE_NAME)
        node_rhenagrheinischeenergie = Node(RhenagRheinischeEnergie_Data.CONTENT, RhenagRheinischeEnergie_Data.TITEL, RhenagRheinischeEnergie_Data.IMAGE_NAME)


        parent_node.connect(node_energy)
        node_energy.connect(node_nextkraftwerke)
        node_energy.connect(node_rhenagrheinischeenergie)

        graph.add_new_node_to_graph(node_energy)
        graph.add_new_node_to_graph(node_nextkraftwerke)
        graph.add_new_node_to_graph(node_rhenagrheinischeenergie)