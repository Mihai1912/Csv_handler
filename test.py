# import re

# def replace_escape_quotes(line):
#     return line.replace('\\"', "'")


# delimitator = ','
# line = 'euro-hygiene-34.fr,"134 rue entrepreneurs, za du vigné, 30420, calvisson, france, languedoc-roussillon","",calvisson,fr,france,"","",https://euro-hygiene-34.fr,Euro Hygiène,LocalBusiness,"","",occ,occitanie,30420'

# line = replace_escape_quotes(line)
# print (line)
# parts = []
# current_part = []  # A list to hold characters of the current part
# inside_quotes = False  # State flag indicating whether we're inside quotes

# for char in line:
#     if char == '"':
#         # Toggle the state flag when we encounter a quote
#         inside_quotes = not inside_quotes
#     elif char == delimitator and not inside_quotes:
#         # If we're not inside quotes and see the separator, we finish the current part
#         parts.append(''.join(current_part))
#         current_part = []  # Reset for the next part
#     else:
#         # Otherwise, keep adding characters to the current part
#         current_part.append(char)

# # Don't forget to add the last part after exiting the loop
# parts.append(''.join(current_part))

# print (type(parts))
# print (parts)
# print (parts.__len__())
def split_on_separator_outside_quotes(s, separator=','):
    parts = []
    current_part = []
    inside_quotes = False
    for char in s:
        if char == '"' and not inside_quotes:
            inside_quotes = True
        elif char == '"' and inside_quotes:
            inside_quotes = False
        elif char == separator and not inside_quotes:
            parts.append(''.join(current_part))
            current_part = []
        else:
            current_part.append(char)
    parts.append(''.join(current_part))  # Add the last part
    return parts

# Example usage
s = 'hello,world,"yes,no",maybe'
separator = ','
print(split_on_separator_outside_quotes(s, separator))
