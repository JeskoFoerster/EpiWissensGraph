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


class TextAreaScrollManager:
    """
    The TextAreaScrollManager class is responsible for managing the scrolling functionality within a text area.
    This class facilitates user interactions with a scrollbar, allowing for smooth navigation through long
    textual content. It handles scrolling events, calculates scrollbar position and size, and provides methods
    for drawing and updating the scrollbar in response to user actions.
    """
    drag_scrolling = False  # True, wenn der Nutzer den Scrollbalken zieht
    initial_scroll_click_y = 0  # Startpunkt des Ziehens
    scroll_bar_x = 0
    scroll_bar_y = 0
    scroll_bar_width = 4
    scroll_bar_height = 0
    scroll_bar_rect = None
    max_content_height = 0
    node_details_background_height = 0

    scroll_threshold = 0
    scroll_position = 0

    SCROLL_AMOUNT = 20

    def __int__(self):
        """
        Initializes the TextAreaScrollManager, setting up the initial state and properties for the scrollbar.
        """
        self.scroll_bar_rect = pygame.Rect(self.scroll_bar_x, self.scroll_bar_y, 0, 0)

    def calculate_scrollbar_height(self, node_details_background_height, max_content_height):
        """
        Calculates the height of the scrollbar based on the height of the text area and the total height of the content.

        This method determines the height of the scrollbar based on the dimensions of the
        text window and the total height of the text content. The scrollbar height is adjusted to
        maintain the proper proportion between the displayed text and the scrollbar.

        """
        # Define the height of the scrollbar
        scroll_bar_percentage = node_details_background_height / max_content_height
        self.scroll_bar_height = node_details_background_height * scroll_bar_percentage
        self.node_details_background_height = node_details_background_height
        self.max_content_height = max_content_height

    def limit_scrolling(self):
        """
        Limits the scrolling position to ensure that scrolling does not exceed the bounds of the content.
        """
        # Begrenzen der Scroll-Position, um über den obersten Punkt hinaus zu verhindern
        self.scroll_position = max(self.scroll_position, 0)
        # Berechnen der maximalen Scroll-Position basierend auf dem Textinhalt und der sichtbaren Bildschirmhöhe
        max_scroll_position = self.max_content_height + self.scroll_threshold - self.node_details_background_height
        # Begrenzen der Scroll-Position, um nicht weiter zu scrollen als der Textinhalt
        self.scroll_position = min(self.scroll_position, abs(max_scroll_position))

    def set_scroll_threshold(self, max_content_height):
        """
        Sets a threshold for scrolling, allowing for a small amount of scrolling beyond the content's end.
        """
        # Scroll Threshold um etwas weiter als bis zum Ende zu scrollen
        self.scroll_threshold = max_content_height * 0.05

    def check_scrollbar_collision(self, event):
        """
        Checks if a given event (such as a mouse click) collides with the scrollbar.

        :param: event: The Pygame event to be checked.
        :return: True if the event collides with the scrollbar, False otherwise.
        """
        if self.scroll_bar_rect is not None and self.scroll_bar_rect.collidepoint(event.pos):
            return True
        else:
            return False

    def check_scroll_necessity(self, event, collision_text_window_rect, max_text_height, node_details_background_height):
        """
        Determines if scrolling is necessary based on the height of the content and the dimensions of the text area.

        :param: event: The Pygame event to be checked.
        :param: collision_text_window_rect: The Pygame Rect object representing the text area.
        :param: max_text_height: The maximum height of the text content.
        :param: node_details_background_height: The height of the node details background.
        :return: True if scrolling is necessary, False otherwise.
        """
        if collision_text_window_rect is not None \
                and max_text_height >= node_details_background_height \
                and self.check_scrollbar_collision(event):
            return True
        else:
            return False

    def start_scrollbar_scrolling(self, event):
        """
        Initiates scrollbar scrolling based on a user event (like mouse click and drag).

        :param: event: The Pygame event that triggers scrolling.
        """
        self.drag_scrolling = True
        self.initial_scroll_click_y = event.pos[1] - self.scroll_bar_y

    def end_scrollbar_scrolling(self):
        """
        Ends the scrolling operation, usually when the user releases the mouse button.
        """
        self.drag_scrolling = False

    def scroll_up(self):
        """
        Scrolls the text content upward.
        """
        self.scroll_position -= self.SCROLL_AMOUNT
        self.limit_scrolling()

    def scroll_down(self):
        """
        Scrolls the text content downward.
        """
        self.scroll_position += self.SCROLL_AMOUNT
        self.limit_scrolling()

    def apply_scrollbar_scroll(self, node_details_background_height, max_text_height):
        """
        Applies the scrollbar's scrolling position to the text content, updating the visible area.
        """
        mouse_y = pygame.mouse.get_pos()[1]
        scroll_bar_new_y = mouse_y - self.initial_scroll_click_y
        scroll_percentage = scroll_bar_new_y / (node_details_background_height - self.scroll_bar_height)
        self.scroll_position = scroll_percentage * (
                max_text_height - node_details_background_height)
        self.limit_scrolling()

    def draw_scrollbar(self, window_width, node_details_x_padding, max_content_height, node_details_background_height, screen, color):
        """
        Draws the scrollbar on the screen based on the current scroll position and dimensions of the text area.

        :param: window_width: The width of the application window.
        :param: node_details_x_padding: The horizontal padding of the node details area.
        :param: max_content_height: The maximum height of the text content.
        :param: node_details_background_height: The height of the node details background.
        :param: screen: The Pygame screen object where the scrollbar will be drawn.
        :param: color: The color of the scrollbar.
        """
        # Calculate the position of the scrollbar
        self.max_content_height = max_content_height
        self.scroll_bar_x = window_width - self.scroll_bar_width - (node_details_x_padding / 2)
        self.scroll_bar_y = (self.scroll_position / (self.max_content_height - node_details_background_height)) * (
                node_details_background_height - self.scroll_bar_height)

        # Create a rectangle representing the scrollbar
        self.scroll_bar_rect = pygame.Rect(self.scroll_bar_x, self.scroll_bar_y, self.scroll_bar_width,
                                           self.scroll_bar_height)

        # Draw the scrollbar on the screen surface
        pygame.draw.rect(screen, color, self.scroll_bar_rect)

    def reset_scroll(self):
        """
        Resets the scroll position to the start of the content.
        """
        self.scroll_position = 0


