def wordcount(book_text):
    wc = 0                                                                                                                           
    split_text = book_text.split()                                                                                                                                                       
    for word in split_text:                                                                                                                                                              
        wc += 1                                                                                                                                                                          
    return(wc)

def charstats(book_text):
    cs = {}
    lowered = book_text.lower()
    return(lowered)

    
