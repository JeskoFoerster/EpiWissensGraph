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

from GraphController.GraphLayoutHandler.QuadtreeBuilder import QuadtreeBuilder, BarnesHutNode
from GraphModel.Node import Node
import numpy as np


class BarnesHutManager:
    # Example:
    quad_tree_builder = QuadtreeBuilder()

    # Create a root barnes_hut_node representing the entire simulation space
    root_node = BarnesHutNode(0, 0, 0)
    x_location = 0
    y_location = 0
    barnes_hut_size = 100

    def __init__(self, x_location, y_location, barnes_hut_size):
        """

        :param: x_location: x location of the Barnes Hut Area
        :param: y_location: total_height location of the Barnes Hut Area
        :param: barnes_hut_size: Used to calculate the max Area which is divided into quadrants.
        """
        self.x_location = x_location
        self.y_location = y_location
        self.barnes_hut_size = barnes_hut_size

    def insert_nodes_into_quadtree(self, graph_nodes: [Node]):
        self.root_node = BarnesHutNode(self.x_location, self.y_location, self.barnes_hut_size)
        # Insert particles into the Barnes-Hut tree
        for graph_node in graph_nodes:
            self.quad_tree_builder.insert_node(self.root_node, graph_node)

    def barnes_hut_layout(self,
                          graph_nodes: [Node],
                          attraction_force_modification,
                          repulsion_force_modification,
                          barnes_hut_approximation_level,
                          max_velocity,
                          time_step=0.9):
        """
        Application of repulsion and attraction effects to each node. For repulsion, the Barnes-Hut algorithm is used.
        Attraction is based on the connection of nodes. Nodes that are connected to each other are attracted.

        :param: time_step: controlling the speed and position update
        :param: max_velocity: Maximum velocity of a Node to limit velocity to prevent excessive movements
        :param: graph_nodes: List of all Nodes
        :param: attraction_force_modification: Modification of the Attraction Force a value lower than 1 will damp force
            and a higher Value will amplify the force.
        :param: repulsion_force_modification: Modification of the Repulsion Force a value lower than 1 will damp force
            and a higher Value will amplify the force.
        :param: barnes_hut_approximation_level: In the Barnes-Hut algorithm, θ (theta) is a parameter used to control
            the approximation level of the algorithm. It is often referred to as the "opening angle" or
            "criterion angle."
        """
        self.insert_nodes_into_quadtree(graph_nodes)

        # Calculate force between nodes (attraction)
        self.__calculate_attraction_force(graph_nodes, max_velocity, time_step, attraction_force_modification)

        # Calculate force between nodes (repulsion)
        self.__calculate_repulsion_force(barnes_hut_approximation_level, graph_nodes, max_velocity,
                                         repulsion_force_modification, time_step)

    def __calculate_repulsion_force(self, barnes_hut_approximation_level, graph_nodes, max_velocity,
                                    repulsion_force_modification, time_step):
        """
           This method calculates the repulsion forces between nodes in the graph
           using a specific approximation technique (Barnes-Hut approximation).

           For each node in the graph, it computes the x and total_height components of the resulting force
           acting on the node due to the repulsion from other nodes.


            :param: barnes_hut_approximation_level (float): The level of Barnes-Hut approximation to use.
            :param: graph_nodes (list of Node): List of nodes in the graph.
            :param: max_velocity (float): The maximum allowed velocity for nodes.
            :param: repulsion_force_modification (float): A modification factor for the repulsion force.
            :param: time_step (float): The time step for the simulation.

           The method updates the acceleration, velocity, and position of each node in the graph
           based on the calculated forces and the simulation parameters. It also limits the node's
           velocity to the specified maximum, if necessary.
           """
        for graph_node in graph_nodes:
            disp_x, disp_y = self.quad_tree_builder.calculate_force(self.root_node, graph_node,
                                                                    repulsion_force_modification,
                                                                    barnes_hut_approximation_level)

            # Initialize velocities and accelerations for nodes
            # graph_node.velocity_x = 0.0
            # graph_node.velocity_y = 0.0
            # graph_node.acceleration_x = 0.0
            # graph_node.acceleration_y = 0.0

            graph_node.acceleration_x += disp_x / graph_node.mass
            graph_node.acceleration_y += disp_y / graph_node.mass

            graph_node.velocity_x += graph_node.acceleration_x * time_step
            graph_node.velocity_y += graph_node.acceleration_y * time_step

            velocity_magnitude = np.sqrt(graph_node.velocity_x ** 2 + graph_node.velocity_y ** 2)
            if velocity_magnitude > max_velocity:
                graph_node.velocity_x = graph_node.velocity_x * max_velocity / velocity_magnitude
                graph_node.velocity_y = graph_node.velocity_y * max_velocity / velocity_magnitude

            # Update node positions using the calculated velocities
        for graph_node in graph_nodes:
            graph_node.x += graph_node.velocity_x * time_step
            graph_node.y += graph_node.velocity_y * time_step

    def __calculate_attraction_force(self, graph_nodes: [Node], max_velocity, time_step, force_modification=0.1):
        """
        Calculate Attraction Force based on Connections:
        Barnes hat calculates a basic repulsive force between all nodes. At the same time there is this
        attraction force based on the connections of the nodes to each other. Thus, other nodes as well as
        cluster are repelled by other nodes.

        :param: time_step: Controlling the speed and position update
        :param: max_velocity: Maximum velocity of a Node to limit velocity to prevent excessive movements
        :param: graph_nodes: List of all Nodes
        :param: force_modification:  Modification value for the attractive force.
        Force will be multiplied by this value.
        """

        for node in graph_nodes:
            for connected_node in node.get_connected_nodes().values():
                node.velocity_x = 0.0
                node.velocity_y = 0.0
                node.acceleration_x = 0.0
                node.acceleration_y = 0.0

                connected_node.velocity_x = 0.0
                connected_node.velocity_y = 0.0
                connected_node.acceleration_x = 0.0
                connected_node.acceleration_y = 0.0

                dx = connected_node.x - node.x
                dy = connected_node.y - node.y
                distance = max(np.sqrt(dx * dx + dy * dy), 1e-10)
                # distance = max(0.1, math.sqrt(dx ** 2 + dy ** 2))
                if distance > 10:
                    # attraction is relative to distance to counter the effect of repulsion
                    attraction_force = (force_modification ** 2) * distance * force_modification * node.mass

                    disp_x = dx * attraction_force
                    disp_y = dy * attraction_force

                    node.acceleration_x += disp_x / node.mass
                    node.acceleration_y += disp_y / node.mass
                    connected_node.acceleration_x -= disp_x / connected_node.mass
                    connected_node.acceleration_y -= disp_y / connected_node.mass

                    node.velocity_x += node.acceleration_x * time_step
                    node.velocity_y += node.acceleration_y * time_step
                    connected_node.velocity_x -= connected_node.acceleration_x * time_step
                    connected_node.velocity_y -= connected_node.acceleration_y * time_step

                    node_velocity_magnitude = np.sqrt(node.velocity_x ** 2 + node.velocity_y ** 2)
                    connected_node_velocity_magnitude = np.sqrt(
                        connected_node.velocity_x ** 2 + connected_node.velocity_y ** 2)

                    if node_velocity_magnitude > max_velocity:
                        node.velocity_x = node.velocity_x * max_velocity / node_velocity_magnitude
                        node.velocity_y = node.velocity_y * max_velocity / node_velocity_magnitude

                    if connected_node_velocity_magnitude > max_velocity:
                        connected_node.velocity_x = connected_node.velocity_x * max_velocity / connected_node_velocity_magnitude
                        connected_node.velocity_y = connected_node.velocity_y * max_velocity / connected_node_velocity_magnitude

                    # Update node positions using the calculated velocities
                    node.x += node.velocity_x * time_step
                    node.y += node.velocity_y * time_step
                    connected_node.x -= connected_node.velocity_x * time_step
                    connected_node.y -= connected_node.velocity_y * time_step
