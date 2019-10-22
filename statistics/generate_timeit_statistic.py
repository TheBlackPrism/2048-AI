import matplotlib.pyplot as plt
import numpy as np

searchai_times = [
    {"depth": 1, "timepermove": 0.010971},
    {"depth": 2, "timepermove": 0.067817},
    {"depth": 3, "timepermove": 2.558497},
    {"depth": 4, "timepermove": 48.070847},
    {"depth": 5, "timepermove": 1641.396178},
]

searchai_times_multiprocess = [
    {"depth": 1, "timepermove": 0.008644},
    {"depth": 2, "timepermove": 0.040891},
    {"depth": 3, "timepermove": 0.620329},
    {"depth": 4, "timepermove": 24.369725},
    {"depth": 5, "timepermove": 416.629117},
]

depth = list(range(1, 6))
times = [0.010971, 0.067817, 2.558497, 48.070847, 1641.396178]
multiprocess_times = [0.008644, 0.040891, 0.620329, 24.369725, 416.629117]


def main():
    x = np.arange(0, 9, 1);

    # Trend für search ai times
    plt.plot(x, 0.0003 * np.exp(3.0395 * x), label='Trend line for singleprocess', color='#ffa524', linestyle='dotted')
    plt.plot(depth, times, label='Singleprocess', color='#ff7f0e', marker='o', linestyle='solid')

    # Trend für multiple process search ai times
    plt.plot(x, 0.0003 * np.exp(2.7956 * x), label='Trend line for multiprocesses', color='#f15e3e',
             linestyle='dotted')
    plt.plot(depth, multiprocess_times, label='Multiprocesses', color='#c31b1c', marker='o', linestyle='solid')

    plt.title("Snakey - Average Time per Move Depending of Depth")
    plt.legend()

    plt.xlabel("depth")
    plt.xlim([0, 8])
    plt.ylabel("seconds")
    plt.yscale('log')
    plt.show()


if __name__ == '__main__':
    main();
