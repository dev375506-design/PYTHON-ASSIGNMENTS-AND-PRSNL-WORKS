def rem(l,words):
    k=[]
    for item in l:
        if not(item==words):
            k.append(item.strip(words))
    return k
    

l=["soham","dev","harsh","ram","shyam"]
print(rem(l,"am"))