def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    
    sorted_chars = sort_chars(num_characters)
    #print(sorted_chars)
    create_report(book_path, num_words, sorted_chars)


def create_report(book_path, num_words, list_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for i in range(len(list_chars)):
        print(f"The '{list_chars[i]['character']}' character was found {list_chars[i]['count']} times")


def get_num_words(text):
    words = text.split()
    return(len(words))

def get_num_characters(text):
    characters = text.split()
    lowered_text = text.lower()
    character_count = {}
    for i in lowered_text:
        if not i.isalpha():
            continue
        if i not in character_count:
            character_count[i] = 1
        else:
            character_count[i] += 1
    return character_count

def sort_on(dict):
    return dict["count"]

def sort_chars(chars):
    character_list = []
    for key in chars:
        temp_dict = {"character": key, "count": chars[key]}
        character_list.append(temp_dict)
    
    character_list.sort(reverse=True, key=sort_on)
    return character_list
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()