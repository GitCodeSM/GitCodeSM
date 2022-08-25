'''
* A program in python to read the 3 pages and create an index of words giving the list of pages on which each word is present.
* There are 3 files Page1.txt, Page2.txt and Page3.txt containing some text. The file exclude-words.txt contains common words like 'and'
* which should not be indexed.
* Unique words collected from all three pages sorted in new_index.txt alphabetically A - Z.
''' 

# importing created module: page_words_module and its two classes
from pages_words_module import Pages, Words_dict

# opening .txt pages 1, 2, 3 and exclude-words
new_page1 = open("Page1.txt", "r")

new_page2 = open("Page2.txt", "r")

new_page3 = open("Page3.txt", "r")

page_exclude_words = open('exclude-words.txt','r')

# calling class Pages()
mytopic = Pages('IT services')
print(mytopic)

# operation on .txt files to generate 3 lists of words with page numbers using various methods in class Pages()
page1_words = mytopic.page_type1(new_page1)

page_exclude_words = open('exclude-words.txt','r')

page1words = mytopic.remove_words(page1_words, page_exclude_words)

page2_words = mytopic.page_type2(new_page2)

page2words = mytopic.remove_words(page2_words, page_exclude_words)

page3_words = mytopic.page_type3(new_page3)

page3words = mytopic.remove_words(page3_words, page_exclude_words)

# calling class Words_dict() for getting a merged dictionary of total words
mydicts = Words_dict()

the_words_index = mydicts.dict_TotalWords(page1words, page2words, page3words)

# method sort_dict() sorts the dictionary alphabetically and returns a list
sorted_word_index = mydicts.sort_dict(the_words_index)

# create and write a .txt file new_index.txt with printed words with page numbers by side, line by line
newfile = open('new_index.txt', 'w')
for element in sorted_word_index:
    newfile.write(element + '\n')
newfile.close()

'''
End of the program.
'''
