# Problem 1
# create a class with name StringClass which should take string
# as an input from constructor. It should have method which
# should return the length of the string and a method to convert
# string to list of characters. This method will take an
# argument as string to convert.

class StringClass:

    def __init__(self, inputString):
        self.string = inputString

    def lengthOfString(self):
        return len(self.string)

    def str2listConverter(self, inputStr):
        return [char for char in inputStr]

stringClass = StringClass("hello")
print("length of the string :- ", stringClass.lengthOfString())
print("String converted to list : - ", stringClass.str2listConverter("neeraj"))
