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
import pygame.freetype

from GraphModel import SelectedNodeContainer
from View.UI.NodeDetailsWindow.INodeDetailsWindow import INodeDetailsWindow
from View.UI.NodeDetailsWindow.MarkdownTextRenderer import MarkdownTextRenderer
from View.UI.NodeDetailsWindow.TextAreaScrollManager import TextAreaScrollManager
from View.UI.NodeDetailsWindow.TextWrapper import TextWrapper
from View.UI.UIThemes import UITheme


class NodeDetailsWindow(INodeDetailsWindow):
    """
    The NodeDetailsWindow class is responsible for rendering and managing the details window of a selected node in a
    graph visualization application. It displays detailed information about a node, including text and images,
    and provides functionality for scrolling through content if it exceeds the visible area.
    """

    # Components
    text_wrapper = TextWrapper()

    # Position of Window
    node_details_window_x_pos = 0

    # Background
    node_details_background_surface = None
    node_details_background_width = 0
    node_details_background_height = 0

    # Padding for all Areas
    NODE_DETAILS_X_PADDING = 10
    NODE_DETAILS_Y_PADDING = 10

    NODE_DETAILS_Y_SPACING = 10  # Spacing for all Content Areas
    content_max_width = 0  # With of any Content

    # Text Area
    text_area_render_surface = None

    # Window Dimensions
    window_width = 0
    window_height = 0

    collision_text_window_rect = None

    max_content_height = 0

    selected_node_container = None
    # Variable um nachzuverfolgen, ob die Daten des selektierten Nodes bereits einmal gerendert wurden.
    re_rendering_required = True
    # Aktuell dargestellter Node um abzugleichen, ob ein anderer Node selektiert wurde.
    currently_rendered_node = None

    # Scrolling
    text_area_scroll_manager = TextAreaScrollManager()

    # Text Renderer
    markdown_text_renderer = MarkdownTextRenderer()

    # Path to resources
    resources_path = None
    image_path = None

    def __init__(self, window_width, window_height, screen, ui_theme: UITheme,
                 selected_node_container: SelectedNodeContainer, resources_path):
        """
        Initializes the NodeDetailsWindow with the necessary UI components, dimensions, and resources.

        :param: window_width: The width of the main application window.
        :param: window_height: The height of the main application window.
        :param: screen: The Pygame screen object where the details window will be rendered.
        :param: ui_theme: The UI theme for styling the details window.
        :param: selected_node_container: A container holding the currently selected node.
        :param: resources_path: The path to the resources directory (for loading images, etc.).
        """
        self.resources_path = resources_path
        self.image_path = os.path.join(resources_path, 'Images')
        self.ui_theme = ui_theme

        self.screen = screen

        self.window_width = window_width
        self.window_height = window_height

        self.node_details_background_width = window_width * 0.382
        self.node_details_background_height = window_height
        self.node_details_window_x_pos = self.window_width - self.node_details_background_width

        self.selected_node_container = selected_node_container
        self.currently_rendered_node = selected_node_container.selected_node

        # Background statisch anlegen
        self.node_details_background_surface = pygame.Surface((self.node_details_background_width,
                                                               self.node_details_background_height),
                                                              pygame.SRCALPHA)
        self.node_details_background_surface.fill(ui_theme.TEXT_WINDOW_BACKGROUND_COLOR)

        self.content_max_width = self.node_details_background_width - self.NODE_DETAILS_X_PADDING * 2

    def show_node_details(self):
        """
        Displays the detailed information about the selected node, including scrolling functionality.
        """
        self.__check_if_re_rendering_is_required()

        self.currently_rendered_node = self.selected_node_container.selected_node
        # Display Background
        self.__display_background_area(self.node_details_window_x_pos)

        # Create Image Area
        image_area_height = self.__display_image_area(self.node_details_window_x_pos, 0, self.content_max_width,
                                                      (self.node_details_background_height * 0.618) * 0.618,
                                                      self.NODE_DETAILS_X_PADDING, self.NODE_DETAILS_Y_PADDING,
                                                      self.image_path)

        image_area_height_with_spacing = image_area_height + self.NODE_DETAILS_Y_SPACING
        # Create Titel Area
        titel_area_height = self.__display_titel_area(self.node_details_window_x_pos,
                                                      image_area_height_with_spacing,
                                                      self.content_max_width,
                                                      self.NODE_DETAILS_X_PADDING, self.NODE_DETAILS_Y_PADDING)

        image_and_titel_area_height_with_spacing = image_area_height_with_spacing + titel_area_height + self.NODE_DETAILS_Y_SPACING
        # Display Text Area
        text_area_height = self.__display_text_area_markdown(self.node_details_window_x_pos,
                                                             image_and_titel_area_height_with_spacing,
                                                             self.content_max_width,
                                                             self.node_details_background_height * 0.382,
                                                             self.NODE_DETAILS_X_PADDING, self.NODE_DETAILS_Y_PADDING)

        # Calculate if a scrollbar is necessary
        content_height = image_and_titel_area_height_with_spacing + text_area_height
        if content_height >= self.node_details_background_height:
            self.text_area_scroll_manager.calculate_scrollbar_height(self.node_details_background_height,
                                                                     self.max_content_height)

            self.text_area_scroll_manager.set_scroll_threshold(self.max_content_height)
            self.text_area_scroll_manager.draw_scrollbar(self.window_width, self.NODE_DETAILS_X_PADDING,
                                                         content_height, self.node_details_background_height,
                                                         self.screen, self.ui_theme.SELECTED_NODE_COLOR)

    def __check_if_re_rendering_is_required(self):
        """
        Check if the Content of the NodeDetailsWindow needs to be re-rendered. This is the case when a new Node has
        been selected.

        Returns:
            bool: True if rendering is required, False otherwise.
        """
        if self.currently_rendered_node != self.selected_node_container.selected_node:
            if self.selected_node_container.selected_node is not None and not self.re_rendering_required:
                self.re_rendering_required = True
                # Reset Scrolling
                self.text_area_scroll_manager.reset_scroll()

    def __display_background_area(self, x_position):
        self.screen.blit(self.node_details_background_surface, (x_position, 0))

    def __display_image_area(self, x_pos, y_pos, image_area_width, image_area_height, x_padding, y_padding, image_path):

        image_area_x_pos = x_pos + x_padding
        y_pos = y_pos + y_padding

        image_file_name = self.selected_node_container.selected_node.image_name
        full_path = os.path.join(image_path, image_file_name)
        image = pygame.image.load(full_path)

        # Dimensionen des geladenen Bildes ermitteln
        image_width, image_height = image.get_size()

        # Skalierungsfaktoren für Breite und Höhe berechnen
        scale_x = image_area_width / image_width
        scale_y = image_area_height / image_height

        # Den kleineren Skalierungsfaktor auswählen, um das Seitenverhältnis beizubehalten und sicherzustellen, dass das Bild in das Surface passt
        scale_factor = min(scale_x, scale_y)

        # Das Bild mit dem gewählten Skalierungsfaktor skalieren
        scaled_image = pygame.transform.scale(image,
                                              (int(image_width * scale_factor), int(image_height * scale_factor)))

        image_area_render_surface = pygame.Surface((image_area_width, image_area_height))
        image_area_render_surface.fill(self.ui_theme.TEXT_WINDOW_BACKGROUND_COLOR)
        # Das skalierte Bild in die Mitte des Surface setzen
        blit_x = (image_area_width - scaled_image.get_width()) // 2
        blit_y = (image_area_height - scaled_image.get_height()) // 2
        image_area_render_surface.blit(scaled_image, (blit_x, blit_y))

        self.screen.blit(image_area_render_surface,
                         (image_area_x_pos, y_pos - self.text_area_scroll_manager.scroll_position))
        return image_area_render_surface.get_height()

    def __display_titel_area(self, x_pos, y_pos, titel_area_width, x_padding, y_padding):
        titel_area_x_pos = x_pos + x_padding
        titel_area_y_pos = y_pos + y_padding
        left_padding = self.window_width * 0.015
        right_padding = self.window_width * 0.015

        titel = self.selected_node_container.selected_node.titel
        titel_with_heading = "# " + titel  # Add # for Markdown Heading Formatting
        calculated_titel_area_height = self.markdown_text_renderer.calculate_text_height(titel_with_heading,
                                                                                         left_padding,
                                                                                         right_padding,
                                                                                         titel_area_width)

        titel_area_render_surface = pygame.Surface((titel_area_width, calculated_titel_area_height))
        # Rendern des Texts auf dem separaten Surface
        titel_area_render_surface.fill(self.ui_theme.TEXT_WINDOW_BACKGROUND_COLOR)
        self.markdown_text_renderer.render_markdown_text(titel_area_render_surface, left_padding, right_padding,
                                                         titel_with_heading, titel_area_width)

        self.screen.blit(titel_area_render_surface,
                         (titel_area_x_pos, titel_area_y_pos - self.text_area_scroll_manager.scroll_position))
        return titel_area_render_surface.get_height()

    def __display_text_area_markdown(self, x_pos, y_pos, text_area_width, image_and_titel_area_height,
                                     x_padding, y_padding):
        """
        Private method to display the text content within the window.
        """
        # X Versatz definieren
        text_area_x_pos = x_pos + x_padding
        text_area_y_pos = y_pos + y_padding
        left_padding = self.window_width * 0.015
        right_padding = self.window_width * 0.015

        # Zeige den Text des ausgewählten Knotens im Textfenster an
        if self.selected_node_container.selected_node is not None and self.re_rendering_required:
            self.re_rendering_required = False

            # Text abrufen
            text = self.selected_node_container.selected_node.description

            # Berechnen der maximalen Höhe des Textfensters basierend auf der Anzahl der Zeilen und der Zeilenhöhe
            max_text_height = self.markdown_text_renderer.calculate_text_height(text, left_padding, right_padding,
                                                                                text_area_width)
            self.max_content_height = image_and_titel_area_height + max_text_height
            # Erstellen eines Rechtecks für das Textfenster
            self.collision_text_window_rect = pygame.Rect(x_padding + x_pos,
                                                          y_padding - self.text_area_scroll_manager.scroll_position,
                                                          text_area_width, self.max_content_height)

            # Erstellen eines separaten Surface für das Textfenster
            self.text_area_render_surface = pygame.Surface((text_area_width, max_text_height))

            # Rendern des Texts auf dem separaten Surface
            self.text_area_render_surface.fill(self.ui_theme.TEXT_WINDOW_BACKGROUND_COLOR)
            self.markdown_text_renderer.render_markdown_text(self.text_area_render_surface, left_padding, right_padding,
                                                             text, text_area_width)

        # Zeichne das Textfenster
        self.screen.blit(self.text_area_render_surface,
                         (text_area_x_pos, text_area_y_pos - self.text_area_scroll_manager.scroll_position))
        return self.text_area_render_surface.get_height()

    def check_text_area_collision(self, event):
        """
        Checks if an event collides with the text area in the node details window.

        :param: event: The Pygame event to be checked.
        :return: A boolean indicating whether there is a collision with the text area.
        """
        if self.collision_text_window_rect is not None \
                and self.collision_text_window_rect.collidepoint(event.pos) \
                and self.max_content_height >= self.node_details_background_height:
            return True
        else:
            return False

    def check_scroll_necessity(self, event):
        """
        Determines if scrolling is necessary based on a given event.

        :param: event: The event that triggers the check.
        :return: A boolean indicating whether scrolling is necessary.
        """
        return self.text_area_scroll_manager.check_scroll_necessity(event,
                                                                    self.collision_text_window_rect,
                                                                    self.max_content_height,
                                                                    self.node_details_background_height)

    def apply_scrollbar_scroll(self):
        """
        Applies scrollbar scrolling to the text area.

        This method updates the scroll position based on the current scrollbar state.
        """
        self.text_area_scroll_manager.apply_scrollbar_scroll(self.node_details_background_height,
                                                             self.max_content_height)

    def is_drag_scrolling(self):
        """
        Checks if drag scrolling is currently active.

        Returns:
            bool: True if drag scrolling is active, False otherwise.
        """
        return self.text_area_scroll_manager.drag_scrolling

    def check_scrollbar_collision(self, event):
        """
        Checks if the scrollbar has collided with a given event.

        Args:
            event: The event to check for collision.

        Returns:
            bool: True if the scrollbar has collided with the event, False otherwise.
        """
        return self.text_area_scroll_manager.check_scrollbar_collision(event)

    def start_scrollbar_scrolling(self, event):
        """
        Starts scrollbar scrolling based on a given event.

        Args:
            event: The event that triggers scrollbar scrolling.
        """
        self.text_area_scroll_manager.start_scrollbar_scrolling(event)

    def end_scrollbar_scrolling(self):
        """
        Ends scrollbar scrolling.

        This method stops the scrollbar scrolling operation.
        """
        self.text_area_scroll_manager.end_scrollbar_scrolling()

    def scroll_up(self):
        """
        Scrolls the text area upwards.

        This method scrolls the text area content upwards.
        """
        self.text_area_scroll_manager.scroll_up()

    def scroll_down(self):
        """
        Scrolls the text area downwards.

        This method scrolls the text area content downwards.
        """
        self.text_area_scroll_manager.scroll_down()
