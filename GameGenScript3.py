import random
names = ['a shooting game', 'an action game', 'an FPS', 'a horror game', 'a tycoon game', 'a sim game', 'a simulation game', 'a god game']

actions = ['kill','shoot','club','murder','stab','chop up','wrestle','kick','punch','slap','destroy','blow up','eradicate','begrudgingly join forces with','ally with','team up with','interrogate','do science on','use your powers on','save','ride horses with','drive cars with','drive tanks with','drive trucks with',
'ride bikes with','have been contracted to kill','assassinate','rob','bribe','hunt','poison','motivate','work on the self-esteem of','feel bad for','cheer up','go on a heist with','pilot spaceships with','listen to','hijack','goof around with','run after','smuggle','defeat','beat up','date','save the world from','time travel with','go back in time to kill','shout at',
'point your gun at','commit war crimes with','freeze','burn', 'manage','sell','buy','trade','reticulate','drag and drop','displace','mutate','splice','mix-and-match','build','customize','herd','terraform','regulate','plop down','create','make','invent','grow','piece together',
'hatch','raise','farm','write about','draw','distribute','craft','compile','solve','monetize','design','mix','experiment on','experiment with','copy-paste','organize','dress up','train','breed','feed','grow','grow stuff on','cure','heal','fix',
'tame', 'school shoot', 'make memes with', 'blame Avrech and', 'send emojis of', 'send nudes of', 'out-edge', 'browse r/reallywhackytictacs with', 'harass', 'cyberbully']

things = ['cars','cops','the police','the CIA','the president','thugs','criminals','gangsters','war criminals','helicopters','jeeps','superheroes','detectives','villains','monsters','babies','random people','civilians','innocent people','prisoners','explosions','bankers','space people','puppies',
'kittens','sharks','bears','gorillas','city guards','ninjas','knights','spies','soldiers','barbarians','aliens','rappers','conspiracy theorists','clowns','evil AIs','giant robots','war robots','crowbars','cosmonauts','extra-dimensional entities','ascended beings','demi-gods','wizards','cavemen','apes',
'mutants','zombies','mutant zombies','robots','robot zombies','mutant zombie robots','nazis','zombie nazis','robot nazis','zombie ghosts','cyborgs','hippies','terrorists','scientists','researchers','fashion designers','jazz singers','dinosaurs','giant crabs','cute girls','hot boys','famous people','mascots','your long-lost relatives','asteroids',
'the forces of good','the forces of evil', 'Yotam', 'Byle', 'jews', 'KKK members', 'Avrech', 'Nitay', 'Tzabari', 'Bentu', 'Kalish', 'Arad', 'memes', 'niggers', 'a nigger', 'our lizard overlords']

goals = ['to make dollah','to get big','to make a name for yourself','to save the world','to save the universe','to investigate a conspiracy','to prevent an evil plot','to solve mysteries','to make them pay','because they looked at you weird','(that\'ll show them)','to get your revenge','to avenge your girlfriend','to become the next big thing','to be a bad enough dude','to unlock achievements','for achievements','in outer space','in a black hole','in the future','in the third world','in the 40s','in the 50s',
'in the 70s','in the 90s','in the year 3000','in the year 10,000','in the \'nads','in Russia','in Europe','in China','in North Korea','in South Africa','in America','in Australia','on Mars','on the Moon','after landing on a mysterious planet','in a frozen wasteland','in the desert','underwater','in an abandoned facility','inside a gigantic terrarium','in a single closed room','in a graveyard','in a junkyard','in the cyberspace','in a wizard tower',
'in a network of underground bunkers','in a laboratory','in a secret research facility','in a lush grassland','while stranded on an island','on an uncharted island','in an empty school','in a historical monument','in hilarious locations','on the set of a movie','until the sequel','to find love','to impress your date','for freedom','for liberty','because it\'s the right thing to do','because, I mean, why the hell not','(don\'t question it)','and you have to find out why','and the reason why becomes less and less obvious throughout the game','to accelerate global warming','to slow global warming','because aliens','because Hitler',
'and go back in time','TO THE MAX','TO THE EXTREME','(with day 1 DLC)','in a sandbox world','and also it\'s kind of a dating sim','and you have to be stealthy and stuff','with kill-streak bonuses','but then skeletons','but you have no arms','except halfway through you realize you\'re really not all that important to the plot','but you don\'t play a big role in the story so you can actually do pretty much whatever you want','and your sidekick is a bird','with a snarky sidekick','with a passive-aggressive sidekick','with a slighly racist sidekick','and your sidekick is the bad guy','except you\'re the sidekick',
'with a shape-shifting sidekick','with too many sidekicks','and everyone in the game hates you','and you have superpowers','with gigantic boss battles','(it gets weirder)','(it gets very dark very fast)','(it\'s pretty light-hearted)','(also, sports)','and also you are a bear','and you can\'t stop running','but you keep randomly teleporting','except the game keeps messing around with your perception','except you\'re 3 years old','but you\'re an old person','until you feel regret','and you can\'t stop gaining powers','but you keep jumping forward in time','but bees are trying to stop you','with the addition of zombies','and everybody\'s a robot','but there are no humans',
'and you\'re the last of your kind','but only a handful of people remain','with other survivors','and magic has returned to the world','and you\'re a wacky animal','and you have way more limbs than necessary','and you\'re a spider','and you can summon your spirit animal','but it\'s all explained in the end','and it never ends','and you gotta go fast','as slowly as possible','and it\'s totally adorable','and it\'s scary as hell','and you\'re all alone','and everybody\'s afraid of you','with lots of customization','and your only weapon is mini-nukes','but everything you touch explodes','and everything you touch turns into more enemies','and your arms are chainsaws',
'and also you are a bird','and you\'re an unfrozen caveman','and you\'re also an ancient wizard','but the bad guy was just trying to help you','except you\'re really unlucky','and you have superhuman luck','except you\'re one of the bad guys','like in the movie','and the name and biography of everybody you kill is displayed onscreen','and corpses don\'t disappear','and you can use the corpses in creative ways','during the apocalypse','before the apocalypse','after the apocalypse','until the end of the world','and you steal the powers of your defeated enemies','and you have the power to become famous at will','and you can erect walls at will','and also you have telepathic powers','and you have stretchy powers','but you\'re composed of tiny critters','and the bad guy is constantly stalking you wherever you go',
'and there\'s a terrifying monster slowly making its way towards you during the whole game','and you only have a few minutes to live','while looking absolutely fantastic','and you keep jumping through windows','and you can\'t stop breaking stuff','but you kill the people you try to help','but you\'re a ghost','and you\'re a cyborg','and you\'re addicted to robot implants','with unpredictable powers','while setting fire to stuff','and you hate every single minute of it','- legally','to stop a meteorite','for world peace','with fire','with guns','until the universe explodes','until you die','until you\'re the last person alive','non-violently', 'to make memes',
'to shoot jews', 'to kill niggers', 'and niggers are still slaves', 'to commit sudoku', 'and the main character commits suicide at the end', 'and the main character is Averch', 'and the one to blame is Avrech', 'and Bentu makes memes behind you', 'and Kalish comes out of the closet', 'but you\'ve been a nigger all along']

def randomchoose(arr):
    return arr[random.randint(0, len(arr)-1)]

def sendToChat():
    sendstring = randomchoose(names) + ' where you ' + randomchoose(actions) + " " + randomchoose(things) + " " + randomchoose(goals)
    print(sendstring)
    return sendstring