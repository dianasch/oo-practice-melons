############
# Part 1   #
############

#git
class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, name, code, first_harvest, color, pairings, is_seedless, is_bestseller):
        """Initialize a melon."""

        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.pairings = []
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        for item in pairing:
            self.pairings.append(item)
        
        return self.pairings

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        return self.code
        # Fill in the rest





def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("Muskmelon", "musk", 1998, "green", [], True, True)
    casaba = MelonType("Casaba", "cas", 2003, "orange", [], False, False)
    crenshaw = MelonType("Crenshaw", "cren", 1996, "green", [], False, False)
    yellow = MelonType("Yellow Watermelon", "yw", 2013, "yellow", [], False, True)

    muskmelon.add_pairing = ["mint"]
    casaba.add_pairing = ["mint", "strawberries"]
    crenshaw.add_pairing = ["proscuitto"]
    yellow.add_pairing = ["ice cream"]

    all_melon_types.append(muskmelon)
    all_melon_types.append(casaba)
    all_melon_types.append(crenshaw)
    all_melon_types.append(yellow)
    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""



    for melon in make_melon_types():

        name = melon.name

        pairing = melon.add_pairing

        for item in pairing:

            print(f"""{name} pairs with:
            -{item}""")
        


    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



