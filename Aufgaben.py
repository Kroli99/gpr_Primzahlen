#Aufgabe 1
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#Aufgabe 2
def all_primes(x):
    allprimes = []
    for i in range(x+1):
        if is_prime(i) == True:
            allprimes.append(i)
        else:
            continue
    return allprimes

#Aufgabe 3
def eratosthenes(num):
    primes = []
    for i in range(2,num+1):
        if i == 2:
            primes.append(i)
        elif i % 2 == 0:
            continue
        elif i == 3:
            primes.append(i)
        elif i % 3 == 0:
            continue
        elif i == 5:
            primes.append(i)
        elif i % 5 == 0:
            continue
        elif i == 7:
            primes.append(i)
        elif i % 7 == 0:
            continue
        else:
            primes.append(i)
    return primes

#Aufgabe 4
def distances(prime_numbers):
    distance = []
    for i in range(0, len(prime_numbers)-1):
        if i >= 0:
            distance.append(abs(prime_numbers[i] - prime_numbers[i+1]))
    return distance

#Aufgabe 5
def heuristic(rep):
    repetition = []
    for i in range(0, len(rep)):
        repetition.append((rep[i], rep.count(rep[i])))
    return set(repetition)

#Aufgabe 6


#print(heuristic(distances(all_primes(100))))
#print(is_prime(5))
#print(all_primes(100))
#print(eratosthenes(100))
#print(distances(all_primes(100)))

def is_prime(n):
    if n < 2: return False
    elif n == 2: return True
    for i in range(2, n):
        if n % i == 0: return False
    return True

def all_primes(x):
    allprimes = [i for i in range(x+1) if is_prime(i) == True]
    return allprimes

print(is_prime(5))
print(all_primes(100))


row = [i for i in range(len())]