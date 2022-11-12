
def a(*args):
    for i in args:
        print(i)
    print(*args)
a("a","b","c","d")        