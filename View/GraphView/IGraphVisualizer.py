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

from GraphModel import Node


class IGraphVisualizer(ABC):
    @abstractmethod
    def draw_graph(self):
        """
        Draws the entire graph on the Pygame screen, including edges and nodes.
        """

    @abstractmethod
    def highlight_selected_subtree(self, node: Node):
        """
        Highlights the subtree rooted at the selected node, including edges and nodes.

        :param: node (Node): The root node of the subtree to be highlighted.
        """