# cislo.py

class Number:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def to_octal(self):
        return oct(self.value)[2:]  # oct() returns a string starting with "0o", remove "0o"

    def to_hexadecimal(self):
        return hex(self.value)[2:]  # hex() returns a string starting with "0x", remove "0x"

    def to_binary(self):
        return bin(self.value)[2:]  # bin() returns a string starting with "0b", remove "0b"
