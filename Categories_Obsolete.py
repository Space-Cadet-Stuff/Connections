import random

# defines the Categories
categories = {
    "Metalcore Bands": ["Architects","Currents","Volumes","Imminence"],
    "Sith Lords (Darth______)": ["Sion","Tenebrae","Kreia","Bane"],
    "Rockets":["Titan","Ariane","Antares","Saturn"],
    "STARSET Albums": ["Transmissions","Vessels","Horizons","Divisions"],
    "Characters in Greek Mythology": ["Prometheus","Hercules","Ares","Alecto"],
    "Creature in a Horror movie name, Silence of the LAMBS, The Human CENTIPEDE, ALIEN, BIRD Box": ["Lambs","Centipede","Alien","Bird"],
    "Incects": ["Grasshopper","Bee","Wasp","Spitfire"],
    "US Aircraft": ["Thunderbolt","Blackbird","Lightning","Raider"],
    "Bird Species": ["Wren","Sparrow","Owl","Emu"],
    "Aliens": ["Calvin","Yautja","Hutt","Whitespike"],
    "Australian Icons": ["Kangaroo","Boomerang","Aukubra","Uluru"],
    "Computer Games": ["Portal","Rust","Doom","Stray"],
    "Polyatomic Anions": ["Sulphate","Oxide","Fluoride","Chloride"],
    "Extraterrestrial Mountain Ranges, ______ Montes": ["Caloris","Mithrim","Tenzing","Taurus"],
    "Probes to Saturn": ["Voyager","Cassini","Pioneer","Huygens"],
    "Cheese": ["Swiss","Cottage","Cream","Blue"],
    "Musician Nicknames": ["Sting","Slash","Flea","Bonzo"],
    "Fish Species": ["Bass","Pike","Shad","Snook"],
    "Alice In Chains Songs": ["Would","Nutshell","Hollow","Rooster"],
    "Haggis Ingredients": ["Pluck","Oatmeal","Onions","Suet"],
    "Guitar Brands": ["Ibanez","Gibson","Jackson","Fender"],
    "Verb in the name of a Star Wars movie": ["Attack", "Return", "Revenge","Awaken"],
    "Famous Scientists": ["Tesla","Eddison","Curie","Newton"],
    "Songs starting with 'S' from System of a Down's self titled Album": ["Spiders","Sugar","Suggestions","Soil"],
    "First four lightsaber colours seen in Star Wars": ["Green","Blue","Red","Purple"],
    "Multi Bladed Lightsaber Variants": ["Rotary", "Saberstaff", "Crossguard ", "Folding"],
    "Lunar Oceans": ["Tranquility","Serenity","Showers","Crises"],
    "Martian Rovers": ["Curiosity","Opportunity","Perseverance","Spirit"],
    "Industrial Metal Artists": ["Zombie","Manson","Landers","Reznor"],
    "Palindromes": ["Racecar","Refer","Rotator","Defied"],
    "Navigation Instruments": ["Sextant","Radar","Compass","Chronometer"],
    "Constellations": ["Starlink","Orion","Saggitarius","Ursa"],
    "Fire Types": ["Electrical","Oil","Grease","Liquid"],
    "Aqua_______": ["Regia","tic","Marine","rium"],
    "Best Teachers at Saint Augustines": ["Goodrick","","",""],
    "Lost Civilizations": ["Maya","Khmer","Harappan","Çatalhöyük"],
    "Egyprian Gods": ["Horus","Osiris","Set","Thoth"],
    "Terrorist Organizations": ["Isis","Hamas","Al-Quaeda","KKK"],
    "Moons of Saturn": ["Ipaetus","Titan","Mimas","Enceladus"],
    "Galilean Moons": ["Ganymede","Europa","Io","Callisto"],
    "Nebulae": ["Helix","Orion","Carina","Veil"],
    "Seas": ["Caribbean","Adriatic","Mediterranean","Tasman"],
    "Best Teachers at Saints 👍": ["Pollard","Oates","Laforest","Egger"],
    "Shipwrecks": ["Titanic","Endurance","Bismarck","Victory"],
    "Large Manmade Non-Nuclear Explosions": ["Hindenburg","N1","Beirut","Blowdown"],
    "Nu Metal Bands": ["POD","Korn","Disturbed","Slipknot"],
    "Aircraft Companies": ["Lockheed","Sukhoi","Boeing","Airbus"],
    "Kerbal Manufacturers": ["Kerbodyne","","",""],
    "": ["","","",""],
    "": ["","","",""],
    "": ["","","",""],
}

def printGrid(grid):# Prints the grid of words from the chosen categories, randomises the word placement and adds dividing lines
    print("---------------------------------------------------------")
    for row in grid:
        print("|"+"|".join([word.center(max_length) for word in row])+"|")
        print("---------------------------------------------------------")

def checkGuess(guesses):
    for category in chosen_categories:
        valid = True
        for word in category:
            if word not in guesses:
                valid = False
    # clue for josh
    # get the four words
    # put them in an array
    # you need to refer to the original 4 categories
    # the dictionaries themselves and specifically the word lists inside of them
    # e.g.
    # loop through each of the word key fields in the dictionaries
    # there is a python way of comparing the contents of two list
    # for each dictionary in your dictionaries
    # compare the contents of the guessed words against their word lists
    # if any match, you know its a win

def getGuess():# Takes and logs the players guess
    guesses = []
    for i in range(4):
        guess = input("Enter Guesses ")
        guesses.append(guess)
    return guesses
    checkguess()

                
    # clue for josh
    # get the four words
    # put them in an array
    # you need to refer to the original 4 categories
    # the dictionaries themselves and specifically the word lists inside of them
    # e.g.
    # loop through each of the word key fields in the dictionaries
    # there is a python way of comparing the contents of two list
    # for each dictionary in your dictionaries
    # compare the contents of the guessed words against their word lists
    # if any match, you know its a win

def pickCategories(chosen_categories):
    # while len(chosen_categories) < 4:#Picks 4 random categories
    #     random_choice = random.choice(list(categories.keys()))
    #     if random_choice not in list(chosen_categories.keys()):
    #         chosen_categories[random_choice] = categories[random_choice]
    random_keys = random.sample(categories.keys(), 4)
    print("Random keys:", random_keys)


    return chosen_categories

def createBigListOfAllWords(chosen_categories):
    category_words=[word for words in chosen_categories for word in chosen_categories[words]]
    return category_words

def makePrettyGrid(category_words):
    max_length = max(len(word) for words in categories.values() for word in words)#Finds length of longest word to set box widths in the grid

    for word in range(4):
        row = []
        for word in range(4):
            row.append(category_words.pop(random.randint(0, len(category_words)-1)))
        grid.append(row)
    return grid

# mainline 
    
grid = []
row = []
lives = 4

chosen_categories = pickCategories(categories) # needs to return 4 keys to be used throughout the game
# gird = makePrettyGrid(category_words)

# get guess
# loop that happens 4 times, gets four words and puts in a list e.g. [1,2,3,4]
# return that back to mainline guess = getguess()
# feed the guess into a checkguess function that takes the list of guess words AND, 4 original keys chosen categories 
    
# lists not in oder cannot be matched against each other, even if they contain the same words
# convert both into SETS in python, then compare 


pickCategories()


