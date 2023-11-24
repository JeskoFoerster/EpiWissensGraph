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

from abc import ABC

from View.UI.Colors import Colors


class UITheme(ABC):
    BACKGROUND_COLOR = (0, 0, 0)
    NODE_COLOR = (0, 0, 0)
    EDGE_COLOR = (0, 0, 0)
    TEXT_WINDOW_BACKGROUND_COLOR = (0, 0, 0)
    MAIN_MENU_BACKGROUND_COLOR = (0, 0, 0)
    MAIN_MENU_LABEL_COLOR = (0, 0, 0)
    MAIN_MENU_SELECTED_LABEL_COLOR = (0, 0, 0)
    SELECTED_NODE_COLOR = (0, 0, 0)
    SELECTED_NODE_SUBTREE_COLOR = (0, 0, 0)
    BARNES_HUT_COLOR = (150, 150, 150, 100)
    FULL_ALPHA = (0, 0, 0, 0)


class BKTheme(UITheme):
    BACKGROUND_COLOR = Colors.ELECTROMAGNETIC
    NODE_COLOR = Colors.HINT_OF_PENSIVE
    EDGE_COLOR = Colors.CHAIN_GANG_GREY
    TEXT_WINDOW_BACKGROUND_COLOR = Colors.HINT_OF_PENSIVE_ALPHA
    MAIN_MENU_BACKGROUND_COLOR = Colors.HINT_OF_PENSIVE_ALPHA
    MAIN_MENU_LABEL_COLOR = Colors.PURE_WHITE
    MAIN_MENU_SELECTED_LABEL_COLOR = Colors.VANADYL_BLUE
    SELECTED_NODE_COLOR = Colors.VANADYL_BLUE
    SELECTED_NODE_SUBTREE_COLOR = Colors.PROTOSS_PYLON
    BARNES_HUT_COLOR = (150, 150, 150, 100)
    FULL_ALPHA = (0, 0, 0, 0)


class MinimalisticTheme:
    BACKGROUND_COLOR = Colors.PURE_WHITE
    NODE_COLOR = Colors.GREY_BLACK
    EDGE_COLOR = Colors.GREY_BLACK
    TEXT_WINDOW_BACKGROUND_COLOR = Colors.GREY_BLACK_ALPHA
    SELECTED_NODE_COLOR = Colors.CONTRAST_RED
    SELECTED_NODE_SUBTREE_COLOR = Colors.CONTRAST_RED

    BARNES_HUT_COLOR = (150, 150, 150, 100)
