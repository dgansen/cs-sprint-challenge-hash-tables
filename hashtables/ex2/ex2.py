#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    trip = {}
    route = []
    for t in tickets:
        trip[t.source] = t.destination
        if t.source == 'NONE':
            route.append(t.destination)
    while len(route) < length:
        route.append(trip[route[-1]])

    return route
