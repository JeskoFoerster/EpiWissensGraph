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


class GraphContent:

    def __init__(self, graph: Graph):
        self.create_demo_nodes(graph)

    def create_demo_nodes(self, graph):
        """
        Diese Methode dient Ihnen also Demonstration für den Aufbau eines Graphen.
        TODO: Löschen oder kommentieren Sie diese Methode aus wenn Sie Ihren eigenen Graphen erstellen.
        """

        how_to_node = Node("Dies ist der Inhalt des Knotens. Ein Zeilenumbruch erfolgt automatisch. Wenn Sie "
                           "jedoch manuell einen Absatz einfügen möchten ist dies über \n \n möglich.\n \n"
                           " Sie haben die Möglichkeit Text als *kursiv* oder **fett** oder ***kombiniert*** "
                           "hervorzuheben.\n\n"
                           "Mit der ***Leertaste*** können Sie Ihren Graphen ausrichten lassen. Hierbei "
                           "wirken zwei Arten von  simulierten Kräften. Knoten stoßen sich generell ab "
                           "zum Zweck der visuellen Verteilung. Desto weiter Knoten voneinander entfernt "
                           "sind desto schwächer ist Abstoßungskraft. Knoten die miteinander verbunden sind "
                           "ziehen sich an. Desto weiter Knoten voneinander entfernt sind umso stärker ist "
                           "die Anziehungskraft.\n\n"
                           "Mit der ***T*** Taste können Sie die Titel der Knoten ein und ausblenden.\n\n"
                           "Mit der ***Esc*** Taste können Sie die Anwendung schließen.\n\n"
                           "Darüber hinaus können Sie Überschriften in drei Ebenen definieren. Text der als "
                           "Überschrift markiert wird, wird bis zum nächsten Zeilenumbruch als solcher "
                           "erkannt.\n"
                           "\n# Das ist Ebene 1\n"
                           "Nach einem Absatz wird eine Überschrift automatisch unterbrochen."
                           "\n## Das ist Ebene 2\n"
                           "Wie sie sehen ist diese Überschrift etwas kleiner."
                           "\n### Und abschließend Ebene 3\n"
                           "Und hier die kleinste Form.\n\n"
                           "\n# Hinweis\n"
                           "Wenn Ihr Graph wächst wird es immer schwieriger werden ihn zu "
                           "erweitern und zu verändern. Hier entsteht die Verbindung zu Softwareprojekten. "
                           "Zu beginn ist alles noch leicht nachvollziehbar und übersichtlich. Desto mehr "
                           "Funktionalität Sie jedoch implementieren um so komplexer wird Ihr System. "
                           "Es gibt immer mehr Inhalte und mehr Verbindungen dieser Inhalte. Erschaffen Sie "
                           "hierbei keine geeignete Struktur erhalten Sie was wir Spaghetti-Code oder einen "
                           "Big Ball of Mud nennen. Alles ist scheinbar miteinander verbunden und erzeugt "
                           "Abhängigkeiten miteinander. Wenn Sie ein Teil verändern wollen müssen Sie auch "
                           "alle anderen Teile verändern."
                           "Ein Teil Ihrer Aufgabenstellung ist es mit dieser wachsenden Komplexität "
                           "umzugehen. Sie entscheiden dabei als Team welchen Weg Sie einschlagen. Ziehen "
                           "sie es vor die Inhalte hard zu coden also direkt in diese Methode zu schreiben? "
                           "Werden Sie eigene Klassen und Methoden für die Bestandteile des Graphen anlegen? "
                           "Schreiben Sie selbst einen Importer über den Sie Text Files einlesen können?"
                           "Schreiben Sie ein User Interface um Texte direkt über die"
                           "Applikation einzugeben? Denken Sie dabei auch an Modelle und wie Abstraktion "
                           "Ihnen hilft Dinge zu vereinfachen. Planen Sie Ihren Graphen, teilen Sie "
                           "Verantwortlichkeiten im Team auf, erstellen Sie Modelle und iterieren Sie um"
                           "Ihren Wissensgraph inkrementell zu entwickeln."
                           ""
                           "\n# Bilder\n"
                           "Zu jedem Knoten können Sie ein Bild hinzufügen. Hier für ist es notwendig "
                           "das dieses Bild im Ordner Resources\Images abgelegt wird und der Name der Datei "
                           "als dritter Parameter spezifiziert wird. Denken Sie daran Bilder in Git "
                           "hinzuzufügen: Rechtsklick + Git + Add. Auch diese Bilder müssen Sie anschließend "
                           "commiten und pushen."
                           "\n # Verbindungen (Kanten) \n"
                           "Knoten können über die Methode .connect mit einander verbunden werden. Dabei "
                           "wird diese Methode auf dem Vater Knoten angewandt und das Kind als Parameter "
                           "übergeben, \n\nz. B.: ***vater.connect(kind)***\n\n"
                           "Wenn Sie im Graphen einen Knoten Verschieben, werden die Kinder immer "
                           "mit verschoben. Sie können auch bidirektionale Verbindungen anlegen in dem Sie "
                           "zusätzlich: *kind.connect(vater)* verwenden. Selektieren Sie einen Knoten, "
                           "werden alle Kinder und Kindeskinder im Graphen optisch hervorgehoben."
                           "\n # Menü \n"
                           "Das Menü oben links stellt Ihnen zwei Optionen zur Verfügung."
                           "\n ## Export \n"
                           "Der Export erlaubt es Ihnen den aktuellen Graph als ZIP File zu exportieren. "
                           "Dieser File ist Ihre Abgabe am Ende des Projektes. Neben dem Graphen werden auch "
                           "alle Bilder im Image Ordner exportiert."
                           "\n ## Import \n"
                           "Der Import erlaubt es einen exportierten Graphen zu laden. Wenn Sie EPI im POW Modus "
                           "besuchen können Sie auf diesem Wege die Graphen Ihrer Kommilitonen laden. Wenn Sie diese "
                           "Funktion verwenden möchten, achten Sie bitte darauf, dass Bilder im "
                           "importierten ZIP File in den Image Ordner Ihres Projektes importiert werden. "
                           "Falls ein File mit dem identischen Namen im Image Ordner bereits vorhanden ist, "
                           "wird der Name des importierten Bildes mit dem Namen Ihres Teams konkateniert/"
                           "verbunden.\n\n",
                           "Help Knoten: Dies ist der Titel Ihres Knotens",
                           "image_placeholder.png")

        online_source_example_node = Node("## Anmerkung: \n"
                                          "Dies ist Knoten für Online-Quellen. In diesem konkreten Fall für Markdown "
                                          "als Internet Quelle. Hierbei wird die offizielle Website des Entwicklers "
                                          "von Markdown verwendet. Eine Website als Quelle ist legitim, wenn sie "
                                          "bestimmte Kriterien der Glaubwürdigkeit und Zuverlässigkeit erfüllt. "
                                          "Kriterien hierfür sind: \n\n"
                                          "**- Expertise:**\n"
                                          "Überprüfen Sie, wer hinter der Website steht. Ist es eine anerkannte "
                                          "Institution, eine Bildungseinrichtung oder ein Experte auf dem Gebiet? \n\n"
                                          "**- Aktualität:**\n"
                                          "Überprüfen Sie das Datum der Veröffentlichung oder der letzten "
                                          "Aktualisierung. Für viele Themen ist es wichtig, dass die Informationen "
                                          "aktuell sind. \n\n"
                                          "**- Genauigkeit und Zuverlässigkeit:**\n"
                                          "Enthält die Website präzise Informationen, die mit anderen glaubwürdigen "
                                          "Quellen übereinstimmen? Websites, die sorgfältig recherchiert und mit "
                                          "Belegen untermauert sind, sind in der Regel vertrauenswürdiger.\n\n"
                                          "**- Zweck und Objektivität:**\n"
                                          "Beurteilen Sie den Zweck der Website. Ist sie darauf ausgerichtet, "
                                          "objektive Informationen zu liefern, oder verfolgt sie kommerzielle, "
                                          "politische oder ideologische Ziele? Objektive, unparteiische Quellen sind "
                                          "generell vertrauenswürdiger.\n\n"
                                          "**- Transparenz:**\n"
                                          "Gute Quellen bieten oft Informationen über ihre Autoren, Finanzierung, "
                                          "Mission und den Prozess der Inhaltsprüfung.\n\n"
                                          "\n## Beispiel\n"
                                          "\n### Autor:\n"
                                          "Gruber, John"
                                          "\n### Jahr:\n"
                                          "2004"
                                          "\n### Titel:\n"
                                          "Markdown"
                                          "\n### Verfügbar unter:\n"
                                          "https://daringfireball.net/projects/markdown/"
                                          "\n### Zugriff am:\n"
                                          "11. November 2023"
                                          , "(Gruber, 2004)")

        literature_source_example_node = Node("## Anmerkung: \n"
                                              "Dies ist Knoten für Literaturquellen. Hierbei sind folgende "
                                              "Informationen für ***Bücher*** essenziell:\n\n"
                                              "**- Autor:**\n Der vollständige Name des Autors.\n\n"
                                              "**- Erscheinungsjahr:**\n Das Jahr, in dem das Buch veröffentlicht "
                                              "wurde.\n\n"
                                              "**- Titel des Buches:**\n Der vollständige Titel des Buches, eventuell "
                                              "inklusive Untertitel.\n\n"
                                              "**- Auflage:**\n Inhalt kann sich mit den verschieden Auflagen "
                                              "eines Buches unterscheiden. Daher ist es wichtig die Auflage anzugeben, "
                                              "auf die Sie sich beziehen. \n\n"
                                              "**- Ort der Veröffentlichung:**\n Die Stadt, in der der Verlag seinen "
                                              "Sitz hat."
                                              "**- Verlag:**\n Der Name des Verlags.\n\n"
                                              "\n## Beispiel\n"
                                              "\n### Autor:\n"
                                              "Martin, R.C."
                                              "\n### Veröffentlichungsjahr:\n"
                                              "2021"
                                              "\n### Titel:\n"
                                              "Clean Craftsmanship: Disciplines, Standards, and Ethics"
                                              "\n### Auflage:\n"
                                              "1. Auflage"
                                              "\n### Ort:\n"
                                              "Boston"
                                              "\n### Verlag:\n"
                                              "Addison-Wesley Professional"
                                              , "(Martin, 2021)")

        paper_source_example_node = Node("Für wissenschaftliche Veröffentlichungen (***Paper***) sind folgende "
                                         "Angaben notwendig:\n\n"
                                         "**- Autor(en) des Papers:**\n Die Namen der Autoren, in der "
                                         "Reihenfolge, in der sie im Paper aufgeführt sind.\n\n"
                                         "**- Jahr der Veröffentlichung:**\n Das Jahr, in dem das Paper "
                                         "veröffentlicht wurde.\n\n"
                                         "**- Titel des Papers:**\n Der vollständige Titel des Papers.\n\n"
                                         "**- Titel der Zeitschrift oder Konferenz:**\n Der Name der Zeitschrift "
                                         "oder der Konferenz, in der das Paper veröffentlicht wurde.\n\n"
                                         "**- Bandnummer(Ausgabennummer):**\n Die Band- und Ausgabennummer der "
                                         "Zeitschrift, in der das Paper erschien.\n\n"
                                         "**- Seitenzahlen:**\n Die Seitenzahlen des Papers in der Zeitschrift."
                                         "**- URL:**\n Falls das Paper online verfügbar ist, fügen Sie die URL "
                                         "hinzu.\n\n"
                                         "**- Zugriff am:**\n Das Datum, an dem Sie auf das Paper zugegriffen "
                                         "haben, falls es online verfügbar ist.\n\n"
                                         "\n## Beispiel\n"
                                         "\n### Autor:\n"
                                         "Dijkstra, E.W."
                                         "\n### Veröffentlichungsjahr:\n"
                                         "1972"
                                         "\n### Titel:\n"
                                         "The Humble Programmer"
                                         "\n### In:\n"
                                         "Communications of the ACM"
                                         "\n### Bandnummer(Ausgabennummer):\n"
                                         "15(10)"
                                         "\n### Seitenzahlen:\n"
                                         "859-866"
                                         , "(Dijkstra, 1972)")


        how_to_node.connect(online_source_example_node)
        how_to_node.connect(literature_source_example_node)
        how_to_node.connect(paper_source_example_node)

        graph.add_new_node_to_graph(how_to_node)
        graph.add_new_node_to_graph(online_source_example_node)
        graph.add_new_node_to_graph(literature_source_example_node)
        graph.add_new_node_to_graph(paper_source_example_node)
