from asyncio.windows_events import NULL
import json
from queue import PriorityQueue
from numpy import Infinity
import random
import time

with open('przystanki.json', "r", encoding='utf-8') as read_file:
    stops = json.load(read_file)
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    trams = json.load(read_file)

graph = {}
for name in stops["przystanki"]:
    graph.update({name: []})

for tram in trams["tramwaje"]:
    tstops = tram["tprzystanki"]
    tname = tram["name"]
    size = len(tstops)
    for i in range(size):
        if i != size-1:
            graph[tstops[i]["name"]].append((tname, tstops[i+1]["name"]))
        if i != 0:
            graph[tstops[i]["name"]].append((tname, tstops[i-1]["name"]))


stops = []
for tram in trams["tramwaje"]:
    tstops = tram["tprzystanki"]
    for stop in tstops:
        if not stop["name"] in stops:
            stops.append(stop["name"])


def Dijkstra(G, start, goal):
    parent = {}
    value = {}
    value[start] = (0, 0)
    parent[start] = (0, NULL, 0)
    # value: (przystanek: waga, tram_counter)

    V = PriorityQueue()
    V.put((0, start))

    while not V.empty():
        val, stop_name = V.get()
        if val == value[stop_name][0]:
            for e in G[stop_name]:
                weight = 1
                if (e[1] not in value.keys() or value[e[1]][0] > value[stop_name][0] + 1):

                    # e[0] - tram name
                    parent[e[1]] = (value[stop_name][0], stop_name, e[0])

                    tram_counter = value[parent[e[1]][1]][1]
                    if parent[parent[e[1]][1]][2] != e[0]:
                        tram_counter += 1
                        if tram_counter > 3:
                            weight = Infinity

                    value[e[1]] = (value[stop_name][0] +
                                   weight, tram_counter)

                    V.put((value[e[1]][0], e[1]))

    stop = goal
    i = value[goal][0]
    res = ''
    res += f'{i}. {stop}\n'
    i -= 1
    while stop != start:
        res += f'{i}. [{parent[stop][2]}] {parent[stop][1]}\n'
        stop = parent[stop][1]
        i -= 1

    if value[goal][0] == Infinity:
        print("Potrzeba więcej niż 2 przesiadki")
    else:
        print(
            f'Długość drogi: {value[goal][0]}\nIlość tramwajów: {value[goal][1]}')

    return res


def test_dijkstra():
    start_time = time.time()
    for i in range(1000):
        start = random.choice(stops)
        end = random.choice(stops)
        while end == start:
            end = random.choice(stops)

        print(f"--- Algorytm Dijkstry dla przystanków: {start} - {end} ---")
        Dijkstra(graph, start, end)
    print("--- %s seconds ---" % (time.time() - start_time))


# test_dijkstra()
# start_point = "Klasztorna"
# end_point = "Bratysławska"
start_point = input("Przystanek początkowy: ")
end_point = input("Przystanek końcowy: ")
print(f'Algorytm Dijkstry dla przystanków: {start_point} - {end_point}')
print(Dijkstra(graph, start_point, end_point))
