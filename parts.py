from enum import Enum

PART_ATTRIBUTES = {
    'energy': 0,
    'initiative': 0,
    'hull': 0,
    'move': 0,
    'attack': 0,
    'shield': 0,
    'yellows': 0,
    'oranges': 0,
    'blues': 0,
    'reds': 0,
    'yellow_missiles': 0,
    'orange_missiles': 0,
    'blue_missiles': 0,
    'red_missiles': 0,
    'rifts': 0,
    'slots_used': 1,
}

class PARTS(Enum):
    ion_cannon = {'name': 'Ion Cannon', 'yellows': 1, 'energy': -1}
    ion_turret = {'name': 'Ion Turret', 'yellows': 2, 'discovery': True}
    ion_disruptor = {'name': 'Ion Disruptor', 'yellows': 1, 'initiative': 3, 'discovery': True}
    plasma_cannon = {'name': 'Plasma Cannon', 'oranges': 1, 'energy': -2}
    plasma_turret = {'name': 'Plasma Turret', 'oranges': 2, 'energy': -3, 'discovery': True}
    soliton_cannon = {'name': 'Soliton Cannon', 'blues': 1, 'energy': -3}
    soliton_charger = {'name': 'Soliton Charger', 'blues': 1, 'discovery': True}
    antimatter_cannon = {'name': 'Antimatter Cannon', 'reds': 1, 'energy': -4}
    rift_cannon = {'name': 'Rift Cannon', 'rifts': 1, 'energy': -2} # We have to make special rules for this guy

    flux_missile = {'name': 'Flux Missile', 'yellow_missiles': 2, 'initiative': 1, 'missile': True}
    ion_missile = {'name': 'Ion Missile', 'yellow_missiles': 3, 'missile': True, 'discovery': True}
    plasma_missile = {'name': 'Plasma Missile', 'orange_missiles': 2, 'energy': -1, 'missile': True}
    antimatter_missile = {'name': 'Antimatter Missile', 'red_missiles': 1, 'missile': True, 'discovery': True}
    soliton_missile = {'name': 'Soliton Missile', 'blue_missiles': 1, 'missile': True, 'discovery': True}

    electron_computer = {'name': 'Electron Computer', 'attack': 1}
    positron_computer = {'name': 'Positron Computer', 'attack': 2, 'energy': -1}
    gluon_computer = {'name': 'Gluon Computer', 'attack': 3, 'energy': -2}
    axion_computer = {'name': 'Axion Computer', 'attack': 2, 'initiative': 1, 'discovery': True}

    gauss_shield = {'name': 'Gauss Shield', 'shield': 1}
    phase_shield = {'name': 'Phase Shield', 'shield': 2, 'energy': -1}
    absorption_shield = {'name': 'Absorption Shield', 'shield': 1, 'energy': 4}
    inversion_shield = {'name': 'Inversion Shield', 'shield': 2, 'energy': 2, 'discovery': True}
    flux_shield = {'name': 'Flux Shield', 'shield': 3, 'energy': -2, 'discovery': True}

    # Muon Source is special in that it sits outside the ship.
    muon_source = {'name': 'Muon Source', 'slots_used': 0, 'energy': 2, 'discovery': True}
    nuclear_source = {'name': 'Nuclear Source', 'energy': 3}
    fusion_source = {'name': 'Fusion Source', 'energy': 6}
    tachyon_source = {'name': 'Tachyon Source', 'energy': 9}
    zero_point_source = {'name': 'Zero-Point Source', 'energy': 12}
    hypergrid_source = {'name': 'Hypergrid Source', 'energy': 11, 'discovery': True}

    hull = {'name': 'Hull', 'hull': 1}
    improved_hull = {'name': 'Improved Hull', 'hull': 2}
    shard_hull = {'name': 'Shard Hull', 'hull': 3, 'discovery': True}
    sentient_hull = {'name': 'Sentient Hull', 'hull': 1, 'attack': 1}
    conifold_field = {'name': 'Conifold Field', 'hull': 3, 'energy': -2}

    nuclear_drive = {'name': 'Nuclear Drive', 'initiative': 1, 'move': 1, 'energy': -1}
    fusion_drive = {'name': 'Fusion Drive', 'initiative': 2, 'move': 2, 'energy': -2}
    tachyon_drive = {'name': 'Tachyon Drive', 'initiative': 3, 'move': 3, 'energy': -3}
    transition_drive = {'name': 'Transition Drive', 'move': 3}
    conformal_drive = {'name': 'Conformal Drive', 'initiative': 2, 'move': 4, 'energy': -2, 'discovery': True}
    nonlinear_drive = {'name': 'Nonlinear Drive', 'move': 2, 'energy': 2, 'discovery': True}

class Part():

    def __init__(self, part):
        # Unpack the part
        if isinstance(part, Enum):
            part = part.value
        
        self.name = part['name']

        for attribute, value in PART_ATTRIBUTES.items():
            if attribute in part:
                value = part[attribute]
            setattr(self, attribute, value)