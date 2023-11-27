from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from Subgraphs.CompanyNodes import Netflix_Data


class MediaAndEntertainmentSubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.media_and_entertainment_create_sub_graph(graph, parent_node)

    def media_and_entertainment_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_a = Node("information technology", "information technology")
        node_b = Node("Text", "Google")
        node_c = Node("Text", "amazon")
        node_d = Node("Text", "Tesla")
        node_e = Node("Text", "Nvidia")
        node_netflix = Node(Netflix_Data.CONTENT, Netflix_Data.TITEL)

        parent_node.connect(node_a)
        node_a.connect(node_b)
        node_a.connect(node_c)
        node_a.connect(node_d)
        node_a.connect(node_e)
        node_a.connect(node_netflix)

        graph.add_new_node_to_graph(node_a)
        graph.add_new_node_to_graph(node_b)
        graph.add_new_node_to_graph(node_c)
        graph.add_new_node_to_graph(node_d)
        graph.add_new_node_to_graph(node_e)
        graph.add_new_node_to_graph(node_netflix)