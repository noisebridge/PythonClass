# Christopher Beacham May 5, 2017
# Created for Noisebridge Python class, distribute and use freely

# This is an example program that is a client for Studio Ghibli's API.
# (https://ghibliapi.herokuapp.com/#section/Studio-Ghibli-API)
# It downloads all the resources available in the API, and cross links some of them,
# to make an in-memory copy.
# Unfortuately, it is written in a way that it makes way too many requests,
# And takes way too long!

# Use these debugging tools to understand it's behavior and improve it's performance:
# Charles https://www.charlesproxy.com
# PUDB https://documen.tician.de/pudb/
# cProfile https://docs.python.org/2/library/profile.html
# SnakeViz (for reading cProfile output) https://jiffyclub.github.io/snakeviz/


# Your challenges:
# 1 - Make this script faster. It's really slow on my machine. WHY?
# 2 - This script uses too many network calls. Can you use less?
# 3 - The network calls are blocking, they could be parallel. You can see this in charles. Can you fix that?
# 4 - The story it makes at the end sucks, and doesn't use all of the resources
#     available to you from the API. Make it cooler.


import requests
import random
# This is like namedtuple, but mutable. (https://pypi.python.org/pypi/recordtype)
# `pip install recordtype` to get it
from recordtype import recordtype

GHIBLI_URL = "https://ghibliapi.herokuapp.com/"
session = requests.session()
# We don't want to panic when we see charles custom SSL cert.
# I've turned ssl verification off, but you can also pass a file path to charles's cert
# There are several ways to handle this.
session.verify = False
# Here's what passing the cert file would look like.
# You can ask charles to save the file somewhere on your machine
# session.verify = "/Users/Christopher/charles_sessions/charles-ssl-proxying-certificate.pem"


Person = recordtype("Person", ["id",
                               "name",
                               "gender",
                               "age",
                               "eye_color",
                               "hair_color",
                               "films",
                               "species",
                               "url"])

Species = recordtype("Species", ["id",
                                 "name",
                                 "classification",
                                 "eye_colors",
                                 "hair_colors",
                                 "url",
                                 "people",
                                 "films", ])


Film = recordtype("Film", ["id",
                           "title",
                           "description",
                           "director",
                           "producer",
                           "release_date",
                           "rt_score",
                           "people",
                           "species",
                           "locations",
                           "vehicles",
                           "url"])

Vehicle = recordtype("Vehicle", ["id",
                                 "name",
                                 "description",
                                 "vehicle_class",
                                 "length",
                                 "pilot",
                                 "films",
                                 "url", ])

Location = recordtype("Location", ["id",
                                   "name",
                                   "climate",
                                   "terrain",
                                   "surface_water",
                                   "residents",
                                   "films",
                                   "url", ])


def get_record(recordtype, record_url):
    """
    Given a record url and a recordtype, fetch the record from the and build the record.
    Assume there's just one record at the location and everything goes well
    """

    resp = session.get(record_url)

    new_record = recordtype(**resp.json())
    return new_record


def is_specific_url(url):
    """
    This api has a tendency to give you the url for the general list of things
    if there are no entries.
    this separates "people/" from "people/123456"
    """
    return url[-1] != '/'


def get_all_people():
    """
    You can hit the resource name without an ID to get a listing of all of that resource
    """

        resp = session.get(GHIBLI_URL + "people")
        people = [Person(**json_person)
                  for json_person in resp.json()]
        return people


def make_crossover(all_people):
    """
    Make a new story about the studio ghibli characters
    """
    story = """
    {protagonist.name} is a {protagonist.gender} {protagonist.species.name},
    and {friend.name} is a {friend.gender} {friend.species.name},  and they are going on an adventure.
    They have to challenge many obstacles, and fight the evil {antagonist.name}, a {antagonist.age} year old
    {antagonist.species.name}

    """
    # import pudb; pudb.set_trace()  # breakpoint 7ee757b5 //

    story_choices = {
        "protagonist": random.choice(all_people),
        "friend": random.choice(all_people),
        "antagonist": random.choice(all_people),
    }
    print story.format(**story_choices)
    from guppy import hpy
    heap = hpy()
    print heap.heap()


def main():
    people = get_all_people()
    for person in people:
        person.species = get_record(Species, person.species)
        film_objs = []
        # I wish this graph was fully connected, it would be cooler for the story, maybe...
        for film_url in person.films:
            film = get_record(Film, film_url)
            film.locations = [get_record(Location, url)
                              for url in film.locations if is_specific_url(url)]
            film.vehicles = [get_record(Vehicle, url)
                             for url in film.vehicles if is_specific_url(url)]
            film_objs.append(film)

        person.films = film_objs
    make_crossover(people)


if __name__ == '__main__':
    main()
