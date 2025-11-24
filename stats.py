def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    countOfChars = {}
    for i in range(0, len(text)):
        item = text[i]
        if item.lower() in countOfChars.keys():
            countOfChars[item.lower()] += 1
        else:
            countOfChars[item.lower()] = 1
    return countOfChars

def sorted_count_char(countOfChars):
    unsorted = []
    for k,v in countOfChars.items():
        if k.isalpha():
            unsorted.append({
            "char": k,
            "num": v
        })
        else:
            continue
            
    unsorted.sort(key= lambda item: item["num"], reverse=True) #(key="num", reverse=True)
    return unsorted