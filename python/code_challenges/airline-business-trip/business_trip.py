from graphs.graphs import Graph


def business_trip(graph, flights):
    flight_direct = graph.get_neighbors()
    if flight_direct == None:
        return False




