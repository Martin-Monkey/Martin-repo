class WordCounter:
    def __init__(self, source_file, target_word):
        self.source_file = source_file
        self.target_word = target_word.lower()  # Prohledávání je case-insensitive

    def count_word_occurrences(self):
        try:
            word_count = 0

            # Otevřeme soubor a načteme všechny řádky
            with open(self.source_file, 'r') as file:
                for line in file:
                    # Spočítáme výskyt slova v aktuálním řádku
                    word_count += line.lower().count(self.target_word)

            # Výstup: Vytiskneme celkový počet výskytů slova
            print(f"Slovo '{self.target_word}' se vyskytuje {word_count} krát v souboru.")

        except FileNotFoundError:
            print(f"Error: The file {self.source_file} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


# Předpokládejme, že soubor 'file7.txt' již existuje

# Parametry: Cesta k souboru a hledané slovo ("line")
source_file = 'file7.txt'
target_word = 'řádek'

# Vytvoření objektu třídy WordCounter pro hledání slova "line"
counter = WordCounter(source_file, target_word)

# Spočítáme výskyty slova "line"
counter.count_word_occurrences()