from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QTextEdit
from PyQt5.QtCore import Qt, QRectF

class GameMap(QWidget):
    def __init__(self, parent, character_data, show_options_callback):
        super().__init__(parent)
        self.parent = parent
        self.character_data = character_data
        self.show_options_callback = show_options_callback
        self.current_room = (0, 0)
        self.visited_rooms = set()
        self.labyrinth = self.create_labyrinth()
        print("Character data received in GameMap:", self.character_data)
        self.init_ui()

    def create_labyrinth(self):
        return {
            (0, 0): ["Start Room"],
            (1, 0): ["Corridor"],
            (2, 0): ["Corridor"],
            (3, 0): ["Corridor"],
            (3, 1): ["Corridor"],
            (3, 2): ["Boss Room"],
            (2, 2): ["Corridor"],
            (1, 2): ["Corridor"],
            (0, 2): ["Corridor"],
            (0, 1): ["Resting area"],
            (-1, 0): ["Corridor"],
            (-2, 0): ["Treasure Room", "Find the Legendary Dragon Key"],
            (-2, 1): ["Corridor"],
            (-2, 2): ["Corridor"],
            (-1, 2): ["Corridor"]
        }

    def init_ui(self):
        layout = QVBoxLayout()

        # Mini-Map
        self.mini_map_layout = QHBoxLayout()
        self.map_view = QGraphicsView()
        self.map_scene = QGraphicsScene()
        self.map_view.setScene(self.map_scene)
        self.map_view.setFixedSize(200, 200)
        self.mini_map_layout.addWidget(self.map_view)
        layout.addLayout(self.mini_map_layout)

        self.update_map()

        # Player stats and inventory button
        self.stats_layout = QVBoxLayout()
        
        self.character_info = QLabel(f"Personnage : {self.character_data['race']} {self.character_data['class']}", self)
        self.stats_layout.addWidget(self.character_info)

        self.stats_info = QLabel(f"Stats: {self.character_data['stats']}", self)
        self.stats_layout.addWidget(self.stats_info)

        self.equipment_info = QLabel(f"Équipement: {self.character_data['equipment']}", self)
        self.stats_layout.addWidget(self.equipment_info)

        self.inventory_button = QPushButton("Inventaire")
        self.inventory_button.clicked.connect(self.show_inventory)
        self.stats_layout.addWidget(self.inventory_button)
        
        layout.addLayout(self.stats_layout)

        # Game controls and event display
        self.controls_layout = QVBoxLayout()

        self.top_button = QPushButton("Porte Haut")
        self.top_button.clicked.connect(lambda: self.move_player(0, -1))
        self.controls_layout.addWidget(self.top_button, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self.middle_layout = QHBoxLayout()

        self.left_button = QPushButton("Porte Gauche")
        self.left_button.clicked.connect(lambda: self.move_player(-1, 0))
        self.middle_layout.addWidget(self.left_button, alignment=Qt.AlignLeft)

        self.right_button = QPushButton("Porte Droite")
        self.right_button.clicked.connect(lambda: self.move_player(1, 0))
        self.middle_layout.addWidget(self.right_button, alignment=Qt.AlignRight)

        self.controls_layout.addLayout(self.middle_layout)

        self.bottom_button = QPushButton("Porte Bas")
        self.bottom_button.clicked.connect(lambda: self.move_player(0, 1))
        self.controls_layout.addWidget(self.bottom_button, alignment=Qt.AlignBottom | Qt.AlignHCenter)

        layout.addLayout(self.controls_layout)

        # Event display area
        self.event_display = QTextEdit()
        self.event_display.setReadOnly(True)
        layout.addWidget(self.event_display)

        self.options_button = QPushButton("Options")
        self.options_button.clicked.connect(self.show_options_callback)
        layout.addWidget(self.options_button)

        # Zoom controls
        self.zoom_layout = QHBoxLayout()
        self.zoom_in_button = QPushButton("Zoomer")
        self.zoom_in_button.clicked.connect(self.zoom_in)
        self.zoom_layout.addWidget(self.zoom_in_button)

        self.zoom_out_button = QPushButton("Dézoomer")
        self.zoom_out_button.clicked.connect(self.zoom_out)
        self.zoom_layout.addWidget(self.zoom_out_button)

        layout.addLayout(self.zoom_layout)

        self.setLayout(layout)
        self.display_events()

    def update_map(self):
        self.map_scene.clear()
        room_size = 20
        for x in range(-3, 4):
            for y in range(-3, 4):
                room_rect = QRectF(x * room_size, y * room_size, room_size, room_size)
                self.map_scene.addRect(room_rect, brush=Qt.white)

        player_pos = QGraphicsEllipseItem(self.current_room[0] * room_size, self.current_room[1] * room_size, room_size, room_size)
        player_pos.setBrush(Qt.red)
        self.map_scene.addItem(player_pos)

    def move_player(self, dx, dy):
        new_room = (self.current_room[0] + dx, self.current_room[1] + dy)
        if new_room in self.labyrinth:
            if new_room == (3, 2) and not self.parent.inventory_interface.has_item("Clé de dragon légendaire"):
                self.event_display.append("Vous avez besoin de la Clé de dragon légendaire pour entrer dans cette salle.")
                return
            self.current_room = new_room
            if new_room in self.visited_rooms:
                self.update_map()
                self.display_events()
            else:
                self.visited_rooms.add(new_room)
                self.update_map()
                self.display_events()
        else:
            self.event_display.append("Il n'y a pas de passage dans cette direction.")

    def display_events(self):
        events = self.labyrinth.get(self.current_room, ["Aire de repos"])
        self.event_display.clear()
        for event in events:
            self.event_display.append(event)

    def show_inventory(self):
        self.parent.show_inventory_interface()

    def zoom_in(self):
        self.map_view.scale(1.2, 1.2)

    def zoom_out(self):
        self.map_view.scale(1/1.2, 1/1.2)
