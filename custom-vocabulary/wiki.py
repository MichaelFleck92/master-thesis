import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(
        language='de',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

p_wiki = wiki_wiki.page("")
print(p_wiki.text)

open('ns-korpus.txt', 'a').write(p_wiki.text)