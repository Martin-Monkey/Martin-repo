#Task 1

class files_compare:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def compare(self):
        with open(self.file1, 'r') as f1, open(self.file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            for i, (line1, line2) in enumerate(zip(lines1, lines2)):
                if line1 != line2:
                    print(f"Neshodný řádek {i + 1}:")
                    print(f"Soubor 1: {line1.strip()}")
                    print(f"Soubor 2: {line2.strip()}")


# Příklad volání:
comparator = files_compare('file1.txt', 'file2.txt')
comparator.compare()
