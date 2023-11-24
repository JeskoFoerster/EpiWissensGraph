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

from collections import deque

import pygame

from GraphModel import Node, Graph, SelectedNodeContainer
from View.GraphView import IScaleOffsetTransformer
from View.GraphView.IGraphVisualizer import IGraphVisualizer


class GraphVisualizer(IGraphVisualizer):
    """
    The GraphVisualizer class is responsible for rendering a graph onto a screen using Pygame.
    It manages the drawing of nodes and edges and handles the visual representation of the graph,
    including highlighting selected nodes and their subtrees.
    """
    scaleOffsetTransformer: IScaleOffsetTransformer
    selectedNodeContainer: SelectedNodeContainer
    graph: Graph
    screen = None
    edge_color = (0, 0, 0)
    node_color = (0, 0, 0)
    selected_node_color = (0, 0, 0)
    selected_node_subtree_color = (0, 0, 0)
    BASE_NODE_DIAMETER = 5
    BASE_NODE_HIGHLIGHT_DIAMETER = 8
    SELECTED_NODE_SPECIAL_HIGHLIGHT_DIAMETER = 12  # Neuer größerer Durchmesser für den selektierten Knoten
    show_node_labels = True

    def __init__(self, scale_offset_transformer: IScaleOffsetTransformer,
                 screen, graph: Graph, selected_node_container: SelectedNodeContainer,
                 edge_color, node_color, selected_node_color, selected_node_subtree_color):
        """
        Initializes the GraphVisualizer with necessary components and visual properties.

        :param: scale_offset_transformer: An instance of IScaleOffsetTransformer for coordinate scaling and transformation.
        :param: screen: The Pygame screen object where the graph will be drawn.
        :param: graph: The graph to be visualized.
        :param: selected_node_container: A container holding the currently selected node, if any.
        :param: edge_color: The color to be used for drawing graph edges.
        :param: node_color: The color to be used for drawing nodes.
        :param: selected_node_color: The color to be used for highlighting the selected node.
        :param: selected_node_subtree_color: The color to be used for highlighting the subtree of the selected node.
        """

        self.scaleOffsetTransformer = scale_offset_transformer
        self.graph = graph
        self.selectedNodeContainer = selected_node_container
        self.screen = screen

        self.edge_color = edge_color
        self.node_color = node_color
        self.selected_node_color = selected_node_color
        self.selected_node_subtree_color = selected_node_subtree_color
        pygame.font.init()  # Initialisieren Sie das Schriftart-System
        self.font = pygame.font.Font(None, 16)  # Wählen Sie eine Schriftart und Größe

    def draw_text(self, text, position):
        """
        Zeichnet Text an einer bestimmten Position auf dem Bildschirm.

        :param text: Der zu zeichnende Text.
        :param position: Eine Tupel-Position (x, y), an der der Text gezeichnet wird.
        """
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, position)

    def draw_graph(self):
        """
        Renders the graph on the screen, drawing both nodes and edges.
        This method also handles the highlighting of the selected node and its subtree if applicable.
        """
        # Zeichne Kanten
        for node in self.graph.nodes:
            for connected_node in node.get_connected_nodes().values():
                scaled_start = self.scaleOffsetTransformer.get_scaled_coordinates(node)
                scaled_end = self.scaleOffsetTransformer.get_scaled_coordinates(connected_node)
                pygame.draw.line(self.screen, self.edge_color, scaled_start, scaled_end)

        if self.selectedNodeContainer.selected_node is not None:
            self.highlight_selected_subtree(self.selectedNodeContainer.selected_node)

        # Zeichne Knoten
        for node in self.graph.nodes:
            scaled_x, scaled_y = self.scaleOffsetTransformer.get_scaled_coordinates(node)
            pygame.draw.circle(self.screen, self.node_color, (scaled_x, scaled_y), self.BASE_NODE_DIAMETER)

        if self.show_node_labels:
            # Zeichne den Titel der Knoten
            for node in self.graph.nodes:
                scaled_x, scaled_y = self.scaleOffsetTransformer.get_scaled_coordinates(node)
                self.draw_text(node.titel, (
                scaled_x, scaled_y + self.BASE_NODE_DIAMETER + 5))  # Positionieren Sie den Text unter dem Knoten

    def highlight_selected_subtree(self, node: Node):
        """
        Highlights the subtree rooted at a specified node. This method visually differentiates
        the selected node and its connected nodes from the rest of the graph.

        :param: node: The root node of the subtree to be highlighted.
        """
        if node is None:
            return

        stack = deque()
        stack.append(node)

        visited_nodes = set()

        while stack:
            current_node = stack.pop()
            if current_node == self.selectedNodeContainer.selected_node:
                scaled_start = self.scaleOffsetTransformer.get_scaled_coordinates(current_node)
                pygame.draw.circle(self.screen, self.selected_node_color, scaled_start,
                                   self.SELECTED_NODE_SPECIAL_HIGHLIGHT_DIAMETER)
            else:
                scaled_start = self.scaleOffsetTransformer.get_scaled_coordinates(current_node)
                pygame.draw.circle(self.screen, self.selected_node_color, scaled_start,
                                   self.BASE_NODE_HIGHLIGHT_DIAMETER)

            visited_nodes.add(current_node)

            for connected_node in current_node.get_connected_nodes().values():
                scaled_end = self.scaleOffsetTransformer.get_scaled_coordinates(connected_node)
                pygame.draw.line(self.screen, self.selected_node_subtree_color, scaled_start, scaled_end)

                if connected_node not in visited_nodes:
                    stack.append(connected_node)

    def toggle_node_labels(self):
        """
        Toggles the display of the Node Labels.
        """
        self.show_node_labels = not self.show_node_labels

