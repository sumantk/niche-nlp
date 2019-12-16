import os, os.path
import shutil
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser

# Create Schema
#schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True))

# Create index directory
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
else:
    shutil.rmtree("indexdir")
    os.mkdir("indexdir")

# Create Index
ix = create_in("indexdir", schema)

writer = ix.writer() # create writer

#add documents to index
writer.add_document(title=u"First document", path=u"/a", content=u"This is the first document we've added!")
writer.add_document(title=u"Second document", path=u"/b", content=u"The second one is even more interesting!")
writer.commit()

with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("second")
    results = searcher.search(query)
    print(results[0])