import re

# txt = "My Name is Piyush Sharma.I am Currently Living in Gandhinagar.This is a Text Message to work on RegeX"
# x = re.search("^My .*RegeX$", txt)
# print(x)

# txt = """
# Åland My 1st Name is Piyush sharma Is
# my name is Dhruv sharma
# my mobile no is 9998522341
# my elder sister name is denuka sharma
# my mom name name is shashi sharma
# my dad name id vishnu sharma
# """
# pattern = """
# [A-Za-z]* # start with any letter
# sh+       # contains sh in the word
# [a-z]*    #followed by any small letter
# """
# print('\n\nUsing the ASCII', re.findall(r"\w", txt, re.A))
# print('\n\nUsing the DOTALL', re.findall("me.is", txt, re.S))
# print('\n\nUsing the IGNORECASE', re.findall(r"is", txt, re.I))
# print('\n\nUsing the MULTILINE', re.findall("^my", txt, re.M))
# print('\n\nUsing the UNICODE', re.findall(r"\w", txt, re.U))
# print('\n\nUsing the VERBOSE', re.findall(pattern, txt, re.X))
# print('\n\nUsing the DEBUG', re.findall("Piyush", txt, re.DEBUG))

# txt = "The rain in Spain"
# print(re.findall(r'\w', txt))
# print(re.findall(r'\d', txt))
# print(re.findall(r'\S', txt))
# print(re.findall('ai', txt))

# txt = "The air and The rain in Spain again AIR"

# split_example = re.split(r'\s', txt, 2, re.I)
# print('\nThis is the Split Example :', split_example)

# print('\nThis is the Findall Example :', re.findall('air', txt, re.I))

# res = re.search(r'\s', txt, re.I)
# print('\nThe Below is the Search Example :\nThe txt is :', txt,'\nThe Index of the White Space is :', res.start())
# print('Is Spain There in the Txt ?', 'Yes' if re.search('Spain', txt) else 'No')
# print('Is China There in the Txt ?', 'Yes' if re.search('China', txt) else 'No')

# sub_example = re.sub('air', 'hawa', txt, 2, re.I)
# print('\nThis is the Sub Example :', sub_example)

txt = """
The air and The rain in Spain again AIR
There is no hawa in this line
"""

search_example = re.search('ai', txt, re.I)
print('\nThis is the span() Search Example :', search_example.span()) # returns a tuple containing the start, and end positions of the match.
print('\nThis is the string() Search Example :', search_example.string) # returns the string passed into the function
print('\nThis is the group() Search Example :', search_example.group()) # returns the part of the string where there was a match
