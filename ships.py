from parts import Part, PART_ATTRIBUTES, PARTS
from random import randint
import uuid

SHIP_ATTRIBUTES = {
    'slots': 0,
    'quantity_limit': 0,
    'starbase': False,
    'damage_taken': 0,
    'order': 0, # 1 is defender, every subsequent player in the hex
                # is a higher number
    'owner': None,
    'type': None,
    'parts': [],
}


class Ship(Part):

    def __init__(self, **kwargs):
        self._set_name()
        
        # Assign part attributes to the ship to permit manual modification of
        # attributes. These "ship-part" attributes will be added to the sum of
        # any part attributes to find the final totals
        for attribute, value in PART_ATTRIBUTES.items():
            setattr(self, attribute, value)
            self.slots_used = 0

        # Assign the default ship attributes
        for attribute, value in SHIP_ATTRIBUTES.items():
            if attribute in kwargs:
                value = kwargs[attribute]
            setattr(self, attribute, value)

        def attribute_total(self, attribute_name):
            """A lambda function used to calculate (in real-time) the sum of
            one attribute of the the parts on a ship.

            Args:
                attribute_name (str): The name of the atibute to sum.

            Returns:
                int: The sum of the attribute on all parts on the ship.
            """            
            # Get any manually added modifiers to the ship
            total = getattr(self, attribute_name, 0)

            # Sum up the attributes on the parts on the ship
            for part in self.parts:
                total += getattr(part, attribute_name, 0)

            return total

        for attribute, value in PART_ATTRIBUTES.items():
            setattr(Ship, f"total_{attribute}", property(
                lambda x, attribute=attribute: attribute_total(x, attribute)))


    def __repr__(self):
        return f"Order: {self.order}, Init: {self.total_initiative}, " \
            f"Parts: {self.parts}"

    @classmethod
    def random(cls, min_parts= 1, max_parts= 6, drive= True, weapon= True):
        """Creates a randomly generated ship, containing at least one engine and
        between 1 and 7 other parts.

        Args:
            min_parts (int, optional): Minimum amount of parts to add to the 
            ship. Defaults to 1.
            max_parts (int, optional):  Maximum amount of parts to add to the 
            ship. Defaults to 8.
            drive (bool, optional): Add a random drive to the ship. This is in 
            addition to the random parts added to the ship, which may themselves
            include other drives. This is not affected by the min or max parts
            arguments. Defaults to True.

        Returns:
            ship: A randomly generated ship
        """
        part_list = [Part(PARTS.random()) for _ in range(
            randint(min_parts, max_parts))]
        
        if drive:
            part_list.append(Part(PARTS.random_drive()))
        
        if weapon:
            part_list.append(Part(PARTS.random_cannon()))
            part_list.append(Part(PARTS.rift_cannon))
        
        return Ship(
            order= randint(1,4),
            parts= part_list
        )

    @property
    def hp(self):
        """Gets the total hitpoints of the ship (base 1 plus any hull) and
        subtracts any damage taken so far. If the result is less than zero,
        return zero.

        Returns:
            int: The total hit points of the ship
        """
        return max(0, (self.total_hull + 1 - self.damage_taken))

    @property
    def is_valid(self):
        rules = [
            len(self.parts) <= self.slots,
            (not self.starbase and self.total_move > 0) or self.starbase,
            self.total_energy >= 0,
        ]
        return all(rules)

    def add_part(self, part):
        self.parts.append(part)

    @property
    def alive(self):
        return self.hp > 0

    def reset(self):
        """Removes all damage taken.
        """        
        self.damage_taken = 0

    def _set_name(self):
        """Generates a random UUID for the object.
        """        
        self.name = str(uuid.uuid4())
        return self.name
