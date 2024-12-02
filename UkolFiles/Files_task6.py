class FileReplacer:
    def __init__(self, source_file, target_word, replacement_word):
        self.source_file = source_file
        self.target_word = target_word
        self.replacement_word = replacement_word

    def replace_word_in_file(self):
        try:

            with open(self.source_file, 'r') as file:
                lines = file.readlines()


            updated_lines = []
            for line in lines:
                updated_lines.append(line.replace(self.target_word, self.replacement_word))


            with open(self.source_file, 'w') as file:
                file.writelines(updated_lines)

            print(f"The word '{self.target_word}' was replaced with '{self.replacement_word}' in the file.")

        except FileNotFoundError:
            print(f"Error: The file {self.source_file} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")





source_file = 'file8.txt'


with open(source_file, 'w') as file:
    file.write("""Tohle je první řádek.
Tohle je druhý řádek s více textem.
Tento je třetí.
Tento řádek je nejdelší protože obsahuje nejvíce znaků.
Čtvrtý řádek.
""")


target_word = input("Enter the word to search for: ").strip()
replacement_word = input("Enter the word to replace it with: ").strip()


replacer = FileReplacer(source_file, target_word, replacement_word)


replacer.replace_word_in_file()


with open(source_file, 'r') as file:
    print("\nUpdated file content:")
    print(file.read())