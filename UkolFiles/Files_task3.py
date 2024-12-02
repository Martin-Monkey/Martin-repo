class FileProcessor:
    def __init__(self, source_file, target_file):
        self.source_file = source_file
        self.target_file = target_file

    def remove_last_line_and_save(self):
        try:
            
            with open(self.source_file, 'r') as file:
                lines = file.readlines()


            if lines:
                lines = lines[:-1]


            with open(self.target_file, 'w') as file:
                file.writelines(lines)

            print(f"Last line removed successfully. Results saved in {self.target_file}")

        except FileNotFoundError:
            print(f"Error: The file {self.source_file} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


source_file = 'file5.txt'
target_file = 'file6.txt'


with open(source_file, 'w') as file:
    file.write("""This is the first line.
This is the second line.
This is the third line.
This is the fourth line.
This is the last line.
""")


processor = FileProcessor(source_file, target_file)


processor.remove_last_line_and_save()


with open(target_file, 'r') as file:
    print("Content of file6.txt after removing the last line:")
    print(file.read())