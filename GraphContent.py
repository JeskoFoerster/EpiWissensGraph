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

from GraphModel.Graph import Graph
from GraphModel.Node import Node

# import all our Industry's


# import all Company's


class GraphContent:

    def __init__(self, graph: Graph):
        self.create_industy_nodes()
        self.create_company_nodes(graph)
        self.connect_industry_with_node()


    def create_industy_nodes(self):
        print("")

    def create_company_nodes(self, graph):

        main_note = Node("Das ist die Main-Node", "Main-Node", "example.png", radius=10, color=[153, 51, 255])
        graph.add_new_node_to_graph(main_note)

        # all company nodes here:


    def connect_nodes_to_industy(self):
        print("")


