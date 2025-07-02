class heroine:
    name = "alia"
    age  = 34

    def actor(a):
        print("she is a good actress")

h1 = heroine()
print(h1.name)
print(h1.age)
h1.actor()

h1.noOfMovies = 20
print(h1.noOfMovies)
h1.age = 35
print(h1.age)
del h1.noOfMovies
# print(h1.noOfMovies)