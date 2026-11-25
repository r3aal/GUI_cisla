import tkinter as tk

cisla = []

def pridej_cislo():
    text = textove_pole.get()
    try:
        cislo = int(text)

    except ValueError:
        return

    cisla.append(cislo)
    textove_pole.delete(0, tk.END)

    soucet = sum(cisla)
    text_seznamu = "; ".join(str(predmet) for predmet in cisla)

    pole_souctu.config(text = soucet)
    seznam_cisel_pole.config(text = text_seznamu)

def resetuj_vse():
    cisla.clear()
    textove_pole.delete(0, tk.END)
    pole_souctu.config(text = "Zadne cisla pro secteni")
    seznam_cisel_pole.config(text = "Cekam na cisla...")

okno = tk.Tk()
okno.title("Hlavni okno")
okno.geometry("300x300")

nove_cislo_nadpis = tk.Label(okno, text = "Nove cislo:")
nove_cislo_nadpis.pack(pady = (5, 2))

textove_pole = tk.Entry(okno, width = 20)
textove_pole.pack(pady = (0, 5))

pridej_cislo_tlacitko = tk.Button(okno, text = "Pridat cislo", command = pridej_cislo)
pridej_cislo_tlacitko.pack(pady = (0, 5))

reset_tlacitko = tk.Button(okno, text = "Reset", command = resetuj_vse)
reset_tlacitko.pack(pady = 1)

soucet_cisel_nadpis = tk.Label(okno, text = "Soucet cisel:")
soucet_cisel_nadpis.pack(pady = (5, 2))

pole_souctu = tk.Label(okno, text = "Zadne cisla pro secteni")
pole_souctu.pack()

seznam_cisel_nadpis = tk.Label(okno, text = "Seznam cisel:")
seznam_cisel_nadpis.pack(pady = (10, 2))

seznam_cisel_pole = tk.Label(okno, text = "Cekam na cisla...")
seznam_cisel_pole.pack()

okno.mainloop()