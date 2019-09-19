# import csv

# with open('names.csv', 'w') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

def bar_plot():
    import matplotlib.pyplot as barplt
    from matplotlib import style
    style.use("ggplot")
    barplt.xlabel("Rank")
    barplt.ylabel("Score")
    barplt.title("Topic : CD010632")
    barplt.barh(range(10), df.score[:10])
    barplt.savefig("Plot\\Bar_Plot.png")

def simple_plot():
    import matplotlib.pyplot as plt
    from matplotlib import style
    style.use("ggplot")
    plt.xlabel("Rank")
    plt.ylabel("Score")
    plt.title("Topic : CD010632")
    plt.scatter(range(len(df.score)), df.score)
    plt.savefig("Plot\\Simple_Plot.png")

import pandas as pd
df = pd.read_csv("CSV\\CD010632.csv", usecols=['pid', 'score'])
a = []
for i in df.score:
    a.append(i)

bar_plot()
