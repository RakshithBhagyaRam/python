def O_func(x):
    def i_func(y):
        return x*y
    return i_func

my_func=O_func(2)
print(my_func(3))




#output = 6



#tracing

"""Here, the O_func is a higher-order function that takes a single argument x and returns another function i_func. The returned 
i_func is a closure that captures the value of x and has its own argument y. When my_func is assigned the result of O_func(2), 
it is actually the returned i_func with x=2 captured. Finally, my_func(3) calls i_func(3), which returns 2 * 3 = 6."""

