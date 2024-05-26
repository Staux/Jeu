from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QMessageBox

class CombatInterface(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.info_label = QLabel("Interface de Combat", self)
        layout.addWidget(self.info_label)

        self.action_layout = QHBoxLayout()
        self.attack_button = QPushButton("Attaquer")
        self.attack_button.clicked.connect(self.attack)
        self.action_layout.addWidget(self.attack_button)

        self.spell_button = QPushButton("Sort")
        self.spell_button.clicked.connect(self.cast_spell)
        self.action_layout.addWidget(self.spell_button)

        self.item_button = QPushButton("Objet")
        self.item_button.clicked.connect(self.use_item)
        self.action_layout.addWidget(self.item_button)

        self.defend_button = QPushButton("Défendre")
        self.defend_button.clicked.connect(self.defend)
        self.action_layout.addWidget(self.defend_button)

        layout.addLayout(self.action_layout)
        self.setLayout(layout)

    def attack(self):
        QMessageBox.information(self, "Attaquer", "Vous attaquez l'ennemi!")

    def cast_spell(self):
        QMessageBox.information(self, "Sort", "Vous lancez un sort!")

    def use_item(self):
        QMessageBox.information(self, "Objet", "Vous utilisez un objet!")

    def defend(self):
        QMessageBox.information(self, "Défendre", "Vous vous défendez!")
