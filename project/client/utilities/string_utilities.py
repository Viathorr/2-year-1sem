class StringUtilities:
    @staticmethod
    def is_empty_string(string):
        return all(char.isspace() for char in string)

    @staticmethod
    def contains_newline_char(string):
        if '\n' in string:
            return True
        return False
