from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from CompanyNodes import PferdWerkzeuge_Data
from IndustryNodes import MechanicalEngineering_Data


class MechanicalEngineeringGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.mechanical_engineering_create_sub_graph(graph, parent_node)

    def mechanical_engineering_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_mechanical_engineering = Node(MechanicalEngineering_Data.CONTENT, MechanicalEngineering_Data.TITEL,
                                           MechanicalEngineering_Data.IMAGE_NAME, radius=8, color=[204, 51, 255])
        node_pferd = Node(PferdWerkzeuge_Data.CONTENT, PferdWerkzeuge_Data.TITEL, PferdWerkzeuge_Data.IMAGE_NAME)

        parent_node.connect(node_mechanical_engineering)
        node_mechanical_engineering.connect(node_pferd)

        graph.add_new_node_to_graph(node_mechanical_engineering)
        graph.add_new_node_to_graph(node_pferd)