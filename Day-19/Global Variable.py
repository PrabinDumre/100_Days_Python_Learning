# Global keyword

l = 10
def fun(n):
    #l =11
    m = 1
    global l
    print(l,m)
    l = l+4
fun("Prabin")
print(l)


x = 18
def prabin():
    x = 16
    def ridam():
        global x
        x = 11
    print("Before calling ridam",x)
    ridam()
    print("After calling ridam",x)

prabin()
print(x)
