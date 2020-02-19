from whoosh.index import create_in
from whoosh.fields import *
def whoosh():
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    ix = create_in("indexdir", schema)
    writer = ix.writer()
    writer.add_document(title=u"First document", path=u"/a",
                        content=u"This is the first document we've added!")
    writer.add_document(title=u"Second document", path=u"/b",
                        content=u"The second one is even more interesting!")
    writer.commit()
    from whoosh.qparser import QueryParser
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse("first")
        results = searcher.search(query)
        results[0]


import nltk

def nltk_search():
    file = open('NLTK.txt', 'r')
    read_file = file.read()
    text = nltk.Text(nltk.word_tokenize(read_file))
    match = text.concordance('of')
    print(match)

nltk_search()