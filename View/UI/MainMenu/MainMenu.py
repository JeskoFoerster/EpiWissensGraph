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

import pygame

from GraphController.GraphExporter import GraphExporter
from GraphController.GraphImporter import GraphImporter
from View.UI.MainMenu.MenuItemButton import MenuButton
from View.UI.Label import Label
from View.UI.UIThemes import UITheme


class MainMenu:
    """
    The MainMenu class is responsible for managing and displaying the main menu in a graph visualization application.
    It provides interactive options such as exporting and importing graph data and handles user interactions
    with these options. The class integrates with the GraphExporter and GraphImporter for respective functionalities
    and manages the visual presentation and layout of the menu and its items.
    """

    def __init__(self, window_width, window_height, menu_x, menu_y, spacing, ui_theme: UITheme, resources_folder_path,
                 graph_exporter: GraphExporter, graph_importer: GraphImporter):
        """
        Initializes the MainMenu with necessary components, settings, and dimensions.

        :param: window_width: The width of the window where the menu is displayed.
        :param: window_height: The height of the window where the menu is displayed.
        :param: menu_x: The x-coordinate for the menu's position.
        :param: menu_y: The y-coordinate for the menu's position.
        :param: spacing: The spacing between menu items.
        :param: ui_theme: The UI theme used for styling the menu.
        :param: resources_folder_path: The path to the folder containing resources like icons.
        :param: graph_exporter: The GraphExporter instance used for exporting graph data.
        :param: graph_importer: The GraphImporter instance used for importing graph data.
        """
        # Import Export
        self.graph_exporter = graph_exporter
        self.graph_importer = graph_importer

        # Icons
        icon_path = self.image_path = os.path.join(resources_folder_path, 'Icons')
        menu_button_icon_full_path = os.path.join(icon_path, "bars-solid.png")
        export_button_icon_full_path = os.path.join(icon_path, "file-export-solid.png")
        import_button_icon_full_path = os.path.join(icon_path, "file-import-solid.png")
        menu_button_icon = pygame.image.load(menu_button_icon_full_path)
        export_button_icon = pygame.image.load(export_button_icon_full_path)
        import_button_icon = pygame.image.load(import_button_icon_full_path)

        # Background Surface
        menu_background_width = window_width * 0.382 * 0.382
        menu_background_height = window_height
        self.menu_background_surface = pygame.Surface((menu_background_width, menu_background_height), pygame.SRCALPHA)
        self.menu_background_surface.fill(ui_theme.MAIN_MENU_BACKGROUND_COLOR)
        self.menu_x = menu_x + spacing
        self.menu_y = menu_y + spacing

        button_height = 30
        button_width = menu_background_width

        self.menu_button = MenuButton(self.menu_x, self.menu_y,
                                      menu_background_width, button_height, menu_button_icon,
                                      0,
                                      self.menu_background_surface,
                                      ui_theme.MAIN_MENU_LABEL_COLOR,
                                      ui_theme.MAIN_MENU_BACKGROUND_COLOR,
                                      ui_theme.SELECTED_NODE_COLOR,
                                      Label.MAIN_MENU)

        self.export_button = MenuButton(self.menu_x, self.menu_y + button_height + 10,
                                        button_width, button_height, export_button_icon,
                                        3.5,
                                        self.menu_background_surface,
                                        ui_theme.MAIN_MENU_LABEL_COLOR,
                                        ui_theme.FULL_ALPHA,
                                        ui_theme.SELECTED_NODE_COLOR,
                                        Label.EXPORT_BUTTON)

        self.import_button = MenuButton(self.menu_x, self.menu_y + 2 * (button_height + 10),
                                        button_width, button_height, import_button_icon,
                                        -3.5,
                                        self.menu_background_surface,
                                        ui_theme.MAIN_MENU_LABEL_COLOR,
                                        ui_theme.FULL_ALPHA,
                                        ui_theme.SELECTED_NODE_COLOR,
                                        Label.IMPORT_BUTTON)
        self.show_menu = False

    def handle_event(self, event):
        """
        Handles user interaction events with the menu, including clicks for expanding the menu,
        and exporting and importing actions.

        :param: event: The Pygame event to be processed.
        """
        if self.menu_button.click(event):
            self.show_menu = not self.show_menu

        if self.show_menu:
            self.menu_button.maximized = True
            if self.export_button.click(event):
                self.export_action()

            if self.import_button.click(event):
                self.import_action()
        else:
            self.menu_button.maximized = False

    def draw(self, screen):
        """
        Draws the main menu and its items onto the screen.

        :param: screen: The Pygame screen object where the menu is rendered.
        """
        if self.show_menu:
            self.menu_button.draw(screen, True)
            screen.blit(self.menu_background_surface, (self.menu_x, self.menu_y))
            self.export_button.draw(screen)
            self.import_button.draw(screen)
        else:
            self.menu_button.draw(screen)

    def export_action(self):
        """
        Executes the action for exporting graph data. This method triggers the graph export process.
        """
        self.graph_exporter.export_graph()

    def import_action(self):
        """
        Executes the action for importing graph data. This method triggers the graph import process.
        """
        self.graph_importer.import_graph()
