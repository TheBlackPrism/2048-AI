import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

searchai_stats = [{ "name": "Heuristic", "csv": "searchai_heuristic.csv", "df": []},
    { "name": "Snakey", "csv": "searchai_snakey.csv", "df": []},
    { "name": "Snakey +", "csv": "searchai_snakey_plus.csv" , "df": []},
    { "name": "Diagonal", "csv": "searchai_diagonal.csv", "df": []},
    { "name": "Square", "csv": "searchai_square.csv", "df": []}]

heuristicai_stats = [{ "name": "Random Agent", "csv": "heuristicai_0_random_agent.csv", "df": []},
    #{ "name": "Pretty Basic", "csv": "heuristicai_jenny1_pretty_basic.csv", "df": []},
    { "name": "Pretty Good", "csv": "heuristicai_jenny2_pretty_good.csv", "df": []},
    #{ "name": "Check Score", "csv": "heuristicai_jenny3_check_score.csv", "df": []},
    #{ "name": "Check Score 2", "csv": "heuristicai_jenny4_check_score_altered_weights.csv", "df": []},
    { "name": "Check Score", "csv": "heuristicai_jenny5_check_score_minimize_up.csv", "df": []},
    { "name": "Hierarchical Rating", "csv": "heuristicai_yves.csv", "df": []}]

def main():
    generatePlots(searchai_stats, "Search AI", True)
    generatePlots(heuristicai_stats, "Heuristic AI", False)

def generatePlots(stats, title, isHigh):
    data_scores = []
    data_tiles = []
    data_time = []
    data_moves = []
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
    plt.xticks(range(1,len(tickLabels) + 1), tickLabels)
    plt.show()

    # Boxplots - Tiles
    fig1, ax1 = plt.subplots()
    ax1.set_title(title + " - Highest Tile")
    ax1.set_ylabel('Tile')
    ax1.boxplot(data_tiles)
    plt.xticks(range(1,len(tickLabels) + 1), tickLabels)
    plt.show()

    # Boxplots - Time
    fig1, ax1 = plt.subplots()
    ax1.set_title(title + " - Time per Move")
    ax1.set_ylabel('Tile')
    ax1.boxplot(data_time)
    plt.xticks(range(1,len(tickLabels) + 1), tickLabels)
    plt.show()

    # Boxplots - Moves
    fig1, ax1 = plt.subplots()
    ax1.set_title(title + " - Number of Moves")
    ax1.set_ylabel('Tile')
    ax1.boxplot(data_moves)
    plt.xticks(range(1,len(tickLabels) + 1), tickLabels)
    plt.show()

    # Barcharts

    tile_occurences = {}
    if isHigh:
        tile_occurences = {
            '256': 0,
            '512': 0,
            '1024': 0,
            '2048': 0,
            '4096': 0,
            '8192': 0}
    else:
        tile_occurences = {
                '32': 0,
                '64': 0,
                '128': 0,
                '256': 0,
                '512': 0,
                '1024': 0,
                '2048': 0,
                '4096': 0}

    x = 0.0
    idx = 0
    n = len(tile_occurences) # Number of tiles to display
    barWidth = 1.0 / (len(stats) + 1)
    ind = np.arange(n)
    fig1, ax1 = plt.subplots()
    #ax1 = fig1.add_subplot()
    bars=[]
    colors = ['#efb400', '#ff7f0e', '#c31b1c', '#136095', '#2ca02c'];
    for stat in stats:
        df = stat['df'].sort_values(by=['highest tile'])
        labels = list(map(str, Counter(df['highest tile'].tolist()).keys()))
        values = list(Counter(df['highest tile'].tolist()).values())

        for i in range(len(labels)):
            tile_occurences[str(labels[i])] = values[i] / sum(values) * 100
            
        print(tile_occurences)

        bars.append(ax1.bar(ind + x, tile_occurences.values(), width = barWidth, label = stat['name'], color = colors[idx]))
        x+= barWidth
        idx+=1
    ax1.set_xticks(ind + barWidth)
    ax1.set_xticklabels(tile_occurences.keys())
    ax1.legend()
    plt.title(title + ' - Highest tile reached')
    plt.xlabel('tile')
    plt.ylabel('percent (%)')
    plt.ylim([0,70])
    plt.show()

    print("<table><caption>Comparison of the implemented heuristic functions</caption>")
    print("<tbody><tr><th>Algorithm Name</th><th>Highscore</th><th>Average Score</th><th>Highest Tile</th><th>Time Per Move [s]</th></tr>")
    # sonstige Stats
    for stat in stats:
        """print()
        print("Highscore: " + str(max(stat['df']['score'])))
        print("Highest tile reached: " + str(max(stat['df']['highest tile'])))
        print("Average Time per move: " + str(stat['df']['time per move'].mean()))
        print()"""
        print("<tr><td>%s</td><td>%d</td><td>%d</td><td>%f</td></tr>" % (stat['name'], max(stat['df']['score']), max(stat['df']['highest tile']), stat['df']['time per move'].mean()))

    print("</tbody></table>")

if __name__ == '__main__':
    main();
