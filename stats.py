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