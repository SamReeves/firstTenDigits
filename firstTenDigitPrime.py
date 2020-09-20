#!/usr/bin/env python3

import re
# all prime numbers under 100,000
with open('100kPrimes', 'r') as p100k_file:
    p100k = p100k_file.readlines()
    p100k = p100k[1:]

# remove non-numeric characters
for prime in range(len(p100k)):
    p100k[prime] = int(re.sub("[^0-9]","",p100k[prime]))
    
# first 1000 digits of e:
e1k = "7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424371075390777449920695517027618386062613313845830007520449338265602976067371132007093287091274437470472306969772093101416928368190255151086574637721112523897844250569536967707854499699679468644549059879316368892300987931277361782154249992295763514822082698951936680331825288693984964651058209392398294887933203625094431173012381970684161403970198376793206832823764648042953118023287825098194558153017567173613320698112509961818815930416903515988885193458072738667385894228792284998920868058257492796104841984443634632449684875602336248270419786232090021609902353043699418491463140934317381436405462531520961836908887070167683964243781405927145635490613031072085103837505101157477041718986106873969655212671546889570350354"
    
def firstTenDigitPrime(p100k=p100k):
    ends = ["1","3","7","9"]
    possible = []
    nonPrime = []
    
    # split e and remove obvious non-primes
    for position in range(0,len(e1k)-10):
        candidate = e1k[position:position+10]
        if (candidate[9] in ends) and (candidate[0] != "0"):
            possible.append(int(candidate))

    # discover primes against primes < 1e5
    for number in possible:
        for prime in p100k:
            if number%prime == 0:
                nonPrime.append(number)
                break

    primes = list(set(possible) - set(nonPrime))
    for number in possible:
        if number in primes:
            return number

firstTenDigitPrime()