def get_num_of_words(text_content):
    return len(text_content.split())

def get_character_count(text_content):
    character_counter = {}
    for c in text_content:
        lower_character = c.lower()
        if lower_character  not in character_counter:
            character_counter[lower_character] = 1
        else:
            character_counter[lower_character] += 1
    return character_counter


def sort_on(items):
    return items["num"]

def get_sorted_character(character_counter) -> list:
    character_list= [] 
    for key in character_counter:
        if key.isalpha():
            character_list.append({"char": key, "num" :character_counter[key]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list
    
