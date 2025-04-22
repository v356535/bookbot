def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    characters = {}
    
    for letter in text:
        if letter.isalpha() != True:
            continue
        lowercase_letter = letter.lower()
        if lowercase_letter in characters:
            characters[lowercase_letter] += 1
        else:
            characters[lowercase_letter] = 1
    #print(characters)
    
    return characters


    
    

def sorted_numbers(characters):
    sorted_list = [{"char": key, "count": value} for key, value in characters.items()]
    
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    for item in sorted_list:
        print(f'{item["char"]}: {item["count"]}')
    
    
    