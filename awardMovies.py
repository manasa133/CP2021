# movieAwards(oscarResults) [10 pts]
# Write the function movieAwards(oscarResults) that takes a set of tuples,
#  where each tuple holds the name of a category and the name of the winning movie, 
# then returns a dictionary mapping each movie to the number of the awards that it won. 
# For example, if we provide the set:
# { 
#     ("Best Picture", "The Shape of Water"), 
#     ("Best Actor", "Darkest Hour"),
#     ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
#     ("Best Director", "The Shape of Water"),
#     ("Best Supporting Actor", "Three Billboards Outside Ebbing, Missouri"),
#     ("Best Supporting Actress", "I, Tonya"),
#     ("Best Original Score", "The Shape of Water")
# }
# the function should return as follows
# { 
#     "Darkest Hour" : 1,
#     "Three Billboards Outside Ebbing, Missouri" : 2,
#     "The Shape of Water" : 3,
#     "I, Tonya" : 1
# }

def movieAwards():
    given_input = { 
        ("Best Picture", "The Shape of Water"), 
        ("Best Actor", "Darkest Hour"),
        ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
        ("Best Director", "The Shape of Water"),
        ("Best Supporting Actor", "Three Billboards Outside Ebbing, Missouri"),
        ("Best Supporting Actress", "I, Tonya"),
        ("Best Original Score", "The Shape of Water")
    }
    movie = dict()
    for i in given_input:
        if(i[1] not in movie):
            movie[i[1]] = 1
        else:
            movie[i[1]] = movie[i[1]] + 1
    print(movie)

    
movieAwards()

