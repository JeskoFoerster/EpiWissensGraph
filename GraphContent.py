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

# import all our Subgraphs
from Structured_Knowledge_Graph_Example.SubGraph import SubGraph

# this is the Package "ExampleNode" that I created. I am importing the ExampleNode class from my file.
from Resources.ExampleNode import ExampleNode

example_note_data = ExampleNode.Example_note()


class GraphContent:

    def __init__(self, graph: Graph):
        self.create_company_nodes(graph)

    def create_company_nodes(self, graph):

        # I create this note with the values from the ExampleNote class

        main_note = Node(example_note_data.EXAMPLE_DESCRIPTION, example_note_data.EXAMPLE_TITLE, example_note_data.IMAGE, radius=10, color=[238, 130, 238])

        # all SubGraphs here:
        SubGraph(main_note, graph)
        # SubGraph2...
        # SubGraph3...

        # main_note.connect()

        # add the note to the graph
        graph.add_new_node_to_graph(main_note)