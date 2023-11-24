from GraphModel.Graph import Graph
from GraphModel.Node import Node
from Structured_Knowledge_Graph_Example.NodeData import OnlineSourceExample_Data, \
    LiteratureSourceExample_Data
from Structured_Knowledge_Graph_Example.NodeData import HowToNode_Data, PaperSourceExample_Data


class MainGraph:

    def __init__(self, graph: Graph):
        # Umwandeln in ein Attribut sie steht nun der gesamten Klasse zur Verfügung
        self.literature_source_example_node = None
        self.build_graph(graph)

    def build_graph(self, graph):
        # Anlegen der Knoten
        how_to_node = Node(HowToNode_Data.CONTENT, HowToNode_Data.TITEL, HowToNode_Data.IMAGE_NAME)
        online_source_example_node = Node(OnlineSourceExample_Data.CONTENT, OnlineSourceExample_Data.TITEL)
        self.literature_source_example_node = Node(LiteratureSourceExample_Data.CONTENT, LiteratureSourceExample_Data.TITEL)
        paper_source_example_node = Node(PaperSourceExample_Data.CONTENT, PaperSourceExample_Data.TITEL)

        # Verbindungen der Knoten
        how_to_node.connect(online_source_example_node)
        how_to_node.connect(self.literature_source_example_node)
        how_to_node.connect(paper_source_example_node)

        # Hinzufügen des Knoten zum Graphen
        graph.add_new_node_to_graph(how_to_node)
        graph.add_new_node_to_graph(online_source_example_node)
        graph.add_new_node_to_graph(self.literature_source_example_node)
        graph.add_new_node_to_graph(paper_source_example_node)

    def get_literature_source_example_node(self):
        return self.literature_source_example_node
