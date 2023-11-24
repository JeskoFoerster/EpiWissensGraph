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

import pygame

from GraphModel import Graph
from View.GraphView import ScaleOffsetTransformer


class NodeFinder:
    """
    The NodeFinder class is responsible for locating a node in a graph
    based on the given coordinates (x, total_height). It allows identifying a node
    that is in proximity to the specified position by comparing
    distances between coordinates and applying a tolerance threshold based
    on the current zoom factor.
    """

    graph: Graph
    scale_offset_transformer: ScaleOffsetTransformer

    def __init__(self, graph, scale_offset_transformer):
        self.graph = graph
        self.scale_offset_transformer = scale_offset_transformer

    def find_node_at_position(self, x, y):
        # Find the node located at the given position
        for node in self.graph.nodes:
            node_x = node.x
            node_y = node.y
            # Calculate the distance between the given coordinates (x, total_height) and the node's coordinates
            distance = pygame.math.Vector2(x - node_x, y - node_y).length()
            # Check if the distance is less than a certain threshold dependent on self.scale_offset_transformer.zoom
            if distance < 8 / self.scale_offset_transformer.zoom:
                # If the distance is less, return the current node
                return node
        # If no matching node is found, return None
        return None
