from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from Subgraphs.CompanyNodes import AldiNord_Data


class ConsumerGoodsSubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.consumer_goods_create_sub_grapgh(graph, parent_node)

    def consumer_goods_create_sub_grapgh(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_ConsumerGoods = Node("Consumer Goods", "Consumer Goods")
        node_AldiNord = Node("", "")
        node_c = Node("", "")
        node_d = Node("Text", "Tesla")
        node_e = Node("Text", "Nvidia")

        node_AldiNord = Node(AldiNord_Data.CONTENT, AldiNord_Data.TITEL, AldiNord_Data.IMAGE_NAME)

        parent_node.connect(node_ConsumerGoods)
        node_ConsumerGoods.connect(node_AldiNord)
        node_ConsumerGoods.connect(node_c)
        node_ConsumerGoods.connect(node_d)
        node_ConsumerGoods.connect(node_e)
        node_ConsumerGoods.connect(node_AldiNord)

        graph.add_new_node_to_graph(node_ConsumerGoods)
        graph.add_new_node_to_graph(node_AldiNord)
        graph.add_new_node_to_graph(node_c)
        graph.add_new_node_to_graph(node_d)
        graph.add_new_node_to_graph(node_e)
        graph.add_new_node_to_graph(node_AldiNord)
