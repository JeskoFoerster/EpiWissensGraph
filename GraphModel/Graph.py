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

from GraphModel.Node import Node


class Graph:
    """
    The Graph class represents a graph structure consisting of nodes.
    It provides functionality to manage and manipulate a collection of nodes,
    including adding new nodes and defining their initial positions.
    This class serves as the core data structure.
    """
    # Default team name associated with the graph
    team_name = "Die mutigen Mungos"
    # Initial central position for new nodes
    INITIAL_CENTER_POSITION = 5000000
    # List to store all nodes in the graph
    nodes = []

    def add_new_node_to_graph(self, node: Node):
        """
        Adds a new Node to the graph. This method calculates a random position for the node
        near the center of the graph's defined initial central position.

        :param: node: An instance of Node to be added to the graph.
        """
        node.x = random.randint(self.INITIAL_CENTER_POSITION - 5, self.INITIAL_CENTER_POSITION + 5)
        node.y = random.randint(self.INITIAL_CENTER_POSITION - 5, self.INITIAL_CENTER_POSITION + 5)
        self.nodes.append(node)
