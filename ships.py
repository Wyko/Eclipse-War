from parts import Part, PART_ATTRIBUTES, PARTS
import uuid

SHIP_ATTRIBUTES = {
    'slots': 0,
    'quantity_limit': 0,
    'starbase': False,
    'damage_taken': 0,
    'alive': True,
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

    def reset_status(self):
        """Removes all damage taken and sets the status to Alive.
        """        
        self.damage_taken = 0
        self.alive = True

    def _set_name(self):
        """Generates a random UUID for the object.
        """        
        self.name = str(uuid.uuid4())
        return self.name


ion_cannon = Part(PARTS.ion_cannon)

interceptor = Ship()

print(interceptor.total_energy)

interceptor.add_part(ion_cannon)

print(interceptor.total_energy)