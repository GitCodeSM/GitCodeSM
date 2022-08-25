'''
creating class Pages()
'''
class Pages():

    def __init__(self, topic):
        self.topic = topic

    def __str__(self):
        return f'Analysing 3 book pages at a time on {self.topic}...'
    
    '''
    Method for extracting unique words from page1
    '''
    def page_type1(self, page1):
        # Creates a list of unique words for page type 1
        lines = 1
        page1_word_list = []
        while lines in range(1,39):
            p = page1.readline().lower().strip()
            p_list = p.split()
            for x in p_list:
                alphanums = ''.join([c for c in x if c.isalnum()])
                page1_word_list.append(alphanums)
            lines += 1

        for empty_space in page1_word_list:
            i = page1_word_list.index(empty_space)
            if empty_space == '' or empty_space.isdigit():
                page1_word_list.pop(i)
            else:
                continue
        page1_words = list(set(page1_word_list))
        page1_words.remove('â')
        return page1_words
    
    '''
    Method for extracting unique words from page2
    '''
    def page_type2(self, new_page2):
        # Creates a list of unique words for page type 2
        lines = 1
        page2_word_list = []
        while lines in range(1,28):
            p = new_page2.readline().lower().strip()
            p_list = p.split()
            for x in p_list:
                alphanums = ''.join([c for c in x if c.isalnum()])
                page2_word_list.append(alphanums)
            lines += 1

        for empty_space in page2_word_list:
            i = page2_word_list.index(empty_space)
            if empty_space == '' or empty_space.isdigit():
                page2_word_list.pop(i)
            else:
                continue

        page2_words = list(set(page2_word_list))
        return page2_words

    '''
    Method for extracting unique words from page3
    '''
    def page_type3(self, new_page3):
        # Creates a list of unique words for page type 3
        lines = 1
        page3_word_list = []
        while lines in range(1,39):
            p = new_page3.readline().lower().strip()
            p_list = p.split()
            for x in p_list:
                alphanums = ''.join([c for c in x if c.isalnum()])
                page3_word_list.append(alphanums)
            lines += 1

        for empty_space in page3_word_list:
            i = page3_word_list.index(empty_space)
            if empty_space == '' or empty_space.isdigit():
                page3_word_list.pop(i)
            else:
                continue
        page3_words = list(set(page3_word_list))
        return page3_words
    
    '''
    Method for removing unique words from given pages words lists
    '''
    def remove_words(self, page_words, page_exclude_words):
        # Creates a list from page_words list exluding words from a given exclude words list
        lines = 1
        exclude_word_list = []
        while lines in range(1,11):
            p = page_exclude_words.readline().lower().strip()
            exclude_word_list.append(p)
            lines += 1
        
        for word in exclude_word_list:
            if word in page_words:
                page_words.remove(word)
        return page_words

'''
creating class Words_dict() to create words dictionary with page number for each word
'''
class Words_dict():

    def __init__(self):
        print('Words dictionary from three pages of a topic/book.')
    
    '''
    Method for creating a dictionary object for total unique words from all pages with list of page numbers for each word
    '''
    def dict_TotalWords(self, final_page1_words, final_page2_words, final_page3_words):
        # Creates a separate dictionary for all 3 pages and merges into a new dictionary to return
        dict1 = {}
        for x in final_page1_words:
            for y in final_page2_words:
                for z in final_page3_words:
                    if x == y == z:
                        dict1.update({x:[1,2,3]})

        dict2 = {}
        for x in final_page1_words:
            for y in final_page2_words:
                if x == y not in final_page3_words:
                    dict2.update({x:[1,2]})

        dict3 = {}
        for x in final_page1_words:
            for z in final_page3_words:
                if x == z not in final_page2_words:
                    dict3.update({x:[1,3]})
        
        dict4 = {}
        for x in final_page1_words:
            if x not in final_page2_words:
                if x not in final_page3_words:
                    dict4.update({x:[1]})

        dict5 = {}
        for y in final_page2_words:
            if y not in final_page1_words:
                if y not in final_page3_words:
                    dict5.update({y:[1]})

        dict6 = {}
        for z in final_page3_words:
            if z not in final_page1_words:
                if z not in final_page2_words:
                    dict6.update({z:[1]})

        index_words = {}
        index_words.update(dict1)
        index_words.update(dict2)
        index_words.update(dict3)
        index_words.update(dict4)
        index_words.update(dict5)
        index_words.update(dict6)
        return index_words
    
    '''
    Method for sorting the total words dictionary into an alphabetically sorted list
    '''
    def sort_dict(self, index_words):
        # Creates a sorted dictionary (sorted by keys in alphabetical order) and returns a list of sorted dictionary elements
        sorted_index = sorted(index_words.items())
        sorted_index_list = []
        for k,v in sorted_index:
            c = ''
            for n in v:
                c = c + str(n) +','
            sorted_index_list.append(f'{k}:{c}')
        return sorted_index_list
