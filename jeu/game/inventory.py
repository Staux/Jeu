from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTreeWidget, QTreeWidgetItem, QHBoxLayout, QTabWidget
from PyQt5.QtCore import Qt

class InventoryInterface(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.inventory_tree = QTreeWidget()
        self.inventory_tree.setHeaderLabels(["Nom de l'objet", "Description"])
        self.tabs.addTab(self.inventory_tree, "Tous")

        self.weapons_tree = QTreeWidget()
        self.weapons_tree.setHeaderLabels(["Nom de l'objet", "Description"])
        self.tabs.addTab(self.weapons_tree, "Armes")

        self.armor_tree = QTreeWidget()
        self.armor_tree.setHeaderLabels(["Nom de l'objet", "Description"])
        self.tabs.addTab(self.armor_tree, "Armures")

        self.potions_tree = QTreeWidget()
        self.potions_tree.setHeaderLabels(["Nom de l'objet", "Description"])
        self.tabs.addTab(self.potions_tree, "Potions")

        layout.addWidget(self.tabs)

        self.description_label = QLabel("Description de l'objet sélectionné ici")
        layout.addWidget(self.description_label)

        self.inventory_tree.itemSelectionChanged.connect(self.on_item_selected)
        self.weapons_tree.itemSelectionChanged.connect(self.on_item_selected)
        self.armor_tree.itemSelectionChanged.connect(self.on_item_selected)
        self.potions_tree.itemSelectionChanged.connect(self.on_item_selected)

        self.action_layout = QHBoxLayout()
        self.use_item_button = QPushButton("Utiliser")
        self.use_item_button.clicked.connect(self.use_item)
        self.action_layout.addWidget(self.use_item_button)

        self.equip_item_button = QPushButton("Équiper")
        self.equip_item_button.clicked.connect(self.equip_item)
        self.action_layout.addWidget(self.equip_item_button)

        self.remove_item_button = QPushButton("Retirer")
        self.remove_item_button.clicked.connect(self.remove_item)
        self.action_layout.addWidget(self.remove_item_button)

        layout.addLayout(self.action_layout)

        self.back_button = QPushButton("Retour")
        self.back_button.clicked.connect(self.back_to_main)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def add_item(self, name, description, category="Tous"):
        item = QTreeWidgetItem([name, description])
        self.inventory_tree.addTopLevelItem(item)
        if category == "Armes":
            self.weapons_tree.addTopLevelItem(item)
        elif category == "Armures":
            self.armor_tree.addTopLevelItem(item)
        elif category == "Potions":
            self.potions_tree.addTopLevelItem(item)

    def use_item(self):
        selected_item = self.inventory_tree.selectedItems()
        if selected_item:
            item = selected_item[0]
            self.description_label.setText(f"Utilisé: {item.text(0)}")
            # Appliquer l'effet de l'objet (ex: augmenter la santé)
            # self.parent.character_data['stats']['santé'] += 10 # exemple d'effet
            self.inventory_tree.takeTopLevelItem(self.inventory_tree.indexOfTopLevelItem(item))
        else:
            self.description_label.setText("Aucun objet sélectionné")

    def equip_item(self):
        selected_item = self.inventory_tree.selectedItems()
        if selected_item:
            item = selected_item[0]
            self.description_label.setText(f"Équipé: {item.text(0)}")
            # Mettre à jour les attributs du personnage
            # self.parent.character_data['stats']['force'] += 5 # exemple d'effet
            self.inventory_tree.takeTopLevelItem(self.inventory_tree.indexOfTopLevelItem(item))
        else:
            self.description_label.setText("Aucun objet sélectionné")

    def remove_item(self):
        selected_item = self.inventory_tree.selectedItems()
        if selected_item:
            item = selected_item[0]
            self.description_label.setText(f"Jeté: {item.text(0)}")
            # Retirer l'effet de l'objet sur le personnage
            # self.parent.character_data['stats']['force'] -= 5 # exemple d'effet
            self.inventory_tree.takeTopLevelItem(self.inventory_tree.indexOfTopLevelItem(item))
        else:
            self.description_label.setText("Aucun objet sélectionné")

    def on_item_selected(self):
        selected_item = self.inventory_tree.selectedItems()
        if selected_item:
            item = selected_item[0]
            self.description_label.setText(f"Description: {item.text(1)}")

    def back_to_main(self):
        self.parent.show_game_map()

    def has_item(self, item_name):
        return any(item_name in item.text(0) for item in self.inventory_tree.findItems(item_name, Qt.MatchContains))
