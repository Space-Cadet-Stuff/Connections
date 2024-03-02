import random

# Defines the Categories
categories = {
    'Metalcore Bands': ['Architects','Currents','Volumes','Imminence'],
    'Sith Lords (Darth______)': ['Sion','Tenebrae','Kreia','Bane'],
    'Rockets':['Titan','Ariane','Antares','Saturn'],
    'STARSET Albums': ['Transmissions','Vessels','Horizons','Divisions'],
    'Characters in Greek Mythology': ['Prometheus','Hercules','Ares','Alecto'],
    'Creature in a Horror movie name, Silence of the LAMBS, The Human CENTIPEDE, ALIEN, BIRD Box': ['Lambs','Centipede','Alien','Bird'],
    'Incects': ['Grasshopper','Bee','Wasp','Spitfire'],
    'US Aircraft': ['Thunderbolt','Blackbird','Lightning','Raider'],
    'Bird Species': ['Wren','Sparrow','Owl','Emu'],
    'Aliens': ['Calvin','Yautja','Hutt','Whitespike'],
    'Australian Icons': ['Kangaroo','Boomerang','Aukubra','Uluru'],
    'Computer Games': ['Portal','Rust','Doom','Stray'],
    'Polyatomic Anions': ['Sulphate','Oxide','Fluoride','Chlorine'],
    'Extraterrestrial Mountain Ranges, ______ Montes': ['Caloris','Mithrim','Tenzing','Taurus'],
    'Probes to Saturn': ['Voyager','Cassini','Pioneer','Huygens'],
    'Cheese': ['Swiss','Cottage','Cream','Blue'],
    'Musician Nicknames': ['Sting','Slash','Flea','Bonzo'],
    'Fish Species': ["Bass","Pike","Shad","Snook"],
    'Alice In Chains Songs': ["Would","Nutshell","Hollow","Rooster"],
    'Haggis Ingredients': ["Pluck","Oatmeal","Onions","Suet"]
}

max_length = max(len(word) for words in categories.values() for word in words)

grid = []
for _ in range(4):
    category = random.choice(list(categories.keys()))
    words = categories[category]
    grid.append([word.center(max_length) for word in words])

# Print the grid
for row in grid:
    print("|".join(row))