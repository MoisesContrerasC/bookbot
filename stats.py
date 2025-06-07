def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()    
        return file_contents

def get_word_count(text):
    words = text.split() 
    counter = 0
    for w in words:
        counter+=1
    return counter

def get_character_count(text):
    charater_dict = {}
    formated_text = text.lower()
    for i in list(formated_text):
        if i not in charater_dict:
            charater_dict[i] = 1
        else:
            charater_dict[i] += 1
    return charater_dict

def sort_on(character_count):
    return character_count["count"]

def get_sorted_list(character_count):
    sorted_list = []
    for k,v in character_count.items():
        temp_dict = {}
        temp_dict["char"] = k
        temp_dict["count"] = v
        sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True , key=sort_on)
    return sorted_list

def get_print_format(file_path, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        char, count = i["char"], i["count"]
        if char.isalpha():
            print(f"{char}: {count}")
        else: 
            pass
    print("============= END ===============")
