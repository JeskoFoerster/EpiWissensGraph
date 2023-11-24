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


class MenuButton:
    """
    The MenuButton class represents an interactive button in the user interface of a graph visualization application.
    This class handles the visual representation of a button, including its icon, label, and various states such as
    'clicked' or 'highlighted'. It is designed to be a versatile component for the application's menu, capable of
    handling user interactions and visual changes.
    """

    maximized = True

    def __init__(self, x, y, width, height, icon, icon_x_offset, parent_surface, label_color, background_color,
                 highlight_color, text=''):
        """
        Initializes a MenuButton with specified properties and dimensions.

        :param: x: The x-coordinate of the button.
        :param: y: The y-coordinate of the button.
        :param: width: The width of the button.
        :param: height: The height of the button.
        :param: icon: The Pygame surface representing the button's icon.
        :param: icon_x_offset: The horizontal offset for the icon within the button.
        :param: parent_surface: The parent Pygame surface to which this button belongs.
        :param: label_color: The color of the label text.
        :param: background_color: The background color of the button.
        :param: highlight_color: The color used to highlight the button when selected.
        :param: text: The label text of the button.
        """
        self.icon_size = height  # Die Größe des Icons ist gleich der Höhe des Buttons
        self.text = text
        self.clicked = False
        self.label_color = label_color
        self.highlight_color = highlight_color
        self.background_color = background_color
        self.icon_offset = icon_x_offset

        # Berechne die absolute Position des Buttons relativ zum parent_surface
        parent_x, parent_y = parent_surface.get_abs_offset()
        self.x = parent_x + x
        self.y = parent_y + y
        self.width = width  # Erweitert die Breite, um das Icon unterzubringen
        self.height = height

        self.icon_area_width = width * 0.382
        self.label_area_width = self.width * 0.618

        self.icon = pygame.transform.scale(icon, (self.icon_size, self.icon_size))  # Skalieren des Icons
        self.button_background_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.button_background_surface.fill(self.background_color)

    def draw(self, screen, is_selected: bool = False):
        """
        Draws the button on the given screen. This method handles the rendering of the button's icon, label,
        and background.

        :param: screen: The Pygame screen object where the button will be drawn.
        :param: is_selected: A boolean indicating whether the button is currently selected.
        """
        # Zeichne das Surface
        screen.blit(self.button_background_surface, (self.x, self.y))

        # Zeichne das Icon
        screen.blit(self.icon, (
            self.x + (self.icon_area_width // 2) - self.icon_size + self.icon_offset,
            self.y))  # Das Icon wird links auf dem Button platziert

        # Zeichne den Text, wenn vorhanden
        if self.text != '' and self.maximized:
            self.button_background_surface.fill(self.background_color)
            font = pygame.font.SysFont(None, 25)
            if is_selected:
                text_surface = font.render(self.text, True, self.highlight_color)
            else:
                text_surface = font.render(self.text, True, self.label_color)

            # Label position
            text_x = self.x + self.icon_area_width
            # text_x = self.x + self.icon_size + (self.width - self.icon_size - text_surface.get_width()) // 2  # center
            text_y = self.y + (self.height - text_surface.get_height()) // 2

            screen.blit(text_surface, (text_x, text_y))
        else:
            self.button_background_surface.fill((0, 0, 0, 0))

    def click(self, event):
        """
        Handles click events on the button, toggling its 'clicked' state and determining if the click event
        occurred within the button's area.

        :param: event: The Pygame event to be processed.
        :return: A boolean indicating whether the button was clicked.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (self.x <= mouse_x <= self.x + self.width and
                    self.y <= mouse_y <= self.y + self.height):
                self.clicked = not self.clicked
                return True
        return False
