"""
Ein Konstanten-File in Python ist eine Datei, die dazu verwendet wird, Konstanten zu definieren, die im gesamten
Projekt verwendet werden. Eine Konstante ist ein Wert, der während der Laufzeit des Programms nicht geändert wird.
Das Verwenden eines separaten Files für Konstanten bietet verschiedene Vorteile:

Zentralisierte Verwaltung: Durch die Speicherung aller Konstanten in einer Datei können Sie sie zentral verwalten.
Dies erleichtert die Wartung, da Änderungen an den Konstanten nur an einem Ort vorgenommen werden müssen.

Wiederverwendbarkeit: Konstanten können in verschiedenen Teilen des Programms wiederverwendet werden, ohne dass sie
an mehreren Stellen definiert werden müssen. Dies reduziert Redundanz und potenzielle Fehlerquellen.

Lesbarkeit und Klarheit: Ein dedizierter Konstanten-File trägt zur Klarheit und Lesbarkeit des Codes bei,
da die Bedeutung und der Zweck der Konstanten leichter verständlich sind. Es ist sofort ersichtlich, dass diese Werte
nicht verändert werden sollten.
"""


TITEL = "Help Knoten: Dies ist der Titel Ihres Knotens"

CONTENT = ("Dies ist der Inhalt des Knotens. Ein Zeilenumbruch erfolgt automatisch. Wenn Sie "
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
           "verbunden.\n\n")

IMAGE_NAME = "image_placeholder.png"
