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

from abc import ABC, abstractmethod


class IComponentProvider(ABC):
    """
    IComponentProvider is an abstract base class defining an interface for providing various components
    used in a graph visualization application. It acts as a contract for classes that implement this interface,
    ensuring they provide access to essential components like UI elements, graph handling utilities, and
    visualization tools. This interface facilitates dependency injection, allowing for better modularity
    and easier testing by abstracting the creation of components from their usage.
    """

    @abstractmethod
    def get_screen(self):
        """
        Abstract method to provide the PyGame screen.
        This screen is used for rendering the graphical components of the application.
        Implementations of this method should return the PyGame screen object.
        """

    @abstractmethod
    def get_ui_theme(self):
        """
        Abstract method to provide the UI Theme.
        The UI Theme contains color data and other stylistic elements for the application's user interface.
        Implementations should return an object representing the UI theme.
        """

    @abstractmethod
    def get_node_details_window(self):
        """
        Abstract method to provide the NodeDetailsWindow Component.
        This component is responsible for displaying and handling interactions with node-specific details.
        Implementations should return an instance of NodeDetailsWindow.
        """

    @abstractmethod
    def get_scale_offset_transformer(self):
        """
        Abstract method to provide the ScaleOffset Component.
        This component is crucial for handling zoom and pan operations in the graph visualization.
        Implementations should return an instance of a scale and offset transformer.
        """

    @abstractmethod
    def get_selected_node_container(self):
        """
        Abstract method to provide the SelectedNodeContainer Component.
        This component manages the state of the currently selected node in the graph.
        Implementations should return an instance of SelectedNodeContainer.
        """

    def get_graph_layout_handler(self):
        """
        Abstract method to provide the GraphLayoutHandler Component.
        This component is responsible for computing and managing the layout of nodes in the graph.
        Implementations should return an instance of a graph layout handler.
        """

    @abstractmethod
    def get_node_finder(self):
        """
        Abstract method to provide the NodeFinder Component.
        This component assists in locating nodes within the graph, typically based on user interactions.
        Implementations should return an instance of NodeFinder.
        """

    @abstractmethod
    def get_drag_handler(self):
        """
        Abstract method to provide the DragHandler Component.
        This component handles drag operations within the application, such as moving nodes or panning the view.
        Implementations should return an instance of a drag handler.
        """

    @abstractmethod
    def get_subtree_mover(self):
        """
        Abstract method to provide the SubtreeMover Component.
        This component is used for handling operations related to moving a subtree within the graph.
        Implementations should return an instance of SubtreeMover.
        """

    @abstractmethod
    def get_main_menu(self):
        """
        Abstract method to provide the MainMenu Component.
        This component represents the main menu interface of the application, offering various options and controls.
        Implementations should return an instance of MainMenu.
        """

    @abstractmethod
    def get_graph_visualizer(self):
        """
        Abstract method to provide the GraphVisualizer Component.
        This component is responsible for the visual representation of the graph, including rendering nodes and edges.
        Implementations should return an instance of GraphVisualizer.
        """
