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
from GraphModel import Graph


class GraphExporter:
    """
    The GraphExporter class is responsible for exporting the data of a graph into different formats.
    This includes gathering all relevant information from the Graph object, such as node details and
    connections, and then saving this data into a file. The class supports exporting to various formats,
    including JSON and ZIP, allowing for easy sharing and storage of graph data. It also handles
    the inclusion of associated image files in the export, ensuring a complete representation of the graph.
    """

    def __init__(self, graph: Graph, resources_folder_path):
        """
        Initializes the GraphExporter with a specific graph and a path to the resources folder.
        """
        self.graph = graph
        self.image_folder_path = os.path.join(resources_folder_path, "Images")

    def export_graph(self):
        """
        Exports the graph data to a ZIP file.
        """
        app = QApplication([])  # Initialisiert die PyQt-Anwendung
        graph_data = self.prepare_graph_data()

        file_path, _ = QFileDialog.getSaveFileName(
            caption="Export Graph",
            filter="ZIP files (*.zip)"
        )

        if file_path:
            if not file_path.endswith('.zip'):
                file_path += '.zip'
            self.export_to_zip(graph_data, file_path)

        app.exit()  # Schließt die PyQt-Anwendung

    def prepare_graph_data(self):
        """
        Prepares the graph data for export.
        """
        return {
            "team_name": self.graph.team_name,
            "nodes": [
                {
                    "uuid": str(node.uuid),
                    "description": node.description,
                    "titel": node.titel,
                    "x": node.x,
                    "y": node.y,
                    "image_name": node.image_name,
                    "connected_nodes": [str(uuid) for uuid in node.get_connected_nodes()]
                } for node in self.graph.nodes
            ]
        }

    def export_to_zip(self, graph_data, file_path):
        """
        Exports graph data to a ZIP file.
        """
        with zipfile.ZipFile(file_path, 'w') as zipf:
            json_path = file_path.replace('.zip', '.json')
            with open(json_path, 'w') as file:
                json.dump(graph_data, file)
            zipf.write(json_path, os.path.basename(json_path))
            os.remove(json_path)  # Delete temporary JSON file

            for image in os.listdir(self.image_folder_path):
                zipf.write(os.path.join(self.image_folder_path, image), image)

