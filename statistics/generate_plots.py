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
    data_scores=[]
    data_tiles=[]
    data_time=[]
    data_moves=[]
    tickLabels = []
    for stat in stats:
        stat['df'] = pd.read_csv(stat["csv"], sep=';')
        data_scores.append(stat['df']['score'].tolist())
        data_tiles.append(stat['df']['highest tile'].tolist())
        data_time.append(stat['df']['time per move'].tolist())
        data_moves.append(stat['df']['number of moves'].tolist())
        tickLabels.append(stat['name'])

    # Boxplots - Scores
    fig1, ax1 = plt.subplots()
    ax1.set_title(title + " - Scores")
    ax1.set_ylabel('Score')
    ax1.boxplot(data_scores)
    plt.xticks(range(1,len(tickLabels)+1), tickLabels)
    plt.show()

    # Boxplots - Tiles
    fig1, ax1 = plt.subplots()
    ax1.set_title(title + " - Highest Tile")
    ax1.set_ylabel('Tile')
    ax1.boxplot(data_tiles)
    plt.xticks(range(1,len(tickLabels)+1), tickLabels)
    plt.show()

    # Boxplots - Time
    fig1, ax1 = plt.subplots()
    ax1.set_title(title + " - Time per Move")
    ax1.set_ylabel('Tile')
    ax1.boxplot(data_time)
    plt.xticks(range(1,len(tickLabels)+1), tickLabels)
    plt.show()

    # Boxplots - Moves
    fig1, ax1 = plt.subplots()
    ax1.set_title(title + " - Number of Moves")
    ax1.set_ylabel('Tile')
    ax1.boxplot(data_moves)
    plt.xticks(range(1,len(tickLabels)+1), tickLabels)
    plt.show()

    # Barcharts
    for stat in stats:
        df = stat['df'].sort_values(by=['highest tile'])
        labels = list(map(str, Counter(df['highest tile'].tolist()).keys()))
        values = list(Counter(df['highest tile'].tolist()).values())

        tile_occurences = {'256': 0,
                '512': 0,
                '1024': 0,
                '2048': 0,
                '4096': 0,
                '8192': 0,}

        for i in range(len(labels)):
            tile_occurences[str(labels[i])] = values[i]

        print(tile_occurences)

        plt.subplot()
        plt.bar(tile_occurences.keys(), tile_occurences.values(), 0.3)
        plt.title(title + ' ' + stat['name'] + ' - Highest tile reached')
        plt.xlabel('tile')
        plt.ylim([0,15])
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
