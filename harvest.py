############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, pairings, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""


        self.code = new_code
        self.first_harvest = first_harvest
        self.color = color
        self.pairings = []
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings = self.pairings.append(pairing)
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

    all_melon_types.append(MelonType(muskmelon, "Muskmelon", "musk", 1998, "green", muskmelon.add_pairing("mint"), True, True)) 
    all_melon_types.append(MelonType(casaba, "Casaba", "cas", 2003, "orange", casaba.add_pairing("straberries", "mint"), False, False ))   
    all_melon_types.append(MelonType(crewnshaw, "Crenshaw", "cren", 1996, "green", crenshaw.add_pairing("prosciutto"), False, False))   
    all_melon_types.append(MelonType(yellow, "Yellow Watermelon", "yw", 2013, "yellow", yellow.add_pairing("ice cream"), False, True))
    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

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



