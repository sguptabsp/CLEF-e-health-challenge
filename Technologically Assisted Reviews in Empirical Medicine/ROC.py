from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import random
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn import metrics

df = pd.read_csv("CSV\\TitleScore.csv")
df_title = pd.read_csv("CSV\\TitleScoreSortByTitle.csv")
df_abstract = pd.read_csv("CSV\\TitleScoreSortByAbstract.csv")

df1 = pd.read_csv("CSV\\QueryScore.csv")
df_title1 = pd.read_csv("CSV\\QueryScoreSortByTitle.csv")
df_abstract1 = pd.read_csv("CSV\\QueryScoreSortByAbstract.csv")

recall_title_abstract = pd.DataFrame(df.recall_title_abstract)
precision_title_abstract = pd.DataFrame(df.precision_title_abstract)
recall_title = pd.DataFrame(df_title.recall_title)
precision_title = pd.DataFrame(df_title.precision_title)
recall_abstract = pd.DataFrame(df_abstract.recall_abstract)
precision_abstract = pd.DataFrame(df_abstract.precision_abstract)

F1_beta_title = pd.DataFrame(df.F1_beta_title).mean()
F1_beta_abstract = pd.DataFrame(df.F1_beta_abstract).mean()
F1_beta_title_abstract = pd.DataFrame(df.F1_beta_title_abstract).mean()

recall_title_abstract1 = pd.DataFrame(df1.recall_title_abstract)
precision_title_abstract1 = pd.DataFrame(df1.precision_title_abstract)
recall_title1 = pd.DataFrame(df_title1.recall_title)
precision_title1 = pd.DataFrame(df_title1.precision_title)
recall_abstract1 = pd.DataFrame(df_abstract1.recall_abstract)
precision_abstract1 = pd.DataFrame(df_abstract1.precision_abstract)

def scat():
    import numpy as np
    x = [0.735576, 0.762753, 0.814575]
    y = [0.070829, 0.072664, 0.07809]

    # x=[0.756195, 0.766079, 0.816499]
    # y=[0.057806, 0.059772, 0.063846]
    z = np.arange(3)
    colors = ["Text", "Abstract", "Full Text"]
    c = ["ro", "yo", "bo"]
    plt.xlabel('recall')
    plt.ylabel('precision')
    plt.title('Search by TITLE')
    for i in z:
        plt.plot(x[i], y[i], c[i], label=colors[i], marker='^')
    plt.legend()


    plt.show()

def rp_plot():
    # print(precision)
    import matplotlib.pyplot as plt
    import numpy as np
    #
    # plt.scatter([precision_title, precision_abstract, precision_title_abstract],
    #             [recall_title, recall_abstract, recall_title_abstract]
    #             )
    # rec = pd.DataFrame(precision, columns = ["Imp"], index = recall).sort_values(['Imp'], ascending = False)
    # print(rec)
    # print(rec)

    plt.xlabel('precision')
    plt.ylabel('recall')
    fig, ax = plt.subplots()
    ax.scatter([precision_title, precision_abstract, precision_title_abstract],
                [recall_title, recall_abstract, recall_title_abstract])

    plt.savefig("test.png")
    plt.show()

def auc():
    import numpy as np
    a = np.trapz([recall_title, recall_abstract, recall_title_abstract],
             x = [precision_title, precision_abstract, precision_title_abstract])

    print(a)

def map():
    map_ft = metrics.auc(recall_title_abstract, precision_title_abstract)
    print("Full Text search by tile",map_ft)
    map_a = metrics.auc(recall_abstract, precision_abstract)
    print("Abstract search by title",map_a)
    map_t = metrics.auc(recall_title, precision_title)
    print("Title search by title",map_t)

    map_ft1 = metrics.auc(recall_title_abstract1, precision_title_abstract1)
    print("Full text search by query",map_ft1)
    map_a1 = metrics.auc(recall_abstract1, precision_abstract1)
    print("Abstract search by query",map_a1)
    map_t1 = metrics.auc(recall_title1, precision_title1)
    print("Title search by query",map_t1)

scat()

# print(recall_title1)
# print(recall_abstract1)
# print(recall_title_abstract1)
#
# print(precision_title1)
# print(precision_abstract1)
# print(precision_title_abstract1)

# print("F1 beta title", F1_beta_title)
# print("F1 beta abstract", F1_beta_abstract)
# print("F1 beta Full Text", F1_beta_title_abstract)