from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all the companys in the subgraph
from CompanyNodes import ESLGaming_Data
from CompanyNodes import RiotGames_Data, Netflix_Data
from IndustryNodes import MediaAndEntertainment_Data


class MediaAndEntertainmentSubGraph:

    def __init__(self, parent_node: Node, graph: Graph):
        self.media_and_entertainment_create_sub_graph(graph, parent_node)

    def media_and_entertainment_create_sub_graph(self, graph: Graph, parent_node: Node):
        # Create Nodes
        node_media_and_entertainment = Node(MediaAndEntertainment_Data.CONTENT, MediaAndEntertainment_Data.TITEL, MediaAndEntertainment_Data.IMAGE_NAME, radius=8, color=[204, 51, 255])
        node_netflix = Node(Netflix_Data.CONTENT, Netflix_Data.TITEL, Netflix_Data.IMAGE_NAME)
        node_eslgaming = Node(ESLGaming_Data.CONTENT, ESLGaming_Data.TITEL, ESLGaming_Data.IMAGE_NAME)
        node_riotgames = Node(RiotGames_Data.CONTENT, RiotGames_Data.TITEL, RiotGames_Data.IMAGE_NAME)

        parent_node.connect(node_media_and_entertainment)
        node_media_and_entertainment.connect(node_netflix)
        node_media_and_entertainment.connect(node_eslgaming)
        node_media_and_entertainment.connect(node_riotgames)

        graph.add_new_node_to_graph(node_media_and_entertainment)
        graph.add_new_node_to_graph(node_netflix)
        graph.add_new_node_to_graph(node_eslgaming)
        graph.add_new_node_to_graph(node_riotgames)