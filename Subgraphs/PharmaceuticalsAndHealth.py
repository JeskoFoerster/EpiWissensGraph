from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from Subgraphs.CompanyNodes import Innovas_Data

class PharmaceuticalsAndHealthGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.pharmaceuticals_create_sub_graph(graph, parent_node)

    def pharmaceuticals_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_pharmaceuticalsAndHealth = Node("Gesundheitswesen", "Gesundheitswesen", radius=8, color=[204, 51, 255])
        node_innovas = Node(Innovas_Data.CONTENT, Innovas_Data.TITEL, Innovas_Data.IMAGE_NAME)

        parent_node.connect(node_pharmaceuticalsAndHealth)
        node_pharmaceuticalsAndHealth.connect(node_innovas)

        graph.add_new_node_to_graph(node_pharmaceuticalsAndHealth)
        graph.add_new_node_to_graph(node_innovas)