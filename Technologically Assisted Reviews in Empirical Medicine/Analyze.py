df = []
df1 = []
def sbt():
    import pandas as pd

    df = pd.read_csv("CSV\\TitleScore.csv")
    df = df.set_index("topicid")
    df = df.ix[['CD010438', 'CD010771', 'CD011134']]
    print(df)
    # df = df.sort_index(by=['recall_title_abstract'], ascending=[False])
    import numpy as np
    import matplotlib.pyplot as plt

    # data to plot
    n_groups = 3
    recall_title = df["recall_title"]
    recall_abstract = df["recall_abstract"]
    recall_title_abstract = df["recall_title_abstract"]

    recall_title = recall_title[:3]
    recall_abstract = recall_abstract[:3]
    recall_title_abstract = recall_title_abstract[:3]

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.20
    opacity = 0.8

    rects1 = plt.bar(index, recall_title, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Title Recall')

    rects2 = plt.bar(index + bar_width, recall_abstract, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Abstract Recall')

    rects3 = plt.bar(index + 2 * bar_width, recall_title_abstract, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Title-Abstract Recall')

    plt.xlabel('Topic ID')
    plt.ylabel('Recall')
    plt.title('Search by Title')
    plt.xticks((index + bar_width), ['CD010438', 'CD010771', 'CD011134'])
    plt.legend()

    plt.tight_layout()

    plt.show()

def sbq():
    import pandas as pd

    df = pd.read_csv("CSV\\QueryScore.csv")
    df = df.set_index("topicid")
    df = df.ix[['CD010438','CD010771','CD011134']]
    print(df)
    # df = df.sort_index(by=['recall_title_abstract'], ascending=[False])
    import numpy as np
    import matplotlib.pyplot as plt

    # data to plot
    n_groups = 3
    recall_title = df["recall_title"]
    recall_abstract = df["recall_abstract"]
    recall_title_abstract = df["recall_title_abstract"]

    recall_title = recall_title[:3]
    recall_abstract = recall_abstract[:3]
    recall_title_abstract = recall_title_abstract[:3]

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.20
    opacity = 0.8

    rects1 = plt.bar(index, recall_title, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Title Recall')

    rects2 = plt.bar(index + bar_width, recall_abstract, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Abstract Recall')

    rects3 = plt.bar(index + 2 * bar_width, recall_title_abstract, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Title-Abstract Recall')

    plt.xlabel('Topic ID')
    plt.ylabel('Recall')
    plt.title('Search by Query')
    plt.xticks((index + bar_width),['CD010438','CD010771','CD011134'])
    plt.legend()

    plt.tight_layout()

    plt.show()

def recall():
    import numpy as np
    import matplotlib.pyplot as plt

    import pandas as pd

    df = pd.read_csv("CSV\\TitleScore.csv")
    df = df.set_index("topicid")
    df = df.ix[['CD010438', 'CD010771', 'CD011134']]


    df1 = pd.read_csv("CSV\\QueryScore.csv")
    df1 = df1.set_index("topicid")
    df1 = df1.ix[['CD010438', 'CD010771', 'CD011134']]
    # data to plot
    n_groups = 3
    recall_title_abstract = df["recall_title_abstract"]
    recall_title_abstract1 = df1["recall_title_abstract"]

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.20
    opacity = 0.8

    rects1 = plt.bar(index, recall_title_abstract, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Recall-Search by Title')

    rects2 = plt.bar(index + bar_width, recall_title_abstract1, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Recall- Search by Query')


    plt.xlabel('Topic ID')
    plt.ylabel('Recall')
    plt.xticks((index + bar_width/2), ['CD010438', 'CD010771', 'CD011134'])
    plt.legend()

    plt.tight_layout()

    plt.show()

sbt()
sbq()
recall()