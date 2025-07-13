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

    
