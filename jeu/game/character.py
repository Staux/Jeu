from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QSpinBox, QRadioButton, QButtonGroup, QSlider
from PyQt5.QtCore import Qt

class CharacterCreation(QWidget):
    def __init__(self, parent, start_game_callback):
        super().__init__(parent)
        self.parent = parent
        self.start_game_callback = start_game_callback
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Choix de la race
        self.race_label = QLabel("Race")
        layout.addWidget(self.race_label)
        self.race_options = QComboBox()
        self.race_options.addItems(["Humain", "Elfe", "Nain", "Orc"])
        layout.addWidget(self.race_options)

        # Choix de la classe
        self.class_label = QLabel("Classe")
        layout.addWidget(self.class_label)
        self.class_options = QComboBox()
        self.class_options.addItems(["Guerrier", "Mage", "Voleur"])
        layout.addWidget(self.class_options)

        # Sélection des cheveux
        self.hair_label = QLabel("Cheveux")
        layout.addWidget(self.hair_label)
        self.hair_style_options = QComboBox()
        self.hair_style_options.addItems(["Court", "Long", "Bouclé"])
        layout.addWidget(self.hair_style_options)

        self.hair_color_label = QLabel("Couleur des Cheveux")
        layout.addWidget(self.hair_color_label)
        self.hair_color = QSlider(Qt.Horizontal)
        self.hair_color.setRange(0, 100)
        layout.addWidget(self.hair_color)

        # Sélection du visage
        self.face_label = QLabel("Visage")
        layout.addWidget(self.face_label)
        self.face_group = QButtonGroup(self)
        self.face_radio1 = QRadioButton("Visage 1")
        self.face_radio2 = QRadioButton("Visage 2")
        self.face_group.addButton(self.face_radio1)
        self.face_group.addButton(self.face_radio2)
        layout.addWidget(self.face_radio1)
        layout.addWidget(self.face_radio2)

        self.eye_color_label = QLabel("Couleur des Yeux")
        layout.addWidget(self.eye_color_label)
        self.eye_color_options = QComboBox()
        self.eye_color_options.addItems(["Bleu", "Vert", "Marron"])
        layout.addWidget(self.eye_color_options)

        self.skin_color_label = QLabel("Couleur de la Peau")
        layout.addWidget(self.skin_color_label)
        self.skin_color = QSlider(Qt.Horizontal)
        self.skin_color.setRange(0, 100)
        layout.addWidget(self.skin_color)

        # Distribution des Points de Compétence
        self.strength_label = QLabel("Force")
        layout.addWidget(self.strength_label)
        self.strength_points = QSpinBox()
        self.strength_points.setRange(0, 20)
        layout.addWidget(self.strength_points)

        self.intelligence_label = QLabel("Intelligence")
        layout.addWidget(self.intelligence_label)
        self.intelligence_points = QSpinBox()
        self.intelligence_points.setRange(0, 20)
        layout.addWidget(self.intelligence_points)

        self.dexterity_label = QLabel("Dextérité")
        layout.addWidget(self.dexterity_label)
        self.dexterity_points = QSpinBox()
        self.dexterity_points.setRange(0, 20)
        layout.addWidget(self.dexterity_points)

        # Aperçu des compétences
        self.stats_preview = QLabel("Aperçu des Compétences")
        layout.addWidget(self.stats_preview)

        # Choix de l'équipement de départ
        self.equipment_label = QLabel("Équipement de Départ")
        layout.addWidget(self.equipment_label)
        self.equipment_list = QComboBox()
        self.equipment_list.addItems(["Épée", "Arc", "Bâton magique"])
        layout.addWidget(self.equipment_list)

        # Bouton pour commencer le jeu
        self.start_game_button = QPushButton("Commencer le Jeu")
        self.start_game_button.clicked.connect(self.start_game)
        layout.addWidget(self.start_game_button)

        self.setLayout(layout)

    def start_game(self):
        character_data = {
            "race": self.race_options.currentText(),
            "class": self.class_options.currentText(),
            "hair_style": self.hair_style_options.currentText(),
            "hair_color": self.hair_color.value(),
            "face": self.face_group.checkedButton().text(),
            "eye_color": self.eye_color_options.currentText(),
            "skin_color": self.skin_color.value(),
            "strength": self.strength_points.value(),
            "intelligence": self.intelligence_points.value(),
            "dexterity": self.dexterity_points.value(),
            "equipment": self.equipment_list.currentText()
        }
        self.start_game_callback(character_data)
