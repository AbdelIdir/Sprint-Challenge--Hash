class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    dictio = {}

    for ticket in tickets:
        # linking ticket destinations together
        dictio[ticket.source] = ticket.destination

    route = []
    trip = "NONE"
    for t in range(len(dictio)):

        # reconstructing the trip
        trip = dictio[trip]
        route.append(trip)
    return route
