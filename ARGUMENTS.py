def greet(name, greeting ='Hello, <name>!'):
    return(greeting.replace('<name>', name))
greet('Bruce')
print(greet('Bruce', 'Alles goed, <name>?'))


def force(mass, body ='earth'):
    m = float(mass)
    planet = {
        'sun':274, 
        'jupiter':24.9,
        'neptune':11.1,
        'saturn':10.4,
        'earth':9.8,
        'uranus':8.9,
        'venus':8.9,
        'mars':3.7,
        'mercury':3.7,
        'moon':1.6,
        'pluto':0.6
    }
    return(m * planet[body])
print(force(5, 'moon'))


def pull(m1, m2, d):
    G = float(6.674 * 10**-11)
    pull = G  * (m1 * m2 / d**2)
    return pull
print(pull(10, 10, 10))