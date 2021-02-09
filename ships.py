PART_ATTRIBUTES = {
    'energy_usage': 0,
    'energy_production': 0,
    'initiative': 0,
    'hulls': 0,
    'drives': 0,
    'computers': 0,
    'shields': 0,
    'yellows': 0,
    'oranges': 0,
    'reds': 0,
    'missiles': 0,
}

class Part(object):

    def __init__(self, name, **kwargs):
        self.name = name

        for attribute, value in PART_ATTRIBUTES.items():
            if attribute in kwargs:
                value = kwargs[attribute]
            setattr(self, attribute, value)

SHIP_ATTRIBUTES = {
    'slots': 0,
    'quantity_limit': 0,
    'starbase': False,
    'parts': [],
}

class Ship(Part):

    def __init__(self, name, **kwargs):
        super(Ship, self).__init__(name, **kwargs)

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
            property_name = "total_%s" % attribute
            setattr(Ship, property_name,
                property(lambda x: attribute_total(x, attribute)))

        @property
        def is_valid(self):
            rules = [
                len(self.parts) <= self.slots,
                (not self.starbase and self.total_drives > 0) or self.starbase,
                self.total_energy_production >= self.total_energy_usage,
            ]
            return all(rules)

        def add_part(self, part):
            self.parts.append(part)
