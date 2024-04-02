
import random
from time import sleep
import webbrowser

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
grid = []
lives = 4
def chooseWords():
    random_keys = random.sample(list(categories.keys()), 4)

    selected_words = []

    all_words = []

    for key in random_keys:
        selected_words.append(categories[key])
        all_words.extend(categories[key])

    random.shuffle(all_words)
    return selected_words, all_words

def makeGrid(all_words):
    max_length = max(len(word) for words in categories.values() for word in words)
    for word in range(4):
        row = []
        for word in range(4):
            row.append(all_words.pop(random.randint(0, len(all_words)-1)))
        grid.append(row)
    return grid, max_length

def printGrid(all_words, selected_words):
    selected_words, all_words = chooseWords()
    grid, max_length = makeGrid(all_words)
    
    for words_list in selected_words:
        print(words_list)

    for row in grid:
        print("---------------------------------------------------------")
        print("|"+"|".join([word.center(max_length) for word in row])+"|")
        print("---------------------------------------------------------")

def getGuesses(all_words):
    print("Words to choose from: ", all_words)
    guesses = []
    while len(guesses) < 4:
        guess = input("Enter a word: ")
        if guess in all_words:
            guesses.append(guess)
            print("Guesses: ",guesses)
        else:   
            print("Invalid word. Please try again.")
    return guesses


selected_words, all_words = chooseWords()
printGrid(all_words, selected_words)
getGuesses(all_words)