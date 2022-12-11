# if u cannot change anything in the given function then use this in the inner function
def div(a,b):
    print(a/b)
    def newdiv(func):
        def innerfunc(a,b):
            if a<b:
                a,b=b,a
            return func(a,b)
        return innerfunc
div(4,2)                           
