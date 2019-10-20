import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

searchai_stats = [
    { "name": "heuristic", "csv": "searchai_heuristic.csv", "df": []},
    { "name": "snakey", "csv": "searchai_snakey.csv", "df": []},
    #{ "name": "snakey +", "csv": "searchai_snakey_plus.csv" , "df": []},
    { "name": "diagonal", "csv": "searchai_diagonal.csv", "df": []},
    { "name": "square", "csv": "searchai_square.csv", "df": []}
]

heuristicai_stats = [
    { "name": "heuristic", "csv": ".csv", "df": []},
]

def main():
    generatePlots(searchai_stats, "Search AI")
    #generatePlots(heuristicai_stats)

def generatePlots(stats, title):
    data=[]
    tickLabels = []
    for stat in stats:
        stat['df'] = pd.read_csv(stat["csv"], sep=';')
        data.append(stat['df']['score'].tolist())
        tickLabels.append(stat['name'])

    fig1, ax1 = plt.subplots()
    ax1.set_title(title + " - Scores")
    ax1.set_ylabel('Score')
    ax1.boxplot(data)

    plt.xticks(range(1,len(tickLabels)+1), tickLabels)
    plt.show()


if __name__ == '__main__':
    main();
