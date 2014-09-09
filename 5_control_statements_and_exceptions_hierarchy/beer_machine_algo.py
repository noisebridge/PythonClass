import random 

def gen_bottle_cluster():
    for i in range(10):
        yield random.randint(-5, 35)

def log(print_arg):
    """totally fake logging function"""
    print(print_arg)

#check to see how many bottles we've received in the cluster
#raise ZeroDivisionError if we receive any value of zero or less then fake log it with fake log function
#get 


def beer_problem(list_of_beer_clusters):
    leftovers = 0
    six_packs_made = 0
    if leftovers < 6:
        for beer in list_of_beer_clusters:
            if beer > 0:
                six_packs_made += beer // 6
                leftovers += beer % 6
            else:
                #raise ZeroDivisionError
                log("ZeroDivisionError")
    else:
        leftovers -= 6
        six_packs_made += 1
    print("list of beer_clusters_was:\n {}".format(list(list_of_beer_clusters)))
    return six_packs_made, leftovers





print beer_problem(gen_bottle_cluster())