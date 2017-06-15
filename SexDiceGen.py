import random


dice1=['whisper into','fuck','suck','tickle','smother','tie up','handjob','threesome with a nigger and','cuddle','titfuck','send tentacles on']
dice2=['Tzach','Bush','Avrech', 'Nitay', 'Byle', 'Tzabari', 'Shrek', 'Nave', 'Ofek','Yotam','Kalish']
dice3=['','with clothes on', 'in the fridge', '\'s asshole', 'in the gorilla cage', 'at Dizengoff Center', 'while 9/11 happens', 'at school', 'but it\'s a hentai', 'while locked in your basement', 'on Shrek\'s dick', 'in a sick minecraft server', 'while jacking Zeus off']

def randomchoose(arr):
    return arr[random.randint(0, len(arr)-1)]

def sendToChat():
    sendstring = randomchoose(dice1) + ' ' + randomchoose(dice2) + ' ' + randomchoose(dice3)
    print(sendstring)
    return sendstring
