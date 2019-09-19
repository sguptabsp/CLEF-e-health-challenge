# from pyelasticsearch import ElasticSearch
from pubmed_lookup import PubMedLookup
from pubmed_lookup import Publication
from Bio import Entrez
import csv

#Create server for storing Data
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
count = 0

#Function for fetch details using pid
def fetch_details(pid):
    email = ''
    url = 'http://www.ncbi.nlm.nih.gov/pubmed/' + str(pid)
    lookup = PubMedLookup(url, email)

    publication = Publication(lookup)
    return publication

# funtion to load data to ES server
def Load_to_ES(pid, topicid):
    print(len(pid))
    for i in pid:

        try:
            publication = fetch_details(i)
            doc = {
                'title': publication.title,
                'authors': publication.authors,
                'abstract': repr(publication.abstract)
            }
            res = es.index(index="pubmed-data", doc_type= str(topicid), id=i, body=doc)
            print(res['created'])
            print('n is ' + str(i))
            # res = es.get(index="pubmed-data", doc_type=str(topicid), id=i)
            pid.remove(i)
            #print(res['_source'])

            #es.indices.refresh(index="pubmed-data")
        except Exception:
            print("error in ES")
            # Load_to_ES(pid,topicid)
            continue

    if len(pid) !=0 :
        print("Again load call")
        Load_to_ES(pid, topicid)

#function for search
def search(query, topicid):
    # res = es.search(index="pubmed-data", doc_type=str(topicid), body={"query": {"match_all": {}}})
    # res = es.search(index="pubmed-data", doc_type=str(topicid), body={"query": {"query_string": {"query": query}},"size":10000})

    res = es.search(index="pubmed-data", doc_type=str(topicid), body={"query": {"multi_match": {"query": query,
                                                                                                "type": "most_fields",
                                                                                                "fields": ["title","abstract"],
                                                                                                # "minimum_should_match": "20%",
                                                                                                "operator": "or"
                                                                                                }},"size":10000,})

#     res = es.search(index="pubmed-data", doc_type=str(topicid), body={
#     "query": {
#         "dis_max": {
#             "queries": [
#                 {"match": {"title": query}},
#                 {"match": {"abstract": query}}
#             ],
#             "tie_breaker": 0.3
#         }
#     }
# })

#     res = es.search(index="pubmed-data", doc_type=str(topicid), body={
#   "query": {
#     "bool": {
#       "must": {
#         "match": {
#           "abstract": {
#             "query": query,
#             "minimum_should_match": "10%"
#           }
#         }
#       },
#       "should": {
#         "match_phrase": {
#           "abstract": {
#             "query": query,
#             "slop":  1
#           }
#         }
#       }
#     }
#   }
# })

    # res = es.search(index="pubmed-data", doc_type=str(topicid), body= )
#     res = es.search(index="pubmed-data", doc_type=str(topicid), body={
#     "query": {
#         "match": {
#             "abstract": {
#                 "query":                query,
#                 "minimum_should_match": "50%"
#             }
#         }
#     },
#     "rescore": {
#         "window_size": 50,
#         "query": {
#             "rescore_query": {
#                 "match_phrase": {
#                     "abstract": {
#                         "query": query,
#                         "slop":  50
#                     }
#                 }
#             }
#         }
#     }
# })
    print("Got %d Hits:" % res['hits']['total'])
    # print("pid\t\t\t"+"score")
    # for hit in res['hits']['hits']:
    #     # print("%(title)s %(authors)s: %(abstract)s" % hit["_source"])
    #     print(str(hit["_id"]) + "\t" +  str(hit["_score"]))
    #     #print(hit["_id"])
    filename = str(topicid)+".csv"
    with open("CSV\\QueryTitleAbstractScore\\"+filename, 'w') as csvfile:
        fieldnames = ['pid', 'score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for hit in res['hits']['hits']:
            writer.writerow({'pid': str(hit["_id"]), 'score': str(hit["_score"]) })


def searchAbstract(query, topicid):
    res = es.search(index="pubmed-data", doc_type=str(topicid), body={"query": {"multi_match": {"query": query,
                                                                                                "type": "most_fields",
                                                                                                "fields": ["abstract"],
                                                                                                # "minimum_should_match": "20%",
                                                                                                "operator": "or"
                                                                                                }}, "size": 10000})

    print("Got %d Hits:" % res['hits']['total'])
    filename = str(topicid) + ".csv"
    with open("CSV\\QueryAbstractScore\\" + filename, 'w') as csvfile:
        fieldnames = ['pid', 'score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for hit in res['hits']['hits']:
            writer.writerow({'pid': str(hit["_id"]), 'score': str(hit["_score"])})


def searchTitle(query, topicid):
    res = es.search(index="pubmed-data", doc_type=str(topicid), body={"query": {"multi_match": {"query": query,
                                                                                                "type": "most_fields",
                                                                                                "fields": ["title"],
                                                                                                # "minimum_should_match": "20%",
                                                                                                "operator": "or"
                                                                                                }}, "size": 10000})

    print("Got %d Hits:" % res['hits']['total'])
    filename = str(topicid) + ".csv"
    with open("CSV\\QueryTitleScore\\" + filename, 'w') as csvfile:
        fieldnames = ['pid', 'score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for hit in res['hits']['hits']:
            writer.writerow({'pid': str(hit["_id"]), 'score': str(hit["_score"])})


def get_pid(topicid):
    p=[]
    res = es.search(index="pubmed-data", doc_type=str(topicid), body={"query": {"match_all": {}},"size":10000})
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        # print("%(title)s %(authors)s: %(abstract)s" % hit["_source"])
        # print(str(hit["_id"]) + "\t" +  str(hit["_score"]))
        #print(hit["_id"])
        p.append(str(hit["_id"]))
    return p
