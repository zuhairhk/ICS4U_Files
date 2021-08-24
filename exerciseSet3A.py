import random


def fToC(temp):
    '''fToC() converts the temperature from farenheit to celsius
    arg:
    -- temp : float
    return:
    -- temp : float
    '''

    fTemp = (temp - 32) / 1.8

    return fTemp


def cToF(temp):
    '''fToC() converts the temperature from celsius to farenheit
    arg:
    -- temp : float
    return:
    -- temp : float
    '''

    cTemp = (temp * 1.8) + 32

    return cTemp


t = random.randint(0, 45)
print('T is:', t)
print('F to C:', fToC(t))
print('C to F:', cToF(t))
