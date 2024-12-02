class FileAnalyzer:
    def __init__(self, source_file):
        self.source_file = source_file

    def find_longest_line_length(self):
        try:
            
            with open(self.source_file, 'r') as file:
                lines = file.readlines()


            longest_line_length = 0
            for line in lines:
                line_length = len(line)
                if line_length > longest_line_length:
                    longest_line_length = line_length


            print(f"The length of the longest line is: {longest_line_length}")

        except FileNotFoundError:
            print(f"Error: The file {self.source_file} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")



source_file = 'file7.txt'

with open(source_file, 'w') as file:
    file.write("""Tohle je první řádek.
Tohle je druhý řádek s více textem.
Tento je třetí.
Tento řádek je nejdelší protože obsahuje nejvíce znaků.
Čtvrtý řádek.
""")


analyzer = FileAnalyzer(source_file)
analyzer.find_longest_line_length()