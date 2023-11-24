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

import json
import os
import zipfile
from PyQt5.QtWidgets import QApplication, QFileDialog
from ComponentAssembly.GraphAnalyzer import GraphAnalyzer
from GraphModel.Graph import Graph
from GraphModel.Node import Node


class GraphImporter:
    """
    The GraphImporter class is responsible for importing graph data from external sources into the application.
    It supports importing graph data, including node details and connections, from a ZIP file, which may also
    contain related image files. The class handles the extraction and processing of this data, converting it
    into a usable graph structure within the application. It integrates closely with GraphAnalyzer for post-import
    analysis and verification of the graph structure.
    """

    def __init__(self, graph: Graph, resources_folder_path, graph_analyzer: GraphAnalyzer):
        """
        Initializes the GraphImporter.
        """
        self.graph = graph
        self.image_folder_path = os.path.join(resources_folder_path, "Images")
        self.graph_analyzer = graph_analyzer

    def import_graph(self):
        """
        Imports graph data from a selected ZIP file.
        """
        self.graph.nodes.clear()
        app = QApplication([])  # Initialisiert die PyQt-Anwendung
        zip_file_path, _ = QFileDialog.getOpenFileName(filter="ZIP files (*.zip)")
        if zip_file_path:
            with zipfile.ZipFile(zip_file_path, 'r') as zipf:
                image_name_mapping = self.extract_and_rename_images(zipf)
                json_file_name = os.path.basename(zip_file_path).replace('.zip', '.json')

                if json_file_name in zipf.namelist():
                    zipf.extract(json_file_name)
                    with open(json_file_name, 'r') as file:
                        graph_data = json.load(file)
                    os.remove(json_file_name)  # Temporäre JSON-Datei löschen
                    self.create_graph_from_json(graph_data, image_name_mapping)

        app.exit()

    def extract_and_rename_images(self, zipf):
        """
        Extracts and renames images from the ZIP file. If an image with the same name already exists in the target folder,
        it is renamed to avoid conflicts. This method returns a mapping of original to new image names.

        :param: zipf: The opened ZIP file object from which images are to be extracted.
        :return: A dictionary mapping original image names to new names (if renamed).
        """
        os.makedirs(self.image_folder_path, exist_ok=True)
        image_name_mapping = {}
        for file in zipf.namelist():
            if file.endswith(('.png', '.jpg', '.jpeg')):
                original_image_name = file
                final_image_name = file
                original_image_path = os.path.join(self.image_folder_path, file)
                if os.path.exists(original_image_path):
                    final_image_name = self.graph.team_name + "_" + file
                final_image_path = os.path.join(self.image_folder_path, final_image_name)
                with open(final_image_path, 'wb') as f_out:
                    f_out.write(zipf.read(file))
                if original_image_name != final_image_name:
                    image_name_mapping[original_image_name] = final_image_name
        return image_name_mapping

    def create_graph_from_json(self, graph_data, image_name_mapping):
        """
        Creates a graph from JSON data. This method processes the JSON data structure to reconstruct the graph,
        including nodes and their connections. It also updates image names based on the mapping provided from
        the image extraction process.

        :param: graph_data: A dictionary containing the graph data extracted from the JSON file.
        :param: image_name_mapping: A dictionary mapping original image names to new names.
        """
        graph = Graph()
        graph.team_name = graph_data.get("team_name", "Standardteamname")
        nodes = {}
        for node_data in graph_data["nodes"]:
            image_name = node_data["image_name"]
            # Update image_name if it's in the mapping
            if image_name in image_name_mapping:
                image_name = image_name_mapping[image_name]

            node = Node(
                node_data["description"],
                node_data["titel"],
                image_name,
                node_data["x"],
                node_data["y"],
            )
            node.uuid = node_data["uuid"]
            nodes[node.uuid] = node
            graph.nodes.append(node)

        for node_data in graph_data["nodes"]:
            for connected_uuid in node_data["connected_nodes"]:
                nodes[node_data["uuid"]].connect(nodes[connected_uuid])

        self.graph = graph
        self.graph_analyzer.display_statistics(graph)
