import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox, QInputDialog
from game.ui import MainMenu
from game.character import CharacterCreation
from game.map import GameMap
from game.combat import CombatInterface
from game.dialogue import DialogueInterface
from game.inventory import InventoryInterface
from game.options import OptionsMenu
from game.loot import LootWindow

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Les Chroniques de l'Ancienne Cité")
        self.setGeometry(100, 100, 800, 600)
        self.character_data = None

        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        self.main_menu = MainMenu(self)
        self.stack.addWidget(self.main_menu)

        self.character_creation = CharacterCreation(self, self.start_game)
        self.stack.addWidget(self.character_creation)

    def show_main_menu(self):
        self.stack.setCurrentWidget(self.main_menu)

    def show_character_creation(self):
        self.stack.setCurrentWidget(self.character_creation)

    def start_game(self, character_data):
        print("Starting game with character data:", character_data)
        self.character_data = character_data
        self.character_data['stats'] = {
            'strength': self.character_data.get('strength', 0),
            'intelligence': self.character_data.get('intelligence', 0),
            'dexterity': self.character_data.get('dexterity', 0)
        }
        print("Character data with stats:", self.character_data)
        self.show_game_map()

    def show_game_map(self):
        print("Showing game map")
        self.game_map = GameMap(self, self.character_data, self.show_options)
        self.stack.addWidget(self.game_map)
        self.stack.setCurrentWidget(self.game_map)

    def show_combat_interface(self):
        self.combat_interface = CombatInterface(self)
        self.stack.addWidget(self.combat_interface)
        self.stack.setCurrentWidget(self.combat_interface)

    def show_dialogue_interface(self):
        self.dialogue_interface = DialogueInterface(self)
        self.stack.addWidget(self.dialogue_interface)
        self.stack.setCurrentWidget(self.dialogue_interface)

    def show_inventory_interface(self):
        self.inventory_interface = InventoryInterface(self)
        self.stack.addWidget(self.inventory_interface)
        self.stack.setCurrentWidget(self.inventory_interface)

    def show_loot_window(self, items):
        self.loot_window = LootWindow(self, items)
        self.loot_window.show()

    def add_item_to_inventory(self, name, description, category="Tous"):
        self.inventory_interface.add_item(name, description, category)

    def show_options(self):
        self.options_menu = OptionsMenu(self, self.resume_game, self.save_game, self.back_to_main_menu)
        self.stack.addWidget(self.options_menu)
        self.stack.setCurrentWidget(self.options_menu)

    def resume_game(self):
        self.stack.setCurrentWidget(self.game_map)

    def save_game(self, save_name):
        if not os.path.exists('saves'):
            os.makedirs('saves')
        save_data = {
            "character_data": self.character_data,
            "current_room": self.game_map.current_room,
            "visited_rooms": list(self.game_map.visited_rooms)
        }
        with open(f"saves/{save_name}.json", "w") as save_file:
            json.dump(save_data, save_file)
        QMessageBox.information(self, "Sauvegarde", "Partie sauvegardée avec succès")

    def back_to_main_menu(self):
        reply = QMessageBox.question(self, 'Retour au Menu Principal', 'Voulez-vous sauvegarder avant de quitter?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            save_name, ok = QInputDialog.getText(self, 'Nom de la Sauvegarde', 'Entrez le nom de la sauvegarde:')
            if ok and save_name:
                self.save_game(save_name)
        self.show_main_menu()

    def load_game(self, save_name):
        try:
            with open(f"saves/{save_name}.json", "r") as save_file:
                save_data = json.load(save_file)
            self.character_data = save_data["character_data"]
            self.show_game_map()
            self.game_map.current_room = tuple(save_data["current_room"])
            self.game_map.visited_rooms = set(map(tuple, save_data["visited_rooms"]))
            self.game_map.update_map()
            self.game_map.display_events()
        except FileNotFoundError:
            QMessageBox.warning(self, "Erreur", "La sauvegarde n'a pas été trouvée")

    def get_save_files(self):
        if not os.path.exists('saves'):
            return []
        return [f.split('.')[0] for f in os.listdir('saves') if f.endswith('.json')]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec_())
