import uuid




SHIP_ATTRIBUTES = {
    'slots': 0,
    'quantity_limit': 0,
    'starbase': False,
    'damage_taken': 0,
    'alive': True,
    'parts': [],
}


class Ship():

    def __init__(self, **kwargs):
        self._set_name()
        
        # super(Ship, self).__init__(self.name, **kwargs)

        for attribute, value in SHIP_ATTRIBUTES.items():
            if attribute in kwargs:
                value = kwargs[attribute]
            setattr(self, attribute, value)

        def attribute_total(self, attribute_name):
            total = getattr(self, attribute_name, 0)
            for part in self.parts:
                total += getattr(part, attribute_name, 0)
            return total

        for attribute, value in PART_ATTRIBUTES.items():
            setattr(Ship, f"total_{attribute}",
                    property(lambda x: attribute_total(x, attribute)))

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


interceptor = Ship()

print(interceptor.total_energy)