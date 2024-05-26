import tkinter as tk
from tkinter import messagebox

class DialogueInterface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        
    def create_widgets(self):
        self.dialogue_frame = tk.Frame(self)
        self.dialogue_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.npc_label = tk.Label(self.dialogue_frame, text="NPC Name", font=("Helvetica", 14))
        self.npc_label.pack(anchor="w")

        self.dialogue_text = tk.Text(self.dialogue_frame, height=10, wrap="word")
        self.dialogue_text.pack(fill="both", padx=10, pady=10)
        self.dialogue_text.insert(tk.END, "Bonjour aventurier. Que veux-tu savoir ?")

        self.options_frame = tk.Frame(self.dialogue_frame)
        self.options_frame.pack(fill="x", padx=10, pady=10)

        self.option1_button = tk.Button(self.options_frame, text="Option 1", command=lambda: self.choose_option(1))
        self.option1_button.pack(fill="x", pady=2)

        self.option2_button = tk.Button(self.options_frame, text="Option 2", command=lambda: self.choose_option(2))
        self.option2_button.pack(fill="x", pady=2)

        self.option3_button = tk.Button(self.options_frame, text="Option 3", command=lambda: self.choose_option(3))
        self.option3_button.pack(fill="x", pady=2)

        self.back_button = tk.Button(self, text="Retour", command=self.back_to_main)
        self.back_button.pack(pady=10)

    def choose_option(self, option):
        roll = self.roll_d20()
        success = roll > 10  # Exemples de vérifications de compétences
        result_text = f"Vous avez choisi l'option {option}. Roll: {roll}. {'Succès' if success else 'Échec'}."
        self.add_to_dialogue_log(result_text)

    def roll_d20(self):
        import random
        return random.randint(1, 20)

    def add_to_dialogue_log(self, text):
        self.dialogue_text.insert(tk.END, f"\n{text}")
        self.dialogue_text.see(tk.END)

    def back_to_main(self):
        self.master.show_main_menu()
