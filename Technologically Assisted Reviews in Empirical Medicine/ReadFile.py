import re
import ElasticSerarch
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from os import listdir


topic_list = []
title_list = []
query_list = []
pids_list = []

#Function for Read data from text file
def Read_Data():
    mypath = 'E:\\IIT\Lecture\\CS522 ADM\\Project\\Data\\run33\\'
    for f in listdir(mypath):
        with open(mypath+f, 'r') as myfile:
            data = myfile.read().replace('\n', '')
            #Tokenization remove any non-alphanumric character like puntuation
            data = re.split('\W+', data )
            #Normalization remove stopwords
            data = [word for word in data if word not in stopwords.words('english')]
            topic = data[data.index('Topic') + 1:data.index('Title')]
            title = data[data.index('Title') + 1:data.index('Query')]
            query = data[data.index('Query') + 1:data.index('Pids')]
            pids = data[data.index('Pids') + 1:]
            print(topic)

            topic_list.append(topic)
            title_list.append(title)
            query_list.append(query)
            pids_list.append(pids)


def main():

    try:
        Read_Data()
        a = list(set(pids_list[0]))
        b = ElasticSerarch.get_pid(topic_list[0][0])
        pid = [x for x in a if x not in b]
        print("a",len(a))
        print("b",len(b))
        print("pid",len(pid))
        ElasticSerarch.Load_to_ES(pid, topic_list[0][0])
        print("Done")
        query = ''
        print(query_list[0])
        for i in query_list[0]:
            query = query+' '+ i
        print(query)
        ElasticSerarch.search(query, topic_list[0][0])
    except Exception:
        print("error")
        pass

if __name__ == "__main__":
    main()



