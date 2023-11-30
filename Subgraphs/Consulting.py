from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from CompanyNodes import SollersConsulting_Data
from IndustryNodes import Consulting_Data


class ConsultingGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.consulting_create_sub_graph(graph, parent_node)

    def consulting_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_consulting = Node(Consulting_Data.CONTENT, Consulting_Data.TITEL, Consulting_Data.IMAGE_NAME, radius=8, color=[204, 51, 255])
        node_sollersConsulting = Node(SollersConsulting_Data.CONTENT, SollersConsulting_Data.TITEL, SollersConsulting_Data.IMAGE_NAME)

        parent_node.connect(node_consulting)
        node_consulting.connect(node_sollersConsulting)

        graph.add_new_node_to_graph(node_consulting)
        graph.add_new_node_to_graph(node_sollersConsulting)