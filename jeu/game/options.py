from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QComboBox, QCheckBox, QPushButton, QLineEdit

class OptionsMenu(QWidget):
    def __init__(self, parent, resume_game_callback, save_game_callback, back_to_main_menu_callback):
        super().__init__(parent)
        self.parent = parent
        self.resume_game_callback = resume_game_callback
        self.save_game_callback = save_game_callback
        self.back_to_main_menu_callback = back_to_main_menu_callback
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Audio Options
        audio_layout = QVBoxLayout()
        audio_label = QLabel("Audio")
        audio_layout.addWidget(audio_label)

        self.volume_general = QSlider(Qt.Horizontal)
        self.volume_general.setRange(0, 100)
        self.volume_general.setValue(50)
        audio_layout.addWidget(QLabel("Volume Général"))
        audio_layout.addWidget(self.volume_general)

        self.volume_fx = QSlider(Qt.Horizontal)
        self.volume_fx.setRange(0, 100)
        self.volume_fx.setValue(50)
        audio_layout.addWidget(QLabel("Volume des Effets Sonores"))
        audio_layout.addWidget(self.volume_fx)

        self.volume_music = QSlider(Qt.Horizontal)
        self.volume_music.setRange(0, 100)
        self.volume_music.setValue(50)
        audio_layout.addWidget(QLabel("Volume de la Musique"))
        audio_layout.addWidget(self.volume_music)

        layout.addLayout(audio_layout)

        # Video Options
        video_layout = QVBoxLayout()
        video_label = QLabel("Vidéo")
        video_layout.addWidget(video_label)

        self.resolution_option = QComboBox()
        self.resolution_option.addItems(["800x600", "1024x768", "1280x720", "1920x1080"])
        video_layout.addWidget(QLabel("Résolution de l'Écran"))
        video_layout.addWidget(self.resolution_option)

        self.fullscreen_check = QCheckBox("Mode Plein Écran")
        video_layout.addWidget(self.fullscreen_check)

        self.quality_option = QComboBox()
        self.quality_option.addItems(["Basse", "Moyenne", "Haute"])
        video_layout.addWidget(QLabel("Qualité des Textures"))
        video_layout.addWidget(self.quality_option)

        self.effects_check = QCheckBox("Effets Visuels")
        video_layout.addWidget(self.effects_check)

        layout.addLayout(video_layout)

        # Controls Options
        controls_layout = QVBoxLayout()
        controls_label = QLabel("Contrôles")
        controls_layout.addWidget(controls_label)

        self.sensitivity_scale = QSlider(Qt.Horizontal)
        self.sensitivity_scale.setRange(0, 100)
        self.sensitivity_scale.setValue(50)
        controls_layout.addWidget(QLabel("Sensibilité de la Souris"))
        controls_layout.addWidget(self.sensitivity_scale)

        layout.addLayout(controls_layout)

        # Gameplay Options
        gameplay_layout = QVBoxLayout()
        gameplay_label = QLabel("Gameplay")
        gameplay_layout.addWidget(gameplay_label)

        self.difficulty_option = QComboBox()
        self.difficulty_option.addItems(["Facile", "Normal", "Difficile"])
        gameplay_layout.addWidget(QLabel("Niveau de Difficulté"))
        gameplay_layout.addWidget(self.difficulty_option)

        self.accessibility_check = QCheckBox("Sous-titres")
        gameplay_layout.addWidget(self.accessibility_check)

        layout.addLayout(gameplay_layout)

        # Save and Load Options
        save_load_layout = QVBoxLayout()
        save_load_label = QLabel("Sauvegarde et Chargement")
        save_load_layout.addWidget(save_load_label)

        self.save_name = QLineEdit()
        self.save_name.setPlaceholderText("Nom de la sauvegarde")
        save_load_layout.addWidget(self.save_name)

        save_button = QPushButton("Sauvegarder")
        save_button.clicked.connect(self.save_game)
        save_load_layout.addWidget(save_button)

        layout.addLayout(save_load_layout)

        # Back to Main Menu
        back_button = QPushButton("Menu Principal")
        back_button.clicked.connect(self.back_to_main_menu_callback)
        layout.addWidget(back_button)

        # Resume Game
        resume_button = QPushButton("Reprendre")
        resume_button.clicked.connect(self.resume_game_callback)
        layout.addWidget(resume_button)

        self.setLayout(layout)

    def save_game(self):
        save_name = self.save_name.text().strip()
        if save_name:
            self.save_game_callback(save_name)
        else:
            self.save_game_callback("Sauvegarde sans nom")
