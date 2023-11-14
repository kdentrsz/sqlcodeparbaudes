import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sqlite3

class DatabaseManager:
    def __init__(self, db_name='nomafinalfinalfinal.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Klienti (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Vards TEXT,
                Uzvards TEXT,
                PersonasKods TEXT,
                TelefonaNumurs TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Nominacijas (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Kategorija TEXT,
                ProduktaNosaukums TEXT,
                TehniskieRaksturojumi TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Noma (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NominacijaID INTEGER,
                KlientaID INTEGER,
                NomaIlgums INTEGER,
                KopejaCena REAL,
                ProduktsPieejams TEXT,
                NomaCenaDiena REAL,
                FOREIGN KEY (NominacijaID) REFERENCES Nominacijas (ID),
                FOREIGN KEY (KlientaID) REFERENCES Klienti (ID)
            )
        ''')

        self.conn.commit()

    def insert_klients(self, vards, uzvards, personas_kods, telefona_numurs):
        self.cursor.execute('''
            INSERT INTO Klienti (Vards, Uzvards, PersonasKods, TelefonaNumurs)
            VALUES (?, ?, ?, ?)
        ''', (vards, uzvards, personas_kods, telefona_numurs))

        self.conn.commit()

    def insert_nominacijas(self, kategorija, produkta_nosaukums, tehniskie_raksturojumi):
        self.cursor.execute('''
            INSERT INTO Nominacijas (Kategorija, ProduktaNosaukums, TehniskieRaksturojumi)
            VALUES (?, ?, ?)
        ''', (kategorija, produkta_nosaukums, tehniskie_raksturojumi))

        self.conn.commit()

    def insert_noma(self, nominacija_id, klienta_id, noma_ilgums, kopeja_cena, produkts_pieejams, noma_cena_diena):
        self.cursor.execute('''
            INSERT INTO Noma (NominacijaID, KlientaID, NomaIlgums, KopejaCena, ProduktsPieejams, NomaCenaDiena)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nominacija_id, klienta_id, noma_ilgums, kopeja_cena, produkts_pieejams, noma_cena_diena))

        self.conn.commit()

class KlientiTab:
    def __init__(self, parent, db_manager):
        self.parent = parent
        self.db_manager = db_manager

        frame_klients = ttk.Frame(self.parent)
        frame_klients.grid(row=0, column=0, padx=10, pady=10)

        label_vards = ttk.Label(frame_klients, text="Vards:")
        label_vards.grid(row=0, column=0, padx=5, pady=5)
        self.entry_vards = ttk.Entry(frame_klients)
        self.entry_vards.grid(row=0, column=1, padx=5, pady=5)

        label_uzvards = ttk.Label(frame_klients, text="Uzvards:")
        label_uzvards.grid(row=1, column=0, padx=5, pady=5)
        self.entry_uzvards = ttk.Entry(frame_klients)
        self.entry_uzvards.grid(row=1, column=1, padx=5, pady=5)

        label_personas_kods = ttk.Label(frame_klients, text="Personas Kods:")
        label_personas_kods.grid(row=2, column=0, padx=5, pady=5)
        self.entry_personas_kods = ttk.Entry(frame_klients)
        self.entry_personas_kods.grid(row=2, column=1, padx=5, pady=5)

        label_telefona_numurs = ttk.Label(frame_klients, text="Telefona Numurs:")
        label_telefona_numurs.grid(row=3, column=0, padx=5, pady=5)
        self.entry_telefona_numurs = ttk.Entry(frame_klients)
        self.entry_telefona_numurs.grid(row=3, column=1, padx=5, pady=5)

        button_klients = ttk.Button(frame_klients, text="Pievienot Klientu", command=self.insert_klients)
        button_klients.grid(row=4, column=0, columnspan=2, pady=10)

    def insert_klients(self):
        vards = self.entry_vards.get()
        uzvards = self.entry_uzvards.get()
        personas_kods = self.entry_personas_kods.get()
        telefona_numurs = self.entry_telefona_numurs.get()

        self.db_manager.insert_klients(vards, uzvards, personas_kods, telefona_numurs)

class NominacijasTab:
    def __init__(self, parent, db_manager):
        self.parent = parent
        self.db_manager = db_manager

        frame_nominacijas = ttk.Frame(self.parent)
        frame_nominacijas.grid(row=0, column=1, padx=10, pady=10)

        label_kategorija = ttk.Label(frame_nominacijas, text="Kategorija:")
        label_kategorija.grid(row=0, column=0, padx=5, pady=5)
        self.entry_kategorija = ttk.Entry(frame_nominacijas)
        self.entry_kategorija.grid(row=0, column=1, padx=5, pady=5)

        label_produkta_nosaukums = ttk.Label(frame_nominacijas, text="Produkta Nosaukums:")
        label_produkta_nosaukums.grid(row=1, column=0, padx=5, pady=5)
        self.entry_produkta_nosaukums = ttk.Entry(frame_nominacijas)
        self.entry_produkta_nosaukums.grid(row=1, column=1, padx=5, pady=5)

        label_tehniskie_raksturojumi = ttk.Label(frame_nominacijas, text="Tehniskie Raksturojumi:")
        label_tehniskie_raksturojumi.grid(row=2, column=0, padx=5, pady=5)
        self.entry_tehniskie_raksturojumi = ttk.Entry(frame_nominacijas)
        self.entry_tehniskie_raksturojumi.grid(row=2, column=1, padx=5, pady=5)


        button_nominacijas = ttk.Button(frame_nominacijas, text="Pievienot Nominaciju", command=self.insert_nominacijas)
        button_nominacijas.grid(row=4, column=0, columnspan=2, pady=10)

    def insert_nominacijas(self):
        kategorija = self.entry_kategorija.get()
        produkta_nosaukums = self.entry_produkta_nosaukums.get()
        tehniskie_raksturojumi = self.entry_tehniskie_raksturojumi.get()
       

        self.db_manager.insert_nominacijas(kategorija, produkta_nosaukums, tehniskie_raksturojumi)

class NomaTab:
    def __init__(self, parent, db_manager):
        self.parent = parent
        self.db_manager = db_manager

        frame_noma = ttk.Frame(self.parent)
        frame_noma.grid(row=0, column=2, padx=10, pady=10)

        label_sakuma_datums = ttk.Label(frame_noma, text="Sākuma Datums:")
        label_sakuma_datums.grid(row=0, column=0, padx=5, pady=5)
        self.entry_sakuma_datums = ttk.Entry(frame_noma)
        self.entry_sakuma_datums.grid(row=0, column=1, padx=5, pady=5)

        label_beigu_datums = ttk.Label(frame_noma, text="Beigu Datums:")
        label_beigu_datums.grid(row=1, column=0, padx=5, pady=5)
        self.entry_beigu_datums = ttk.Entry(frame_noma)
        self.entry_beigu_datums.grid(row=1, column=1, padx=5, pady=5)

        label_produkts_pieejams = ttk.Label(frame_noma, text="Produkts pieejams:")
        label_produkts_pieejams.grid(row=2, column=0, padx=5, pady=5)
        self.produkts_pieejams = ttk.Entry(frame_noma)
        self.produkts_pieejams.grid(row=2, column=1, padx=5, pady=5)

        
        label_noma_cena_diena = ttk.Label(frame_noma, text="Noma Cena Dienā:")
        label_noma_cena_diena.grid(row=3, column=0, padx=5, pady=5)
        self.entry_noma_cena_diena = ttk.Entry(frame_noma)
        self.entry_noma_cena_diena.grid(row=3, column=1, padx=5, pady=5)

        button_noma = ttk.Button(frame_noma, text="Pievienot Nomu", command=self.insert_noma)
        button_noma.grid(row=4, column=0, columnspan=2, pady=10)

    def insert_noma(self):
        nominacija_id = 1
        klienta_id = 1

        sakuma_datums_str = self.entry_sakuma_datums.get()
        beigu_datums_str = self.entry_beigu_datums.get()

        sakuma_datums = datetime.strptime(sakuma_datums_str, "%d.%m.%Y")
        beigu_datums = datetime.strptime(beigu_datums_str, "%d.%m.%Y")

        noma_ilgums = (beigu_datums - sakuma_datums).days
        noma_cena_diena = float(self.entry_noma_cena_diena.get())  

        kopeja_cena = noma_ilgums * noma_cena_diena
        produkts_pieejams = self.produkts_pieejams.get()

        self.db_manager.insert_noma(nominacija_id, klienta_id, noma_ilgums, kopeja_cena, produkts_pieejams, noma_cena_diena)

if __name__ == "__main__":
    root = tk.Tk()
    db_manager = DatabaseManager()

    klients_tab = KlientiTab(root, db_manager)
    nominacijas_tab = NominacijasTab(root, db_manager)
    noma_tab = NomaTab(root, db_manager)

    root.mainloop()
