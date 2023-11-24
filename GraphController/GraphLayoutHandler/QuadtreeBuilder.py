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

import numpy as np


class BarnesHutNode:
    """
    The BarnesHutNode class represents a node in the Barnes-Hut quadtree, used for spatial partitioning
    in the Barnes-Hut optimization algorithm. Each node represents a quadrant of space and is used to
    efficiently calculate forces between particles in a large system, such as nodes in a graph layout algorithm.
    """
    def __init__(self, x, y, size):
        """
        Initializes a BarnesHutNode with a specified position and size.

        :param: x: The x-coordinate of the center of the quadrant.
        :param: y: The y-coordinate of the center of the quadrant.
        :param: size: The size of the quadrant, crucial for defining the space it covers and for subdividing into
        child quadrants.

        The Barnes-Hut algorithm recursively divides the space into four quadrants, and each node in this tree
        represents one of these quadrants. The size of this quadrant is needed
        to define which space each node covers.
        self.size is determined when a new node is created by dividing the size of the parent quadrant
        is divided by 2. This ensures that the size of the child nodes is exactly half the size of the parent quadrant.
        of the size of the parent quadrant.

        The size of the first node should be chosen so that it adequately covers the entire space in which your
        particles or objects are located. Ideally, the size of the first node should be large enough
        that it contains all the particles in the space. If the size is too small, this can lead to
        the algorithm to perform an unnecessarily large number of subdivisions, which can affect performance.
        In turn, if the size is too large, accurate calculations may be affected.

        """
        self.x = x
        self.y = y
        self.size = size
        self.center_of_mass_x = 0.0
        self.center_of_mass_y = 0.0
        self.total_mass = 0.0
        self.children = [None] * 4


class QuadtreeBuilder:
    def insert_node(self, barnes_hut_node, graph_node):
        """
        Insert a graph node into a Barnes-Hut node in the tree structure.

        :param: barnes_hut_node: The Barnes-Hut node representing a cluster of particles.
        :param: graph_node: The graph node representing a single particle to be inserted.
        """
        if barnes_hut_node.total_mass == 0:
            barnes_hut_node.center_of_mass_x = graph_node.x
            barnes_hut_node.center_of_mass_y = graph_node.y
            barnes_hut_node.total_mass = graph_node.mass
        else:
            total_mass = barnes_hut_node.total_mass + graph_node.mass
            barnes_hut_node.center_of_mass_x = (
                                                       barnes_hut_node.center_of_mass_x * barnes_hut_node.total_mass + graph_node.x * graph_node.mass) / total_mass
            barnes_hut_node.center_of_mass_y = (
                                                       barnes_hut_node.center_of_mass_y * barnes_hut_node.total_mass + graph_node.y * graph_node.mass) / total_mass
            barnes_hut_node.total_mass = total_mass

        if barnes_hut_node.size > 1:
            """
            Determine which of the four possible quadrants the graph_node belongs to 
            and create a new barnes_hut_node if no quadrant exists in this area. 
            """
            quadrant = 0
            if graph_node.x > barnes_hut_node.x + barnes_hut_node.size / 2:
                quadrant += 1
            if graph_node.y > barnes_hut_node.y + barnes_hut_node.size / 2:
                quadrant += 2

            if barnes_hut_node.children[quadrant] is None:
                # Create a new child node if it doesn't exist already
                child_size = barnes_hut_node.size / 2
                child_x = barnes_hut_node.x + (quadrant % 2) * child_size
                child_y = barnes_hut_node.y + (quadrant // 2) * child_size
                barnes_hut_node.children[quadrant] = BarnesHutNode(child_x, child_y, child_size)

            # Recursively insert the graph_node into the appropriate child barnes_hut_node
            self.insert_node(barnes_hut_node.children[quadrant], graph_node)

    def calculate_force(self, barnes_hut_node, graph_node, force_modification=1.0, theta=3.0):
        """
        Calculate the force between a Barnes-Hut node and a graph node.

        :param: barnes_hut_node: The Barnes-Hut node representing a cluster of particles.
        :param: graph_node: The graph node representing a single particle.
        :param: force_modification: A scaling factor for the force calculation.
        :param: theta: The threshold parameter for deciding whether to approximate distant clusters.
        :return: The force components (fx, fy) acting on the graph node.
        """
        dx = barnes_hut_node.center_of_mass_x - graph_node.x
        dy = barnes_hut_node.center_of_mass_y - graph_node.y
        distance = max(np.sqrt(dx * dx + dy * dy), 1e-10)
        # distance = max(0.1, math.sqrt(dx ** 2 + dy ** 2))

        if barnes_hut_node.size / distance < theta or barnes_hut_node.total_mass == 0:
            # If the barnes_hut_node is sufficiently far away or empty, treat it as a single graph_node
            # force = graph_node.mass * barnes_hut_node.total_mass / (distance * distance)
            force = -((graph_node.mass * barnes_hut_node.total_mass / (distance ** 1.2)) * force_modification)

            angle = np.arctan2(dy, dx)
            fx = force * np.cos(angle)
            fy = force * np.sin(angle)
            return fx, fy
        else:
            # Otherwise, recursively calculate forces from the children
            total_fx, total_fy = 0.0, 0.0
            for child in barnes_hut_node.children:
                if child is not None:
                    fx, fy = self.calculate_force(child, graph_node, force_modification, theta)
                    total_fx += fx
                    total_fy += fy
            return total_fx, total_fy
