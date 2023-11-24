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

from View.GraphView.IScaleOffsetTransformer import IScaleOffsetTransformer


class ScaleOffsetTransformer(IScaleOffsetTransformer):
    """
    The ScaleOffsetTransformer class implements the IScaleOffsetTransformer interface and is responsible for
    transforming  coordinates in the graph visualization context. This includes scaling and translating
    (panning) operations, which are essential for zooming in and out of the graph and navigating around the graph
    by dragging the view. The class maintains the current zoom level and offset values and provides
    methods to update these based on user interactions.
    """
    # Start Camera Focus
    start_x, start_y = 5000000, 5000000

    zoom = 1.0
    offset_x, offset_y = None, None
    mouse_x, mouse_y = 0, 0  # Speichere die Mausposition

    zoom_scaling_factor = zoom * 0.1
    max_zoom_out = 0.0000001

    def __init__(self, window_width, window_height):
        """
        Initializes the transformer with window dimensions and sets the initial offset.

        :param: window_width (int): The width of the window.
        :param: window_height (int): The height of the window.

        The offset is initialized to center the camera focus in the window.
        """
        # Offset wird auf Start position initalisiert
        self.offset_x, self.offset_y = window_width // 2 - self.start_x, window_height // 2 - self.start_y

    def get_scaled_coordinates(self, node):
        """
        Transforms node coordinates based on the current zoom and offset.

        :param: node (Node): The node containing coordinates to transform.

        :return: Tuple[int, int]: The transformed (scaled) x and total_height coordinates of the node.
        """
        scaled_x = int(node.x * self.zoom) + self.offset_x
        scaled_y = int(node.y * self.zoom) + self.offset_y
        return scaled_x, scaled_y

    def get_scaled_mouse_position(self):
        """
        Returns the mouse position on the scaled plane.

        :param: Tuple[float, float]: The scaled x and total_height coordinates of the mouse position.
        """
        # Gibt die Mausposition auf der skalierten Ebene zurück
        mouse_x, mouse_y = pygame.mouse.get_pos()
        scaled_x = (mouse_x - self.offset_x) / self.zoom
        scaled_y = (mouse_y - self.offset_y) / self.zoom
        return scaled_x, scaled_y

    def update_mouse_position(self):
        """
        Updates the scaled mouse position based on the current zoom and offset.
        """
        # Aktualisiere die Mausposition basierend auf dem aktuellen Zoom und Offset
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.mouse_x = (mouse_x - self.offset_x) / self.zoom
        self.mouse_y = (mouse_y - self.offset_y) / self.zoom

    def increase_zoom_by(self):
        """
        Increases the zoom factor by a specified value.

        :param: value (float): The amount by which to increase the zoom factor.
        """
        # Speichere die Mausposition vor dem Zoom
        self.update_mouse_position()
        self.zoom += self.zoom_scaling_factor
        # Berechne den Unterschied zwischen alter und neuer Mausposition
        dx = (self.mouse_x * self.zoom_scaling_factor)
        dy = (self.mouse_y * self.zoom_scaling_factor)
        # Passe den Offset entsprechend an
        self.decrease_offset_by(dx, dy)
        self.zoom_scaling_factor = self.zoom * 0.1

    def decrease_zoom_by(self):
        """
        Decreases the zoom factor by a specified value.

        :param: value (float): The amount by which to decrease the zoom factor.
        """
        self.update_mouse_position()
        new_zoom = self.zoom - self.zoom_scaling_factor
        if new_zoom >= self.max_zoom_out:
            self.zoom = new_zoom
            dx = (self.mouse_x * -self.zoom_scaling_factor)
            dy = (self.mouse_y * -self.zoom_scaling_factor)
            self.decrease_offset_by(dx, dy)
            self.zoom_scaling_factor = self.zoom * 0.1

    def increase_offset_by(self, dx, dy):
        """
        Increases the offset by specified values in the x and total_height directions.

        :param: dx (int): The amount to increase the horizontal offset.
        :param: dy (int): The amount to increase the vertical offset.
        """
        self.offset_x += dx
        self.offset_y += dy

    def decrease_offset_by(self, dx, dy):
        """
        Decreases the offset by specified values in the x and total_height directions.

        :param: dx (int): The amount to decrease the horizontal offset.
        :param: dy (int): The amount to decrease the vertical offset.
        """
        self.offset_x -= dx
        self.offset_y -= dy

