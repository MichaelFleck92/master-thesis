from itertools import chain

def unique_words(lines):
    return set(chain(*(line.split() for line in lines if line)))

with open("korpus.txt", 'r') as f:
    korpus = unique_words(f)
    print(unique_words(f))

with open("ns-korpus.txt", 'r') as f:
    ns_korpus = unique_words(f)
    print(unique_words(f))

print(len(korpus))
print(len(ns_korpus))


for word in ns_korpus:
    if word[-1] == "-":
        word = word[:-1]
    if word not in korpus:
        #print(word)
        open('ns-vokabular.txt', 'a').write("\n"+word)