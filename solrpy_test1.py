# coding:utf-8
import solr
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

# create a connection to a solr server
conn = solr.Solr('http://localhost:8080/solr', timeout=1000)

# add a document to the index
tdoc = {"id": 3, "title": "Lucene in Action"}

for k in tdoc:
    print "dict[%s] =" % k, tdoc[k]

conn.add(tdoc)
conn.commit()

# do a search
response = conn.select('Lucene')
for hit in response.results:

    print hit
