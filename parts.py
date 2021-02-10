parts = {
    "ion cannon": {'damage': 1, 'energy': -1},  #
    "ion turret": {'damage': [1, 1], 'discovery': True},  #
    "ion disruptor": {'damage': 1, 'initiative': 3, 'discovery': True},  #
    "plasma cannon": {'damage': 2, 'energy': -2},  #
    "plasma turret": {'damage': [2, 2], 'energy': -3, 'discovery': True},  #
    "antimatter cannon": {'damage': 4, 'energy': -4},  #
    "soliton cannon": {'damage': 3, 'energy': -3},  #
    "soliton charger": {'damage': 3, 'discovery': True},  #
    "rift cannon": {'energy': -2},  #

    "flux missile": {'damage': [1, 1], 'initiative': 1, 'missile': True},  #
    "ion missile": {'damage': [1, 1, 1], 'missile': True, 'discovery': True},
    "plasma missile": {'damage': [2, 2], 'energy': -1, 'missile': True},  #
    "antimatter missile": {'damage': 4, 'missile': True, 'discovery': True},
    "soliton missile": {'damage': 3, 'missile': True, 'discovery': True},

    "electron computer": {'attack': 1},  #
    "positron computer": {'attack': 2, 'energy': -1},  #
    "gluon computer": {'attack': 3, 'energy': -2},  #

    "gauss shield": {'shield': 1},  #
    "phase shield": {'shield': 2, 'energy': -1},  #
    "absorption shield": {'shield': 1, 'energy': 4},  #
    "inversion shield": {'shield': 2, 'energy': 2, 'discovery': True},  #
    "flux shield": {'shield': 3, 'energy': -2, 'discovery': True},  #

    "nuclear source": {'energy': 3},  #
    "fusion source": {'energy': 6},  #
    "tachyon source": {'energy': 9},  #
    "zero-point source": {'energy': 12},  #
    "muon source": {'parts': -1, 'energy': 2, 'discovery': True},  # Special
    "hypergrid source": {'energy': 11, 'discovery': True},

    "hull": {'hull': 1},  #
    "improved hull": {'hull': 2},  #
    "shard hull": {'hull': 3, 'discovery': True},  #
    "sentient hull": {'hull': 1, 'attack': 1},  #
    "conifold field": {'hull': 3, 'energy': -2},  #

    "nuclear drive": {'initiative': 1, 'move': 1, 'energy': -1},  #
    "fusion drive": {'initiative': 2, 'move': 2, 'energy': -2},  #
    "tachyon drive": {'initiative': 3, 'move': 3, 'energy': -3},  #
    "transition drive": {'move': 3},  #
    "conformal drive": {'initiative': 2, 'move': 4, 'energy': -2, 'discovery': True},
    "nonlinear drive": {'move': 2, 'energy': 2, 'discovery': True},

    "axion computer": {'attack': 2, 'initiative': 1, 'discovery': True},
}
