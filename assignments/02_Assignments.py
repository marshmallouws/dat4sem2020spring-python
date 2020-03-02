""" --------------------------- 02-0a Loops ---------------------------
1)  Write a program that creates gramatically valid English sentences.
        Here, we consider a sentence to be gramatically correct when 
        it follows the simple English grammar of the form: Article 
        Adjective Noun Verb. That is, even the sentence A insect fly. 
        is, for the moment, considered correct.
        
        Create additionally to the exercise above, a list of definite 
        and indefinite articles and verbs from an online resource. 
2)  Extend the above program to generate all possible sentences with the given words.
"""
adjectives = ['arctic','ajar','angelic','diabolic','massive']
articles = ['a', 'an']
nouns = ['dog','house', 'Peter', 'Annika', 'horse']
verbs = ['run', 'hide', 'suck', 'cry']

# words = adjectives + articles + noun + verbs

sentences = [[article, adjective, noun, verb] for article in articles 
                                      for adjective in adjectives 
                                      for noun in nouns
                                      for verb in verbs]
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')

vocals = ('a', 'e', 'i', 'o', 'u', 'y')

# With loops
sentences1 = []
for article in articles:
    for adjective in adjectives:
        for noun in nouns:
            for verb in verbs:
                if article == 'a' and adjective.startswith(vocals):
                    break
                elif article == 'an' and adjective.startswith(consonants):
                    break
                sentences1.append([article, adjective, noun, verb])

for sentence in sentences1:
    print(' '.join(sentence))

"""
--------------------------- 02-0b Functions and Modules ---------------------------
"""

"""
--------------------------- 02-1 CLI Programs ---------------------------
SEE Download_script.py!!!!!!!!!!!!!!!!!!!!!!!!

Write a program download_script.py, which downloads a set of files from the internet. The files to download are given as arguments to your program on the command-line as illustrated in the following:

$ python download_script.py http://www.gutenberg.org/files/2701/2701-0.txt http://www.gutenberg.org/cache/epub/27525/pg27525.txt
Downloading file to ./2701-0.txt
Downloading file to ./pg27525.txt
Reuse your webget module from exercises in 07-Functions and Modules.

Modify the above program, so that it can download a list of files from stdin. That is, so that you can reuse the output of one CLI command as input to your program.

$ cat list_of_files.txt | python download_script.py
"""


"""
--------------------------- 02-2 CLI Programs ---------------------------
Write a program that converts the Excel spreadsheet ./iris_data.xlsx into a CSV file with the same data. Start with writing a unit test against which you implement your solution (see below).
Write a program, which converts befkbhalderstatkode.csv from a CSV file into a Python module kkdata.py containing a dictionary named STATISTICS.
"""
import openpyxl
import csv
import platform

filename = './iris_data.xlsx'
wb = openpyxl.load_workbook(filename)

if platform.system() == 'Windows':
    newline=''
else:
    newline=None

#sheet = wb.get_sheet_by_name("Fisher's Iris Data")
sheets = wb.get_sheet_names()
print(sheets)

with open('test.csv', 'w', newline=newline) as output_file:
    output_writer = csv.writer(output_file)
    for s in sheets:
        sheet = wb.get_sheet_by_name(s)
        for rowOfCellObjects in sheet:
            tmp = []
            for cellObj in rowOfCellObjects:
                tmp.append(cellObj.value)
            output_writer.writerow(tmp)


"""
--------------------------- 02-3 Object Oriented Programming ---------------------------
 Create a Python module, which consists of a class TextContainer. 
 The class shall implement methods for computing statistics on texts.
 Counting the amount of words used in a text.
 Counting the amount of chars used in a text.
 Counting the amount of letters, where letters are all ASCII characters
"""
import string

class TextContainer:
    pass

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'TextContainer({self.text!r})'

    # toString
    def __str__(self):
        return f'{self.text}'

    def count_words(self):
        tmp = self.text.split(" ")
        return len(tmp)

    def count_letters(self):
        i = 0
        for char in self.text:
            if char in string.ascii_letters:
                i += 1
        return i

    def count_chars(self):
        i =  0
        for char in self.text:
            if char in string.punctuation:
                i += 1
        return i

t = TextContainer("hej med dig.")


""" --------------------------- 02-04 Exceptions ---------------------------
1)  Create a class called: Person with a constructor that takes a string: name.
2)  Check if name contains only letters and each new word starts with a capital 
    letter. If this is not the case raise an InvalidArgumentException (your own 
    exception here)
3)  Test you new class by making 2 instances (one with a name, that follows the 
    rules and another that violates them)
"""

class InvalidArgumentException(ValueError):

    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)

class Person:
    
    def __init__(self, name):
        self.name = self.check_name(name)
    
    def check_name(self, name):
        names = name.split(" ")
        for n in names:
            if not n.istitle():
                raise InvalidArgumentException('Name is not titled')
            
            for char in n:
                if not char in string.ascii_letters:
                    raise InvalidArgumentException(f'{char} is not valid')
        return name

#p1 = Person("Some2")
p2 = Person("Annika Ehlers")
#p3 = Person("Annika ahlers")