import pylab

fact = {}

def factorial(n = 100):
    fact[0] = 1
    fact[1] = 1
    for i in range(2, n + 1):
        fact[i] = 1
        fact[i] *= fact[i - 1]

def probabilityExactlyTwo3s(k):
    kc2 = fact[k] / (fact[2] * fact[k - 2])
    success = (1/6)**2
    failure = (5/6)**(k - 2)
    return kc2 * success * failure
    
def rangeK(num = 100):
    probabilities = []
    xAxis = []
    for k in range(2, num + 1):
        xAxis.append(k)
        probabilities.append(probabilityExactlyTwo3s(k))
    return (xAxis, probabilities)

factorial()
xAxis, probabilities = rangeK()
pylab.title('Probability of Rolling Exactly Two 3s')
pylab.xlabel('k')
pylab.ylabel('Probability')
pylab.plot(xAxis, probabilities, 'ko')
pylab.yscale("log")
pylab.show()