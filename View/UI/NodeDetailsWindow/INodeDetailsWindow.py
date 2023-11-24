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


class INodeDetailsWindow(ABC):
    @abstractmethod
    def check_text_area_collision(self, event):
        """
        Checks if an event collides with the text area.

        Args:
            event (pygame.event.Event): The event to be checked.

        Returns:
            bool: True if collision with the text area, False otherwise.
        """

    @abstractmethod
    def check_scrollbar_collision(self, event):
        """
        Checks if an event collides with the scroll bar.

        Args:
            event (pygame.event.Event): The event to be checked.

        Returns:
            bool: True if collision with the scroll bar, False otherwise.
        """

    @abstractmethod
    def check_scroll_necessity(self, event):
        """
        Checks if scrolling is necessary based on the given event.

        Args:
            event: The event that triggers the check.

        Returns:
            bool: True if scrolling is necessary, False otherwise.
        """

    @abstractmethod
    def start_scrollbar_scrolling(self, event):
        """
        Initiates scrolling when the user interacts with the scroll bar.

        Args:
            event (pygame.event.Event): The event that triggers scrolling.
        """

    @abstractmethod
    def end_scrollbar_scrolling(self):
        """
        Ends scrolling when the user releases die Scrollbar.
        """

    @abstractmethod
    def scroll_up(self):
        """
        Scrolls the text content upward.
        """

    @abstractmethod
    def scroll_down(self):
        """
        Scrolls the text content downward.
        """

    @abstractmethod
    def apply_scrollbar_scroll(self):
        """
        Applies scrolling based on user interaction.
        """

    @abstractmethod
    def show_node_details(self):
        """
        Displays the detailed information about the selected node, including scrolling functionality.
        """

    @abstractmethod
    def is_drag_scrolling(self):
        """
        Checks if drag scrolling is currently active.

        Returns:
            bool: True if drag scrolling is active, False otherwise.
        """
        pass

