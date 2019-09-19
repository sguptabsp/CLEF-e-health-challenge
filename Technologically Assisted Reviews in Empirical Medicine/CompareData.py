from os import listdir
import re
beta = 10

def score(filename):
    import pandas as pd
    df = pd.read_csv("CSV\\DataCompare1\\"+str(filename)+".csv")
    df1 = pd.read_csv("CSV\\DataforCompare01\\"+str(filename)+".csv")

    df_title = pd.read_csv("CSV\\TitleScore\\"+str(filename)+".csv")
    df_abstract = pd.read_csv("CSV\\AbstractScore\\"+str(filename)+".csv")
    df_title_abstract = pd.read_csv("CSV\\TitleAbstractScore\\"+str(filename)+".csv")

    t = len(df_title)
    a = len(df_abstract)
    ta = len(df_title_abstract)

    # df_title = df_title[:len(df)]
    # df_abstarct = df_abstract[:len(df)]
    # df_title_abstract = df_title_abstract[:len(df)]

    # Title
    test_t = df["pid"]
    train_t = df_title["pid"]

    relevent_pid = []

    for i in test_t:
        for j in train_t:
            if (i == j):
                relevent_pid.append(i)

    recall_title = len(relevent_pid) / len(test_t)
    precision_title = (len(relevent_pid)) / len(train_t)
    F1_title = (2*recall_title*precision_title)/(recall_title+precision_title)
    F1_beta_title = (1+ beta*beta) * ((recall_title*precision_title)/(recall_title+(beta*beta*precision_title)))

    # Abstract
    test_a = df["pid"]
    train_a = df_abstract["pid"]

    relevent_pid = []

    for i in test_a:
        for j in train_a:
            if (i == j):
                relevent_pid.append(i)

    recall_abstract = len(relevent_pid) / len(test_t)
    precision_abstract = (len(relevent_pid)) / len(train_t)
    F1_abstract = (2 * recall_abstract * precision_abstract) / (recall_abstract + precision_abstract)
    F1_beta_abstract = (1 + beta * beta) * (
    (recall_abstract * precision_abstract) / (recall_abstract + (beta * beta * precision_abstract)))

    # Title-Abstract
    test_ta = df["pid"]
    train_ta = df_title_abstract["pid"]

    relevent_pid = []

    for i in test_ta:
        for j in train_ta:
            if (i == j):
                relevent_pid.append(i)

    recall_title_abstract = len(relevent_pid) / len(test_t)
    precision_title_abstract = (len(relevent_pid)) / len(train_t)
    F1_title_abstract = (2 * recall_title_abstract * precision_title_abstract) / (recall_title_abstract + precision_title_abstract)
    F1_beta_title_abstract = (1 + beta * beta) * (
        (recall_title_abstract * precision_title_abstract) / (recall_title_abstract + (beta * beta * precision_title_abstract)))

    writer.writerow({'topicid':str(filename),
                     'recall_title':str(recall_title),
                     'precision_title':str(precision_title),
                     'F1_title':str(F1_title),
                     'F1_beta_title':str(F1_beta_title),
                     'recall_abstract':str(recall_abstract),
                     'precision_abstract':str(precision_abstract),
                     'F1_abstract':str(F1_abstract),
                     'F1_beta_abstract': str(F1_beta_abstract),
                     'recall_title_abstract':str(recall_title_abstract),
                     'precision_title_abstract':str(precision_title_abstract),
                     'F1_title_abstract': str(F1_title_abstract),
                     'F1_beta_title_abstract': str(F1_beta_title_abstract),})

import csv
with open("CSV\\TitleScore.csv", 'w') as csvfile:
    fieldnames = ['topicid','recall_title', 'precision_title', 'F1_title', 'F1_beta_title' ,'recall_abstract', 'precision_abstract',
                  'F1_abstract', 'F1_beta_abstract','recall_title_abstract', 'precision_title_abstract','F1_title_abstract'
        , 'F1_beta_title_abstract'
                  ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    mypath = 'E:\\IIT\\Lecture\\CS522 ADM\\Project\\Data\\topics_train\\'

    for f in listdir(mypath):
        with open(mypath + f, 'r') as myfile:
            data = myfile.read().replace('\n', '')
            data = re.split('\W+', data)
            topic = data[data.index('Topic') + 1:data.index('Title')]
            score(topic[0])
