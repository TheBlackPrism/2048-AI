import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

searchai_stats = [
    { "name": "Heuristic", "csv": "searchai_heuristic.csv", "df": []},
    { "name": "Snakey", "csv": "searchai_snakey.csv", "df": []},
    #{ "name": "snakey +", "csv": "searchai_snakey_plus.csv" , "df": []},
    { "name": "Diagonal", "csv": "searchai_diagonal.csv", "df": []},
    { "name": "Square", "csv": "searchai_square.csv", "df": []}
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

    # Boxplots
    fig1, ax1 = plt.subplots()
    ax1.set_title(title + " - Scores")
    ax1.set_ylabel('Score')
    ax1.boxplot(data)
    plt.xticks(range(1,len(tickLabels)+1), tickLabels)
    plt.show()

    # Barcharts
    for stat in stats:
        df = stat['df'].sort_values(by=['highest tile'])
        labels = list(map(str, Counter(df['highest tile'].tolist()).keys()))
        values = Counter(df['highest tile'].tolist()).values()
        plt.subplot()
        plt.bar(labels, values, 0.3)
        plt.title(title + ' ' + stat['name'] + ' - Highest tile reached')
        plt.xlabel('tile')
        plt.show()

    # sonstige Stats
    for stat in stats:
        print(stat['name'])
        print("Highscore: " + str(max(stat['df']['score'])))
        print("Highest tile reached: " + str(max(stat['df']['highest tile'])))
        print("Average Time per move: " + str(stat['df']['time per move'].mean()))
        print()


if __name__ == '__main__':
    main();
