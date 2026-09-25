def grad(x):
    return 2*x
def cost(x):
    return x**2 - 2
def myGD1 (x0, eta):
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta * grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, it)
(x1, it1) = myGD1(3, 0.1)
(x2, it2) = myGD1(2, 0.1)
print ('Solution x1 = %f, cost = %f, after %d iterations' % (x1[-1], cost(x1[-1]), it1))
print ('Solution x2 = %f, cost = %f, after %d iterations' % (x2[-1], cost(x2[-1]), it2))