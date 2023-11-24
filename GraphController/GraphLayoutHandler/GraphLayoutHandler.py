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
from View.GraphView import IScaleOffsetTransformer
from .BarnesHutManager import BarnesHutManager
from .IGraphLayoutHandler import IGraphLayoutHandler
from .QuadtreeBuilder import BarnesHutNode


class AutoLayoutHandler(IGraphLayoutHandler):
    """
    AutoLayoutHandler is a class that implements automatic graph layout using the Barnes-Hut optimization algorithm.
    This class is responsible for positioning the nodes in a graph efficiently, aiming to make the graph
    easy to understand and visually appealing. It uses the Barnes-Hut algorithm to approximate the forces
    between nodes in large graphs, which helps in significantly speeding up the layout calculation.
    """
    barnesHutManager = None
    scaleOffsetTransformer: IScaleOffsetTransformer
    screen = None
    draw_color = (0, 0, 0)
    graph: Graph

    def __init__(self,
                 x_location,
                 y_location,
                 barnes_hut_size,
                 scale_offset_transformer: IScaleOffsetTransformer,
                 screen,
                 draw_color,
                 graph: Graph):
        """
        Initializes an AutoLayoutHandler instance.

        :param: x_location: The x-coordinate for the Barnes-Hut quadtree root.
        :param: y_location: The y-coordinate for the Barnes-Hut quadtree root.
        :param: barnes_hut_size: The size of the Barnes-Hut quadtree area.
        :param: scale_offset_transformer: An instance of IScaleOffsetTransformer for transforming coordinates.
        :param: screen: The Pygame screen object where the graph is rendered.
        :param: draw_color: The color used for drawing the Barnes-Hut area.
        :param: graph: The graph whose nodes will be arranged.
        """

        self.graph = graph
        self.barnesHutManager = BarnesHutManager(x_location, y_location, barnes_hut_size)
        self.barnesHutManager.insert_nodes_into_quadtree(graph.nodes)
        self.scaleOffsetTransformer = scale_offset_transformer
        self.screen = screen
        self.draw_color = draw_color

        # Modifications for Auto Layout
        self.attraction_force_modification = 0.1
        self.repulsion_force_modification = len(graph.nodes)
        self.max_velocity = 5

    def auto_layout(self, pause_layout):
        """
        Performs automatic layout for graphs.

        :param: pause_layout (bool): A flag indicating whether layout should be paused.

        If `pause_layout` is False, this method performs automatic layout for the graph.
        It involves various calculations for arranging nodes and edges.
        The method also measures execution time and prints it to the console.

        """
        # GraphLayoutHandler on loop
        if not pause_layout:
            # Starte die Zeitmessung
            # start_time = time.time()
            # Suitable Force Relation for Graphs N = 100
            # self.barnesHutManager.barnes_hut_layout(self.nodeGenerator.nodes, 0.05, 1000.0, 2.0, 0.5, 0.9)

            # Suitable Force Relation for Graphs N = 800
            # self.barnesHutManager.barnes_hut_layout(self.graph.nodes, 0.05, 10.0, 3.0, 100, 0.9)
            self.barnesHutManager.barnes_hut_layout(self.graph.nodes, self.attraction_force_modification,
                                                    self.repulsion_force_modification, 3.0, self.max_velocity, 0.5)

            # Beende die Zeitmessung
            # end_time = time.time()
            # Berechne die Differenz zwischen Start- und Endzeit, um die Ausführungszeit zu erhalten
            #execution_time = end_time - start_time

            # print("Die Ausführungszeit beträgt:", execution_time, "Sekunden")

    def show_barnes_hut_area(self):
        """
        Request a visualisation of the Barnes Hut Areas.
        """
        bhn = self.barnesHutManager.root_node
        self.__visualize_barnes_hut_area(bhn)

    def __visualize_barnes_hut_area(self, bhn: BarnesHutNode):
        """
        Recursively draw the Barnes-Hut tree areas.

        :param: bhn: The Barnes-Hut node to draw.
        """
        # Get scaled coordinates and size based on the zoom level.
        scaled_x, scaled_y = self.scaleOffsetTransformer.get_scaled_coordinates(bhn)
        scaled_size = int(bhn.size * self.scaleOffsetTransformer.zoom)

        # Draw the current node as a square.
        rect = pygame.Rect(scaled_x - scaled_size, scaled_y - scaled_size, 2 * scaled_size, 2 * scaled_size)
        pygame.draw.rect(self.screen, self.draw_color, rect, 1)

        # Draw straight lines from the x and total_height positions
        # to the edges of the quadrant based on 'size'.
        pygame.draw.line(self.screen, self.draw_color, (scaled_x, scaled_y - scaled_size),
                         (scaled_x, scaled_y + scaled_size))
        pygame.draw.line(self.screen, self.draw_color, (scaled_x - scaled_size, scaled_y),
                         (scaled_x + scaled_size, scaled_y))

        # Draw the children, if they exist.
        for child in bhn.children:
            if child is not None:
                self.__visualize_barnes_hut_area(child)
