def wordcount(book_text):
    wc = 0                                                                                                                           
    split_text = book_text.split()                                                                                                                                                       
    for word in split_text:                                                                                                                                                              
        wc += 1                                                                                                                                                                          
    return(wc)

def charstats(book_text):
    cs = {}
    for c in book_text:
        lowered = c.lower()
        if lowered in cs:
            cs[lowered] += 1
        else:
            cs[lowered] = 1
    return(cs)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

