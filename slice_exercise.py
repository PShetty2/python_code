#jan 24, 2022

str1 = "Sheridan College"
#end of slice will be n-1 index)
print(str1[1:4])
print(str1[:5])
#starts at index 4 and continues until end of string
print(str1[4:])
#removes last index
print(str1[0:-1])
print(str1[:-1])

message = "Hello World!"
question = "How many people are living on the earth?"
statement = message[0:2] + question[-1:-3]
print(statement)

print("c:/mydrive/Hello")

print("\t SUP SUP")
print("\n SUP SUP")

print('Before uppercase: ', message)
message_upper = message.upper()
print('After uppercase: ', message_upper)

#center() method
print(message.center(50,'-'))

#count() method
#to have a string span multiple lines, use """"
text = """and and and and and and and and and and to to to to to to to to to to to to to to to to to to to to from from from from from
from from"""

txt = "Hello {word}"
print(txt.format(word = 'World!'))

message1 = 'Hi, My name is {} and I am {} years old.'
print(message1.format('Bob',36))


