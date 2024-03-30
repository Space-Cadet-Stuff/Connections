import random# Imports the random library allowing for random selection
from time import sleep# Imports the sleep function from the time module, allowing for timed pauses in the command line
import webbrowser# Imports the webbrowser library, letting the game open links in your broswer

categories = {# Defines the Categories
    "Metalcore Bands": ["Architects","Currents","Volumes","Imminence"],# "Category": ["Word 1","Word 2","Word 3","Word 4"]
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
    "Palindromes": ["Racecar","Refer","Rotator","Deified"],
    "Navigation Instruments": ["Sextant","Radar","Compass","Chronometer"],
    "Constellations": ["Starlink","Orion","Saggitarius","Ursa"],
    "Fire Types": ["Electrical","Oil","Grease","Liquid"],
    "Aqua_______": ["Regia","tic","Marine","rium"],
    "Kerbal Manufacturers": ["Kerbodyne","Probodobodyne","Rockomax","C7"],
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
    "Nu Metal Bands": ["Skillet","Korn","Disturbed","Slipknot"],
    "Aircraft Companies": ["Lockheed","Sukhoi","Boeing","Airbus"],
    "Plastic Explosives": ["C4","Semtex","Seismoplast","Plastrite"],
    "Transition Metals": ["Iron","Nickel","Silver","Gold"],
    "Alloys": ["Brass","Bronze","Solder","Pewter"],
    "Lightsaber Combat Forms": ["Ataru","Shien","Makashi","Soresu"],
}
grid = []# Creates an empty list to be used later
lives = 4# Sets the amount of lives for later on
def chooseWords():# Chooses the words to make the grid
    random_keys = random.sample(list(categories.keys()), 4)# Select 4 random keys

    selected_words = []# Create an array to store lists of words for each selected category

    all_words = []# Create a list to store all words in the selected categories

    for key in random_keys:# Iterate over the selected keys and extract the corresponding lists of words
        selected_words.append(categories[key])# Adds the selected categories to a list called selected_words
        all_words.extend(categories[key])# adds the words in the categories to a large list for generating the grid

    random.shuffle(all_words)# Randomize the order of all words
    return selected_words, all_words# Returns the selected categories and list of all words for later use

def makeGrid(all_words):# Generates the grid for the printGrid function
    max_length = max(len(word) for words in categories.values() for word in words)# Finds the length of the largest word in the dictionary
    for word in range(4):# Iterates over each row in the grid
        row = []# Creates an empty list to store words for the current row
        for word in range(4):# Iterates over each word in the current row
            row.append(all_words.pop(random.randint(0, len(all_words)-1)))# Remove a random word from the list of all words and append it to the current row
        grid.append(row)# Adds the completed row to the grid
    return grid, max_length# Returns the completed grid and the maximum length of words

def printGrid():# Prints the grid out in the command line and adds breaks to the words to give a boxed look to it
    selected_words, all_words = chooseWords()# Calls the chooseWords function to select random categories and words
    grid, max_length = makeGrid(all_words)# Calls the makeGrid function to create the grid using the selected words
    
    for words_list in selected_words:# Iterates for each array
        print(words_list)# Prints one of the word lists in the array

    print("---------------------------------------------------------")# Prints a horizontal line to separate the grid on the first line
    for row in grid:# Iterates over each row in the grid
        print("|"+"|".join([word.center(max_length) for word in row])+"|")# Prints a Divider between each word and centers each word while making the box the max length, creating a uniform grid
        print("---------------------------------------------------------")# Prints a horizontal line to seperate each 

def getGuess():# Takes and logs the players guess
    guesses = []#Creates an empty array to store the guesses
    for i in range(4):# Iterates over loop 4 times
        guess = input("Enter Guesses ")# Asks for user input
        guesses.append(guess)# Adds user input to the guesses array
    return guesses# Returns the player guesses for later
printGrid()