from collections import deque

# The social network (graph)
graph = {}

graph["you"] = ["alice", "bob", "claire"]

graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]

graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    """
    A mango seller is anyone whose name ends with 'm'
    """
    return name.endswith("m")


def search(name):
    # Create a queue
    search_queue = deque()

    # Add your direct friends
    search_queue += graph[name]

    # Keep track of people already checked
    searched = []

    while search_queue:
        # Take the first person from the queue
        person = search_queue.popleft()

        # Check only if not already checked
        if person not in searched:

            print(f"Checking {person}...")

            # Is this person a mango seller?
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True

            # Otherwise add their friends to the queue
            else:
                search_queue += graph[person]
                searched.append(person)

    print("No mango seller found.")
    return False


# Start searching from you
search("you")


# The time complexity of this in O(v + E)
# V - for vertices
# E - for edges