from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from Subgraphs.CompanyNodes import Netflix_Data, ESLGaming_Data, RiotGames_Data


class MediaAndEntertainmentSubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.media_and_entertainment_create_sub_graph(graph, parent_node)

    def media_and_entertainment_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_a = Node("media and entertainment description", "media and entertainment")
        node_netflix = Node(Netflix_Data.CONTENT, Netflix_Data.TITEL, Netflix_Data.IMAGE_NAME)
        node_eslgaming = Node(ESLGaming_Data.CONTENT, ESLGaming_Data.TITEL, ESLGaming_Data.IMAGE_NAME)
        node_riotgames = Node(RiotGames_Data.CONTENT, RiotGames_Data.TITEL, RiotGames_Data.IMAGE_NAME)

        parent_node.connect(node_a)
        node_a.connect(node_netflix)
        node_a.connect(node_eslgaming)
        node_a.connect(node_riotgames)

        graph.add_new_node_to_graph(node_a)
        graph.add_new_node_to_graph(node_netflix)
        graph.add_new_node_to_graph(node_eslgaming)
        graph.add_new_node_to_graph(node_riotgames)