from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTreeWidget, QTreeWidgetItem, QCheckBox

class LootWindow(QWidget):
    def __init__(self, parent, items):
        super().__init__(parent)
        self.parent = parent
        self.items = items
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.loot_tree = QTreeWidget()
        self.loot_tree.setHeaderLabels(["Nom de l'objet", "Description", "Prendre"])
        for name, description in self.items:
            item = QTreeWidgetItem([name, description])
            checkbox = QCheckBox()
            self.loot_tree.addTopLevelItem(item)
            self.loot_tree.setItemWidget(item, 2, checkbox)
        layout.addWidget(self.loot_tree)

        self.take_all_button = QPushButton("Tout prendre")
        self.take_all_button.clicked.connect(self.take_all)
        layout.addWidget(self.take_all_button)

        self.take_selected_button = QPushButton("Prendre sélectionnés")
        self.take_selected_button.clicked.connect(self.take_selected)
        layout.addWidget(self.take_selected_button)

        self.cancel_button = QPushButton("Annuler")
        self.cancel_button.clicked.connect(self.close)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

    def take_all(self):
        for i in range(self.loot_tree.topLevelItemCount()):
            item = self.loot_tree.topLevelItem(i)
            self.parent.add_item_to_inventory(item.text(0), item.text(1))
        self.close()

    def take_selected(self):
        for i in range(self.loot_tree.topLevelItemCount()):
            item = self.loot_tree.topLevelItem(i)
            checkbox = self.loot_tree.itemWidget(item, 2)
            if checkbox.isChecked():
                self.parent.add_item_to_inventory(item.text(0), item.text(1))
        self.close()
