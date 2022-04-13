
from bs4 import BeautifulSoup
import requests
import os

#Colors
grey = "\033[0;90m"
red = "\033[0;91m"
blue = "\033[0;34m"
green = "\033[0;32m"
reset = "\033[0m"

#Colors_bold
redB = "\033[1;91m"
blueB = "\033[1;34m"
greyB = "\033[1;90m"
greenB = "\033[1;32m"

clear_screen = lambda : os.system("cls" if os.name == "nt" else "clear")

def word_search():
    clear_screen()
    while True:
        search_word = input("Indtast venligts det ord du vil undersøge: ")
        source = requests.get(f"https://ordnet.dk/ddo/ordbog?query={search_word}").text

        soup = BeautifulSoup(source, "html.parser")

        article = soup.find("div", class_="artikel")

        try:
            header_match = article.find("span", class_="match").text
            header_class = article.find("span", class_="tekstmedium allow-glossing").text
            break
        except AttributeError:
            print("Ordet du leder efter findes ikke.")


    print(f"\n{blueB}{header_match.capitalize()}{reset}")
    print(header_class.capitalize())

    try:
        inflection_section = article.find(id="id-boj")
        inflection = inflection_section.find("span", class_="tekstmedium allow-glossing").text
        print(f"\n{blueB}Bøjninger:{reset}")
        print(inflection)
    except Exception:
        print(f"\n{blueB}Bøjninger:{reset}")
        print("Der er ingen bøjninger for dette ord.")
        

    try:
        etymologi_section = article.find(id="id-ety")
        etymologi_section_items = etymologi_section.find("span", class_="tekstmedium allow-glossing").text
        etymologi = etymologi_section_items.replace(", ", "\n").replace("  ", " ").capitalize()
        print(f"\n{blueB}Etymologi:{reset}")
        print(etymologi)
    except Exception:
        print(f"\n{blueB}Etymologi:{reset}")
        print("Denne hjemmeside kender ikke oprindelsen af dette ord.")


    print(f"\n{blueB}Definition(er):{reset}")
    definition_section = article.find("div", id="content-betydninger")
    indx = 0
    try:
        while True:
            indx += 1
            definition = definition_section.find("div", id=f"betydning-{indx}").find("span", class_="definition")
            print(f"{blueB}{indx}.{reset} {definition.text.strip().capitalize()}.")
    except AttributeError:
        pass
    except Exception:
        print(f"\n{blueB}Definition(er):{reset}")
        print("Denne hjemmeside kender ingen definitioner af dette ord.")


    try:
        synonym_section = article.find("div", class_="definitionBox onym")
        synonym_section_items = ", ".join([i.text.strip() for i in synonym_section.find("span", class_="inlineList").find_all("a")])
        print()
        print(f"{blueB}Synonym(er):{reset}")
        print(synonym_section_items.capitalize())
    except Exception:
        print(f"\n{blueB}Synonym(er):{reset}")
        print("Denne hjemmeside kender ingen synonymer for dette ord.")

    link = f"https://ordnet.dk/ddo/ordbog?query={search_word}"
    print(f"\n{grey}{link}{reset}\n")

    wantContinue = input("Skal du undersøge endnu et ord? (J/n): ").strip().lower()
    if wantContinue == "n":
        return
    else:
        word_search()
    
word_search()


