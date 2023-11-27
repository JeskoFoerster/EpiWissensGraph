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
from Subgraphs.InformationTechnologyGraph import InformationTechnologySubGraph
from Subgraphs.ConsumerGoodsGraph import ConsumerGoodsSubGraph
from Subgraphs.MediaAndEntertainmentGraph import MediaAndEntertainmentSubGraph
from Subgraphs.EnergyGraph import EnergySubGraph
from Subgraphs.InsuranceGraph import InsuranceSubGraph
from Subgraphs.Aerospace import AerospaceSubGraph
from Subgraphs.ArtificialIntelligenceGraph import ArtificialIntelligenceGraph
from Subgraphs.CloudComputing import CloudComputingGraph
from Subgraphs.MechanicalEngineering import MechanicalEngineeringGraph
from Subgraphs.SoftwareAsService import SoftwareAsServiceGraph
from Subgraphs.Cybersecurity import CybersecurityGraph
from Subgraphs.Consulting import ConsultingGraph
from Subgraphs.Pharmaceuticals import PharmaceuticalsGraph
class GraphContent:

    def __init__(self, graph: Graph):
        self.create_company_nodes(graph)

    def create_company_nodes(self, graph):

        # I create this note with the values from the ExampleNote class

        main_note = Node("Das ist die Main-Node", "Main-Node", "example.png", radius=10, color=[238, 130, 238])

        # all SubGraphs here:
        InformationTechnologySubGraph(main_note, graph)
        ConsumerGoodsSubGraph(main_note, graph)
        AerospaceSubGraph(main_note, graph)
        MediaAndEntertainmentSubGraph(main_note, graph)
        EnergySubGraph(main_note, graph)
        InsuranceSubGraph(main_note, graph)
        ArtificialIntelligenceGraph(main_note, graph)
        CloudComputingGraph(main_note, graph)
        MechanicalEngineeringGraph(main_note, graph)
        SoftwareAsServiceGraph(main_note, graph)
        CybersecurityGraph(main_note, graph)
        ConsultingGraph(main_note, graph)
        PharmaceuticalsGraph(main_note, graph)


        # naechster Subgraph...
        # naechster Subgraph...

        # main_note.connect()

        # add the note to the graph
        graph.add_new_node_to_graph(main_note)