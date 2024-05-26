from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QComboBox, QLabel, QInputDialog

class MainMenu(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Nouveau Jeu
        self.new_game_button = QPushButton("Nouveau Jeu")
        self.new_game_button.clicked.connect(self.parent.show_character_creation)
        layout.addWidget(self.new_game_button)

        # Charger Jeu
        self.load_game_button = QPushButton("Charger Jeu")
        self.load_game_button.clicked.connect(self.load_game)
        layout.addWidget(self.load_game_button)

        # Liste déroulante des sauvegardes
        self.save_files_dropdown = QComboBox()
        self.update_save_files_dropdown()
        layout.addWidget(self.save_files_dropdown)

        # Options
        self.options_button = QPushButton("Options")
        self.options_button.clicked.connect(self.parent.show_options)
        layout.addWidget(self.options_button)

        # Quitter
        self.quit_button = QPushButton("Quitter")
        self.quit_button.clicked.connect(self.parent.close)
        layout.addWidget(self.quit_button)

        self.setLayout(layout)

    def update_save_files_dropdown(self):
        self.save_files_dropdown.clear()
        save_files = self.parent.get_save_files()
        self.save_files_dropdown.addItems(save_files)

    def load_game(self):
        save_name = self.save_files_dropdown.currentText()
        if save_name:
            self.parent.load_game(save_name)
