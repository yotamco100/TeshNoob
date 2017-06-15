import random
names = ['a shooting game', 'an action game', 'an FPS', 'a horror game', 'a tycoon game', 'a sim game', 'a simulation game', 'a god game']

actions = ['school shoot', 'make memes with', 'blame avrech and', 'send emojis of', 'send nudes of', 'out-edge', 'browse r/reallywhackytictacs with', 'harass', 'cyberbully', 'make feminists']

things = ['Yotam', 'Byle', 'jews', 'KKK members', 'Avrech', 'Nitay', 'Tzabari', 'Bentu', 'Kalish', 'Arad', 'memes', 'niggers', 'a nigger', 'our lizard overlords', 'a KKK member', 'feminists', 'feminazis', 'a feminist', 'a feminazi',
':regional_indicator_b:igger']

goals = ['to make memes','to shoot jews', 'to kill niggers', 'and niggers are still slaves', 'to commit sudoku', 'and the main character commits suicide at the end', 'and the main character is Avrech', 'and the one to blame is Avrech', 'and Bentu makes memes behind you', 'and Kalish comes out of the closet', 'but you\'ve been a nigger all along', 'and everyone are feminazis', 'and you must take down the patriarcy with your newly-formed team']

wildcards = ['','- written in assembly', '- the Musical', '- Coming 2018', '- Featuring Shrek', '- Official Merch Soon', '- but it was too overhyped', '- the Minecraft clone', '- Fidget Spinner Edition']

def randomchoose(arr):
    return arr[random.randint(0, len(arr)-1)]

def sendToChat():
    sendstring = randomchoose(names) + ' where you ' + randomchoose(actions) + " " + randomchoose(things) + " " + randomchoose(goals) + " " + randomchoose(wildcards)
    print(sendstring)
    return sendstring
