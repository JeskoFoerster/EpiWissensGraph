from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from Subgraphs.CompanyNodes import AldiNord_Data, Lidl_Data, Action_Data, Obi_Data, Nestle_Data, Otto_Data


class ConsumerGoodsSubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.consumer_goods_create_sub_grapgh(graph, parent_node)

    def consumer_goods_create_sub_grapgh(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_ConsumerGoods = Node("## Beschreibung:\nAusgewählte Firmen die Konsumgüter vertreiben.\n\n## Quellen:\n-[Bild] https://www.adito.de/knowhow/blog/konsumgueter", "Konsumgüter", "konsum.png", radius=8, color=[204, 51, 255])

        node_AldiNord = Node(AldiNord_Data.CONTENT, AldiNord_Data.TITEL, AldiNord_Data.IMAGE_NAME)
        node_Lidl = Node(Lidl_Data.CONTENT, Lidl_Data.TITEL, Lidl_Data.IMAGE_NAME)
        node_Action = Node(Action_Data.CONTENT, Action_Data.TITEL, Action_Data.IMAGE_NAME)
        node_Obi = Node(Obi_Data.CONTENT, Obi_Data.TITEL, Obi_Data.IMAGE_NAME)
        node_Nestle = Node(Nestle_Data.CONTENT, Nestle_Data.TITEL, Nestle_Data.IMAGE_NAME)
        node_Otto = Node(Otto_Data.CONTENT, Otto_Data.TITEL, Otto_Data.IMAGE_NAME)

        parent_node.connect(node_ConsumerGoods)
        node_ConsumerGoods.connect(node_AldiNord)
        node_ConsumerGoods.connect(node_Lidl)
        node_ConsumerGoods.connect(node_Action)
        node_ConsumerGoods.connect(node_Obi)
        node_ConsumerGoods.connect(node_Nestle)
        node_ConsumerGoods.connect(node_Otto)

        graph.add_new_node_to_graph(node_ConsumerGoods)
        graph.add_new_node_to_graph(node_AldiNord)
        graph.add_new_node_to_graph(node_Lidl)
        graph.add_new_node_to_graph(node_Action)
        graph.add_new_node_to_graph(node_Obi)
        graph.add_new_node_to_graph(node_Nestle)
        graph.add_new_node_to_graph(node_Otto)
