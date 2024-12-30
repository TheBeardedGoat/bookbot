with open("books/frankenstein.txt") as f:
    file_contents = f.read()
book_words = file_contents.split()
book_string_lower = file_contents.lower()
characture_list = list(book_string_lower)
#no_dups = set(book_string_lower)

def update_dect(dict):
    final_dir = {}
    for c in dict:
        if c in final_dir:
            final_dir[c] += 1
        else:
            final_dir[c] = 1
    return (final_dir)


def word_count(words):
    total_count = 0
    for w in words:
        total_count += 1
    return (total_count)

def report_builder(count,data):
    #print (data)
    print ("--- Begin report of books/frankenstein.txt ---")
    print (F"{count} words found in the document")
    for key in data:
        if key .isalpha():
            print (f"The {key} character was found {data[key]} times")
        

word_counts = (word_count(book_words))
update_decs = (update_dect(book_string_lower))
report_builder(word_counts,update_decs)

