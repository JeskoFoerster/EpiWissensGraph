from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
# EXAMPLE from Subgraphs.CompanyNodes import SpaceX_Data
from Subgraphs.CompanyNodes import  Tesla_Data, Bmw_Data, Porsche_Data, Audi_Data
class AutomotiveIndustry:

    def __init__(self, parent_node: Node, graph: Graph):
        self.automotive_industry_sub_graph(graph, parent_node)

    def automotive_industry_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_automotive_industry = Node("node_automotive_industry", "node_automotive_industry")
        node_tesla = Node(Tesla_Data.CONTENT, Tesla_Data.TITEL, Tesla_Data.IMAGE_NAME)
        node_bmw = Node(Bmw_Data.CONTENT, Bmw_Data.TITEL, Bmw_Data.IMAGE_NAME)
        node_porsche = Node(Porsche_Data.CONTENT, Porsche_Data.TITEL, Porsche_Data.IMAGE_NAME)
        node_audi = Node(Audi_Data.CONTENT, Audi_Data.TITEL, Audi_Data.IMAGE_NAME)

        parent_node.connect(node_automotive_industry)
        node_automotive_industry.connect(node_tesla)
        node_automotive_industry.connect(node_bmw)
        node_automotive_industry.connect(node_porsche)
        node_automotive_industry.connect(node_audi)

        graph.add_new_node_to_graph(node_automotive_industry)
        graph.add_new_node_to_graph(node_tesla)
        graph.add_new_node_to_graph(node_bmw)
        graph.add_new_node_to_graph(node_porsche)
        graph.add_new_node_to_graph(node_audi)