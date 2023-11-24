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

import re

import pygame

from View.UI.FontManager.FontManager import FontManager
from View.UI.FontManager.IFontManger import IFontManager


class MarkdownTextRenderer:
    """
    A class for rendering Markdown-formatted text using pygame.

    Attributes:
        font_manager (IFontManager): An instance of the FontManager to manage fonts.
        regular_font_size (int): The font size for regular text.
        BLACK (tuple): RGB color tuple representing black.
    """
    pygame.init()
    font_manager: IFontManager
    font_manager = FontManager()
    regular_font_size = 18
    BLACK = (0, 0, 0)

    def __init__(self):
        """
        Initializes a MarkdownTextRenderer object, setting up fonts.
        """
        self.normal_font = pygame.font.Font(self.font_manager.get_font_path_font_path_charissil_regular(), self.regular_font_size)
        self.bold_font = pygame.font.Font(self.font_manager.get_font_path_charissil_bold(), self.regular_font_size)
        self.italic_font = pygame.font.Font(self.font_manager.get_font_path_font_charissil_italic(), self.regular_font_size)
        self.bold_italic_font = pygame.font.Font(self.font_manager.get_font_path_charissil_bolditalic(), self.regular_font_size)
        self.large_heading_font = pygame.font.Font(self.font_manager.get_font_path_charissil_bold(), 40)
        self.medium_heading_font = pygame.font.Font(self.font_manager.get_font_path_charissil_bold(), 30)
        self.small_heading_font = pygame.font.Font(self.font_manager.get_font_path_charissil_bold(), 22)

    def render_markdown_text(self, surface, left_padding, right_padding, text, max_width):
        """
        Renders Markdown-formatted text on the specified surface with word wrapping.

        Args:
            surface (pygame.Surface): The surface to render the text on.
            left_padding (int): Padding from the left.
            right_padding: Padding from the right.
            text (str): The Markdown-formatted text to render.
            max_width (int): The maximum width for word wrapping.

        Returns:
            tuple: A tuple containing the total width and height of the rendered text.


        """
        font = self.normal_font
        total_width = left_padding
        last_text_height = 0
        total_height = 0
        max_width = max_width - right_padding

        pattern = r"(?P<text>[^\*#]+)|(?P<bold_italic>\*\*\*.+?\*\*\*)|(?P<bold>\*\*.+?\*\*)|(?P<italic>\*.+?\*)|(?P<large_heading># [^\n]+)|(?P<medium_heading>## [^\n]+)|(?P<small_heading>### [^\n]+)"

        for line in text.split("\n"):
            for segment in re.finditer(pattern, line):
                content = None

                if segment.group("text"):
                    content = segment.group("text")
                    font = self.normal_font
                elif segment.group("bold_italic"):
                    content = segment.group("bold_italic")[3:-3]
                    font = self.bold_italic_font
                elif segment.group("bold"):
                    content = segment.group("bold")[2:-2]
                    font = self.bold_font
                elif segment.group("italic"):
                    content = segment.group("italic")[1:-1]
                    font = self.italic_font
                elif segment.group("large_heading"):
                    font = self.large_heading_font
                    content = segment.group("large_heading")[2:]
                elif segment.group("medium_heading"):
                    font = self.medium_heading_font
                    content = segment.group("medium_heading")[3:]
                elif segment.group("small_heading"):
                    font = self.small_heading_font
                    content = segment.group("small_heading")[4:]

                if content:
                    words = content.split()
                    for word in words:
                        rendered_word = font.render(word, True, self.BLACK)
                        if total_width + rendered_word.get_width() > max_width:
                            total_height += last_text_height
                            total_width = left_padding
                        surface.blit(rendered_word, (total_width, total_height))
                        total_width += rendered_word.get_width() + font.size(' ')[0]
                        last_text_height = rendered_word.get_height()

            total_height += last_text_height
            total_width = left_padding

    def calculate_text_height(self, text, left_padding, right_padding, max_width):
        """
        Calculates the total height required to render Markdown-formatted text.

        Args:
            text (str): The Markdown-formatted text to calculate height for.
            left_padding (int): Modification for the horizontal start position.
            right_padding (int): Modificator for the horizontal end position.
            max_width (int): The maximum width for word wrapping.

        Returns:
            int: The total height required to render the text.

        """
        font = self.normal_font
        total_width = left_padding
        total_height = 0
        last_text_height = 0
        max_width = max_width - right_padding

        pattern = r"(?P<text>[^\*#]+)|(?P<bold_italic>\*\*\*.+?\*\*\*)|(?P<bold>\*\*.+?\*\*)|(?P<italic>\*.+?\*)|(?P<large_heading># [^\n]+)|(?P<medium_heading>## [^\n]+)|(?P<small_heading>### [^\n]+)"

        for line in text.split("\n"):
            for segment in re.finditer(pattern, line):
                content = None

                if segment.group("text"):
                    content = segment.group("text")
                    font = self.normal_font
                elif segment.group("bold_italic"):
                    content = segment.group("bold_italic")[3:-3]
                    font = self.bold_italic_font
                elif segment.group("bold"):
                    content = segment.group("bold")[2:-2]
                    font = self.bold_font
                elif segment.group("italic"):
                    content = segment.group("italic")[1:-1]
                    font = self.italic_font
                elif segment.group("large_heading"):
                    font = self.large_heading_font
                    content = segment.group("large_heading")[2:]
                elif segment.group("medium_heading"):
                    font = self.medium_heading_font
                    content = segment.group("medium_heading")[3:]
                elif segment.group("small_heading"):
                    font = self.small_heading_font
                    content = segment.group("small_heading")[4:]

                if content:
                    words = content.split()
                    for word in words:
                        word_width, word_height = font.size(word)
                        if total_width + word_width > max_width:
                            total_height += last_text_height
                            total_width = left_padding
                        total_width += word_width + font.size(' ')[0]
                        last_text_height = word_height

            total_height += last_text_height
            total_width = left_padding

        return total_height + (total_height * 0.10)
