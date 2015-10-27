import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def get_arrival_time_data():
    big_table = dict()

    print("Get arrival times from arrival_time.txt")
    with open('arrival_time.txt', 'r') as input_file:
        for line in input_file:
            key = int(str.split(line)[0])
            val = int(str.split(line)[1])
            big_table[key] = val

    return big_table


def compress_data(big_table):
    compressed_big_table = dict()

    print("Compress data in packet of 5 minutes")

    first_second_of_day = 0
    last_second_of_day = 24*3600
    packet_size = 60*5

    for i in range(first_second_of_day, last_second_of_day, packet_size):
        elements = list()
        for j in range(0, packet_size):
            key = i + j
            if key in big_table:
                elements.append(big_table[key])
        val = sum(elements)/len(elements)
        compressed_big_table[i] = val

    print("- previous size: " + str(len(big_table)))
    print("- new size: " + str(len(compressed_big_table)))

    return compressed_big_table


def draw_graph(big_table):
    fig = plt.figure(num=None, figsize=(22, 8), dpi=200, facecolor='w', edgecolor='k')

    print("Drawing the graph")
    x = big_table.keys()
    y = big_table.values()

    ax = plt.gca()

    print("- add the data to the graph")
    #plt.plot(x, y, 's')
    #plt.hist(big_table, 24*10, normed=1, histtype='bar', facecolor='green', alpha=0.75)
    ax.bar(x, y, width=60*5, color='g', alpha=0.8)

    print("- improve the x axis with hours")
    start, end = ax.get_xlim()
    data_range = np.arange(start, end, 3600.0) # 3600 x 1 sec = 1h
    ax.xaxis.set_ticks(data_range)
    ax.xaxis.set_ticklabels(['0',
        '1AM', '2AM', '3AM', '4AM', '5AM', '6AM',
        '7AM', '8AM', '9AM', '10AM', '11AM', '12AM',
        '1PM', '2PM', '3PM', '4PM', '5PM', '6PM',
        '7PM', '8PM', '9PM', '10PM', '11PM', '12PM'
    ])
    plt.xlabel('Hours')
    ax.set_title('Arrival date of Workflows')

    print("- limit the x axis to 24 hours")
    plt.xlim([0, 24*3600])

    print("Saving the image")
    plt.tight_layout()
    plt.grid(True)
    plt.savefig('graph.png')

    print("Image graph.png generated")


big_table = compress_data(get_arrival_time_data())
draw_graph(big_table)
