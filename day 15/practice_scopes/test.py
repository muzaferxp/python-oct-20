
p = 10
x = None

def test():
    global x
    x = 5
    y = 10
    print(p)
def test2():
    a = 5
    #print(x)
    print(p)
    
test()

test2()

print("the value of x is", x)