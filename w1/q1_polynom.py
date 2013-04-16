'''
Implement the mathematical function f(x) = -5 x5 + 69 x2 - 47 as a Python function. 
Then use Python to compute the function values f(0), f(1), f(2), and f(3).
'''

def function(x):
    res = -5 * (x ** 5) + 69 * (x ** 2) - 47
    print res
    return res


function(0)
function(1)
function(2)
function(3)