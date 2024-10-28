from rich import print
import patoolib
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory

links = []
Tk().withdraw()


def get_links():
    global link
    global outdir
    while True:
        link = askopenfilenames(title="Enter the links you want to extract: ")
        links.append(link)
        break
    outdir = askdirectory(title="Enter where you want the links to end up: ")


def extract_links():
    for link in links[0]:
        try:
            patoolib.extract_archive(f"{link}", outdir=outdir)
        except patoolib.util.PatoolError:
            print(f"An error occured while extracting {link}.")


while True:
    choice = input(
        "Type 'q' to quit.\nDo you want to (e)xtract or move (m)ods? ",
    ).lower()
    if choice == "e":
        get_links()
        extract_links()
        break
    elif choice == "q":
        break
    else:
        print("[red]Please select a correct option.[/red]\n")
