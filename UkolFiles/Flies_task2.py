#Task 2

class FileStatistics:
    def __init__(self, source_file, target_file):
        self.source_file = source_file
        self.target_file = target_file

    def calculate_statistics(self):
        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        digits = "0123456789"


        total_characters = 0
        total_lines = 0
        total_vowels = 0
        total_consonants = 0
        total_digits = 0


        with open(self.source_file, 'r') as file:
            for line in file:
                total_lines += 1
                for char in line:
                    total_characters += 1
                    if char in vowels:
                        total_vowels += 1
                    elif char in consonants:
                        total_consonants += 1
                    elif char in digits:
                        total_digits += 1


        self.write_statistics(total_characters, total_lines, total_vowels, total_consonants, total_digits)

    def write_statistics(self, total_characters, total_lines, total_vowels, total_consonants, total_digits):
        statistics = (
            f"Total Characters: {total_characters}\n"
            f"Total Lines: {total_lines}\n"
            f"Total Vowels: {total_vowels}\n"
            f"Total Consonants: {total_consonants}\n"
            f"Total Digits: {total_digits}\n"
        )

        with open(self.target_file, 'w') as file:
            file.write(statistics)



source_file = 'file3.txt'
target_file = 'file4.txt'


with open(source_file, 'w') as file:
    file.write("""
    This is a sample text.
    It contains 123 digits, vowels, and consonants!
    Let's see how many of each we have.
    The number of characters and lines should also be counted.
    """)


statistics = FileStatistics(source_file, target_file)


statistics.calculate_statistics()


with open(target_file, 'r') as file:
    print(file.read())