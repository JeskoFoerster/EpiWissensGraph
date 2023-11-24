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

import os

import pygame.freetype

from ComponentAssembly.GraphAnalyzer import GraphAnalyzer
from GraphController.GraphExporter import GraphExporter
from GraphController.GraphImporter import GraphImporter
from GraphController.GraphLayoutHandler import IGraphLayoutHandler
from GraphController.GraphLayoutHandler.GraphLayoutHandler import AutoLayoutHandler
from GraphController.NodeFinder.NodeFinder import NodeFinder
from GraphController.SubtreeMover.SubtreeMover import SubtreeMover
from GraphModel.Graph import Graph
from GraphModel.RandomGraphGenerator import RandomGraphGenerator
from GraphModel.SelectedNodeContainer import SelectedNodeContainer
from ComponentAssembly.IComponentProvider import IComponentProvider
from View.GraphView import IScaleOffsetTransformer, IGraphVisualizer
from View.GraphView.GraphVisualizer import GraphVisualizer
from View.GraphView.ScaleOffsetTransformer import ScaleOffsetTransformer
from GraphController.ScreenDragHandler.ScreenDragHandler import ScreenDragHandler, IDragHandler
from View.UI.NodeDetailsWindow import INodeDetailsWindow
from View.UI.NodeDetailsWindow.NodeDetailsWindow import NodeDetailsWindow
from View.UI.UIThemes import BKTheme
from View.UI.MainMenu.MainMenu import MainMenu


class ComponentAssembler(IComponentProvider):
    """
    ComponentAssembler is responsible for initializing and assembling the various components
    required for the graph visualization application. It manages the setup of the display,
    handles the creation and configuration of graph-related components (such as layout handlers,
    visualizers, and interaction handlers), and initializes UI components. It also establishes
    the environment for the application including screen dimensions, color themes, and resources
    paths. This class acts as a central point for component management and provides a structured
    way to access and modify different parts of the application.
    """

    # Initialisierung von pygame
    pygame.init()

    # WIDTH, HEIGHT = 1000, 800
    WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
    window_width, window_height = WIDTH - 10, HEIGHT - 50
    # screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("EPI Knowledge Graph")

    # Colors
    uiTheme = BKTheme()

    def __init__(self, graph: Graph, debug_mode: bool = False):
        """
        Initializes the ComponentAssembler with the given graph. It sets up the necessary components
        for graph analysis, visualization, interaction, and UI. It also handles debug mode initialization
        which includes generating random nodes for testing purposes.

        :param: graph: An instance of Graph, which represents the graph data structure to be visualized and
        interacted with. :param: debug_mode: A boolean flag indicating whether the application is in debug mode,
        which affects how the graph is initialized.
        """
        self.debug_mode = debug_mode

        # Graph
        self.graph = graph

        # Analyzing the contents of the graph
        graph_analyzer = GraphAnalyzer()
        graph_analyzer.display_statistics(graph)

        # Container for currently selected Node
        self.selected_node_container = SelectedNodeContainer()

        if debug_mode:
            self.graph.nodes.clear()
            # Node Generator for Testing
            self.node_generator = RandomGraphGenerator(self.graph)
            self.node_generator.create_random_nodes(100, 150)
            # node_generator.create_random_hierarchical_graph(1000, 2)

        # Scale and Offset Handling
        self.scale_offset_transformer: IScaleOffsetTransformer
        self.scale_offset_transformer = ScaleOffsetTransformer(self.window_width, self.window_height)

        # Graph Model Layout über Barness Hut Algorithmus für N-Körper Simulationen
        self.graph_layout_handler: IGraphLayoutHandler
        self.graph_layout_handler = AutoLayoutHandler(0, 0, 50000000,
                                                      self.scale_offset_transformer, self.screen,
                                                      self.uiTheme.BARNES_HUT_COLOR, self.graph)

        # Drag Screen
        self.drag_handler: IDragHandler
        self.drag_handler = ScreenDragHandler(self.scale_offset_transformer)

        # Drag Graph
        self.subtree_mover = SubtreeMover()

        # Graph Visualization
        self.graph_visualizer: IGraphVisualizer
        self.graph_visualizer = GraphVisualizer(self.scale_offset_transformer,
                                                self.screen, self.graph, self.selected_node_container,
                                                self.uiTheme.EDGE_COLOR, self.uiTheme.NODE_COLOR,
                                                self.uiTheme.SELECTED_NODE_COLOR,
                                                self.uiTheme.SELECTED_NODE_SUBTREE_COLOR)
        # Resources
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.resources_folder_path = os.path.join(current_directory, '../Resources')

        # Node Details Window
        self.node_details_window: INodeDetailsWindow
        self.node_details_window = NodeDetailsWindow(self.window_width, self.window_height, self.screen, self.uiTheme,
                                                     self.selected_node_container,
                                                     self.resources_folder_path)

        # Find Node at Position
        self.node_finder = NodeFinder(self.graph, self.scale_offset_transformer)

        # Initialisiere das Menü
        self.graph_exporter = GraphExporter(self.graph, self.resources_folder_path)
        self.graph_importer = GraphImporter(self.graph, self.resources_folder_path, graph_analyzer)
        self.main_menu = MainMenu(self.window_width, self.window_height, 0, 0, 10, self.uiTheme,
                                  self.resources_folder_path, self.graph_exporter,
                                  self.graph_importer)

    def get_screen(self):
        return self.screen

    def get_ui_theme(self):
        return self.uiTheme

    def get_node_details_window(self):
        return self.node_details_window

    def get_scale_offset_transformer(self):
        return self.scale_offset_transformer

    def get_selected_node_container(self):
        return self.selected_node_container

    def get_graph_layout_handler(self):
        return self.graph_layout_handler

    def get_node_finder(self):
        return self.node_finder

    def get_drag_handler(self):
        return self.drag_handler

    def get_subtree_mover(self):
        return self.subtree_mover

    def get_main_menu(self):
        return self.main_menu

    def get_graph_visualizer(self):
        return self.graph_visualizer
