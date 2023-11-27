from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from Subgraphs.CompanyNodes import AldiNord_Data


class ConsumerGoodsSubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.consumer_goods_create_sub_grapgh(graph, parent_node)

    def consumer_goods_create_sub_grapgh(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_consumer_goods = Node("Consumer Goods", "Consumer Goods")
        node_b = Node("Text", "Google")
        node_c = Node("Text", "amazon")
        node_d = Node("Text", "Tesla")
        node_e = Node("Text", "Nvidia")
        node_AldiNord = Node(AldiNord_Data.CONTENT, AldiNord_Data.TITEL, AldiNord_Data.IMAGE_NAME)

        parent_node.connect(node_consumer_goods)
        node_consumer_goods.connect(node_b)
        node_consumer_goods.connect(node_c)
        node_consumer_goods.connect(node_d)
        node_consumer_goods.connect(node_e)
        node_consumer_goods.connect(node_AldiNord)

        graph.add_new_node_to_graph(node_consumer_goods)
        graph.add_new_node_to_graph(node_b)
        graph.add_new_node_to_graph(node_c)
        graph.add_new_node_to_graph(node_d)
        graph.add_new_node_to_graph(node_e)
        graph.add_new_node_to_graph(node_AldiNord)
