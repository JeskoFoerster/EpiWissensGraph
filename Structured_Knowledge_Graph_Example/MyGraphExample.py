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
from Structured_Knowledge_Graph_Example.MainGraph import MainGraph
from Structured_Knowledge_Graph_Example.SubGraph import SubGraph


class MyGraphExample:

    def __init__(self, graph: Graph):
        self.create_main_graph(graph)

    def create_main_graph(self, graph):
        """
        Diese Methode dient Ihnen also Demonstration für den Aufbau eines Graphen.
        Er spiegelt die Klasse GraphContent unterteilt den Code jedoch in kleinere Einheiten.
        """
        main_graph = MainGraph(graph)
        literature_source_example_node = main_graph.get_literature_source_example_node()
        sub_graph = SubGraph(literature_source_example_node, graph)



