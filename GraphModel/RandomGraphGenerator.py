"""
Copyright (C) 2023 TH Köln – University of Applied Sciences

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import random

from GraphModel.Graph import Graph
from GraphModel.Node import Node
from queue import Queue


class RandomGraphGenerator:
    """
    Random GraphModel Generator. Creates Nodes based on the given amount_of_nodes in create_random_nodes.
    In the next step, the Nodes will be connected. There will be an amount_of_nodes of connections based on number_of_connections.
    """
    graph: Graph
    test_text = """# Heading 1 Hier steht Ihr Text.\n Dabei ist **das hier ein Beispiel** für fetten Text. Das hier ist ein *Beispiel für kursiven Text*.\n\n Das hier ist ein Beispiel für ***"kursiv und fett" text.*** Er kann mehrere Zeilen haben.\n ## Heading 2\n Dies ist ein einfaches Beispiel für ein scrollbares Textfenster in Pygame. \n Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \n \n Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \n\n### Heading 3 \n Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Hier steht Ihr Text. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua End."""

    def __init__(self, graph: Graph):
        self.graph = graph

    def create_random_hierarchical_graph(self, amount_of_nodes):
        """
        Generate a random hierarchical graph with a single root node.

        :param: amount_of_nodes: The total number of nodes to create in the graph.
        :param: mass_of_nodes: The mass value to assign to each node.
        """
        node_stack = Queue()
        root_node = self.__create_node(self.test_text, "Titel of this Node", "image_placeholder.png")
        self.graph.add_new_node_to_graph(root_node)
        amount_of_nodes -= 1
        amount_of_children = random.randint(8, 8)
        node_stack.put(root_node)

        if amount_of_nodes > 0:
            self.__create_random_hierarchical_graph_children(amount_of_nodes,
                                                             node_stack,
                                                             amount_of_children)

    def __create_random_hierarchical_graph_children(self,
                                                    amount_of_nodes,
                                                    node_stack: Queue,
                                                    amount_of_children):
        """
        Recursively create child nodes for a parent node in a random hierarchical graph.

        :param: amount_of_nodes: The remaining number of nodes to create.
        :param: node_stack: A queue containing parent nodes.
        :param: mass_of_nodes: The mass value to assign to each node.
        """
        parent_node = node_stack.get()

        for i in range(amount_of_children):
            if amount_of_nodes == 0:
                break

            node = self.__create_node(self.test_text, "Titel of this Node", "image_placeholder.png")
            self.graph.add_new_node_to_graph(node)
            parent_node.connect(node)
            amount_of_nodes -= 1
            node_stack.put(node)

        if amount_of_nodes > 0:
            amount_of_children = random.randint(1, 10)
            self.__create_random_hierarchical_graph_children(amount_of_nodes,
                                                             node_stack,
                                                             amount_of_children)

    def create_random_nodes(self, amount_of_nodes, number_of_connections):
        """
        Create random nodes and connect them to form a graph.

        :param: amount_of_nodes: The total number of nodes to create.
        :param: number_of_connections: The desired number of connections between nodes.
        :param: screen_width: The width of the screen or canvas.
        :param: screen_height: The height of the screen or canvas.
        """

        # Random distribution force directed graphs will not work if all graph_nodes are on the same position
        for i in range(amount_of_nodes):
            # Fruchterman Reingold Random Node derivation: Konzentriert auf einen zentralen Bereich
            # x = random.randint((screen_width/4)-10, (screen_width/4)+10)
            # total_height = random.randint((screen_height/4)-10, (screen_height/4)+10)

            self.__create_node(self.test_text, "Titel of this Node", "image_placeholder.png")

        self.__random_connect_nodes(number_of_connections)

        # self.fruchterman_reingold_layout(self.graph_nodes, 10000, 10000, 10000)

    def __create_node(self, description, titel, image_path):
        """
        Create a new graph node and add it to the list of nodes.

        :param: description: A description or label for the node.
        :param: x: The x-coordinate of the node's position.
        :param: total_height: The total_height-coordinate of the node's position.
        :param: node_mass: The mass value to assign to the node.
        :return: The newly created graph node.
        """
        node = Node(description, titel, image_path)
        self.graph.add_new_node_to_graph(node)
        return node

    def __random_connect_nodes(self, num_connections):
        """
        Create random connections (edges) between graph nodes.

        :param: num_connections: The desired number of connections to create.
        """
        if len(self.graph.nodes) < 2:
            return
        connection_to_make = num_connections

        while connection_to_make > 0:
            node1 = random.choice(self.graph.nodes)
            node2 = random.choice(self.graph.nodes)

            # Avoid connecting a barnes_hut_node to itself or duplicate connections
            if node1 != node2 and node2.uuid not in node1.get_connected_nodes():
                node1.connect(node2)

            connection_to_make -= 1
