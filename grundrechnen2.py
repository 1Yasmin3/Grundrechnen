import tkinter as tk
import random

# Fenster
fenster = tk.Tk()
fenster.title("Zahlen-Spiel")
fenster.geometry("420x400")
fenster.configure(bg="#F2F7FF")  # hellblau

zahlen = []
aktuelle_position = 0

# Große Zahl
label_zahl = tk.Label(
    fenster,
    text="",
    font=("Arial", 52, "bold"),
    bg="#F2F7FF",
    fg="#333333"
)
label_zahl.pack(pady=30)

# Info / Feedback
label_info = tk.Label(
    fenster,
    text="",
    font=("Arial", 16),
    bg="#F2F7FF",
    fg="#333333"
)
label_info.pack(pady=10)

# Eingabe
eingabe = tk.Entry(
    fenster,
    font=("Arial", 18),
    justify="center",
    width=10
)

# Buttons
button_pruefen = tk.Button(
    fenster,
    text="✅ Prüfen",
    font=("Arial", 14),
    bg="#4CAF50",
    fg="white",
    activebackground="#45A049"
)

button_nochmal = tk.Button(
    fenster,
    text="🔁 Nochmal spielen",
    font=("Arial", 14),
    bg="#2196F3",
    fg="white",
    activebackground="#1976D2"
)

def neue_zahl_anzeigen():
    global aktuelle_position

    if aktuelle_position < len(zahlen):
        label_zahl.config(
            text=str(zahlen[aktuelle_position]),
            fg="#333333"
        )
        aktuelle_position += 1
        fenster.after(1000, neue_zahl_anzeigen)
    else:
        label_zahl.config(text="")
        label_info.config(
            text="Wie groß ist die Summe?",
            fg="#333333"
        )
        eingabe.pack(pady=10)
        button_pruefen.pack(pady=10)

def pruefen():
    try:
        antwort = int(eingabe.get())
        richtige_summe = sum(zahlen)

        if antwort == richtige_summe:
            label_info.config(
                text="🎉 Richtig! Super gemacht!",
                fg="#2E7D32"  # grün
            )
        else:
            label_info.config(
                text=f"❌ Fast! Die richtige Summe ist {richtige_summe}",
                fg="#C62828"  # rot
            )

        button_pruefen.pack_forget()
        button_nochmal.pack(pady=15)

    except ValueError:
        label_info.config(
            text="✏️ Bitte eine Zahl eingeben",
            fg="#C62828"
        )

def neues_spiel():
    eingabe.delete(0, tk.END)
    eingabe.pack_forget()
    button_nochmal.pack_forget()

    label_info.config(
        text="Rechne mit!",
        fg="#333333"
    )
    start_spiel()

def start_spiel():
    global zahlen, aktuelle_position
    zahlen = [random.randint(1, 9) for _ in range(5)]
    aktuelle_position = 0
    fenster.after(1000, neue_zahl_anzeigen)

def starten():
    start_button.pack_forget()
    label_info.config(text="Rechne mit!")
    start_spiel()

start_button = tk.Button(
    fenster,
    text="▶ Start",
    font=("Arial", 18),
    bg="#FF9800",
    fg="white",
    activebackground="#FB8C00"
)
start_button.config(command=starten)
start_button.pack(pady=25)

button_pruefen.config(command=pruefen)
button_nochmal.config(command=neues_spiel)

fenster.mainloop()