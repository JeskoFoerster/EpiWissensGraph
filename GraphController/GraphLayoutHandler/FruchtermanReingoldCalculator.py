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

import math


class FruchtermanReingoldCalculator:
    """
    The FruchtermanReingoldCalculator class implements the Fruchterman-Reingold algorithm for graph layout.
    This algorithm positions nodes in a graph based on a simulation of forces, where nodes repel each other like
    charged particles and are pulled closer by edges acting like springs. The goal of this algorithm is to position
    the nodes of the graph in a way that visually represents the structure of the graph, minimizing edge crossings
    and balancing node distribution.
    """

    def __init__(self):
        pass

    def fruchterman_reingold_layout(self, nodes, width, height, iterations, k=1.0):
        """
        Applies the Fruchterman-Reingold algorithm to a set of nodes to calculate their positions.

        :param: nodes: A list of nodes in the graph. Each node should have properties like x, y, disp_x, and disp_y.
        :param: width: The width of the area over which the nodes should be distributed.
        :param: height: The height of the area over which the nodes should be distributed.
        :param: iterations: The number of iterations to run the algorithm, adjusting node positions in each iteration.
        :param: k: A constant influencing the strength of the repulsive forces between nodes. A higher value increases
                  the separation between nodes. This parameter can be tuned to optimize layout appearance.
        """
        for _ in range(iterations):
            for node in nodes:
                node.disp_x = 0
                node.disp_y = 0

            for i, node1 in enumerate(nodes):
                for j, node2 in enumerate(nodes):
                    if i < j:
                        dx = node2.x - node1.x
                        dy = node2.y - node1.y
                        distance = max(0.1, math.sqrt(dx ** 2 + dy ** 2))

                        # Adjust the force calculation based on connections
                        if node2.uuid in node1.__connected_nodes or node1.uuid in node2.__connected_nodes:
                            force = (k ** 2) * 1 + len(node2.__connected_nodes) * 1 + len(node1.__connected_nodes)
                            """
                            Force of attraction:
                            The distance as a damping factor is not used here to keep the force of attraction constant.
                            Thus, connected nodes are drawn together to form clusters while unconnected 
                            nodes distance themselves. 
                            Nodes that have more connections have a stronger force of attraction.
                            """
                        else:
                            force = (-(k ** 2) / distance)  # Abstoßungskraft

                        disp_x = (dx / distance) * force
                        disp_y = (dy / distance) * force

                        node1.disp_x += disp_x
                        node1.disp_y += disp_y
                        node2.disp_x -= disp_x
                        node2.disp_y -= disp_y

            for node in nodes:
                node.x += node.disp_x
                node.y += node.disp_y
                # barnes_hut_node.x = max(0, min(width, barnes_hut_node.x))
                # barnes_hut_node.total_height = max(0, min(height, barnes_hut_node.total_height))
