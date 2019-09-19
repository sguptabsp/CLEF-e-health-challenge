def sbt():
    import pandas as pd

    df = pd.read_csv("CSV\\TitleScore.csv")
    df = df.set_index("topicid")
    df = df.ix[['CD010438', 'CD010771', 'CD011134']]
    print(df)
    # df = df.sort_index(by=['recall_title_abstract'], ascending=[False])
    import numpy as np
    import matplotlib.pyplot as plt

    # recall = [0.756195, 0.766079, 0.816499]
    # precision = [0.057806, 0.059772, 0.063846]
    # map=[0.027168151869,0.0221538432889, 0.1]

    recall=[0.756195,0.057806,0.0274533542137,0.596124]
    precision=[0.766079,0.059772,0.0168225938493,0.607194]
    map=[0.816499,0.063846,0.0211316566653,0.649437]

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(4)
    bar_width = 0.20
    opacity = 0.8

    rects1 = plt.bar(index, recall, bar_width,
                     alpha=opacity,
                     color='b',
                     label = "Text"
                     )

    rects2 = plt.bar(index + bar_width, precision, bar_width,
                     alpha=opacity,
                     color='g',
                     label = "Abstract"
                     )

    rects3 = plt.bar(index + 2 * bar_width, map, bar_width,
                     alpha=opacity,
                     color='r',
                     label = "Full Text"
                     )

    # plt.xlabel('Topic ID')
    # plt.ylabel('Recall')
    # plt.title('Search by Title')
    plt.xticks((index + bar_width), ['Recall', 'Precision', 'Map', 'F-Beta'])
    plt.legend()

    plt.tight_layout()

    plt.show()

sbt()