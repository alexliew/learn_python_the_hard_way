tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# while True:
# for i in ["/","-","|","\\","|"]:
#     print("{!s}\r".format(i), end=" ")

print("test\r", end=" ")
print("hey\v", end=" ")
print('meow\b', end=" ")
print('duh\f', end=" ")
print('huh\a\r', end=" ")
print('\ba')
# print('\u0238')

print("{!r}".format("\""))
print("{!r}".format("\'"))
print("{!r}".format("\t"))
print("{!r}".format("\a"))
print("{!r}".format("\b"))
print("{!r}".format("\r"))
print("{!s}".format("\""))
print("{!s}".format("\'"))
print('''
      'This is a test'
      ''')
print("""
      "This is a test"
      """)
