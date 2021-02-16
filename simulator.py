from ships import Ship
from parts import PARTS, Part
from random import randint
from typing import Generator

"""Eclipse Combat Simulator
By: Wyko ter Haar

- Ask user for ships
- Put parts on ships
- Tally up the attribute totals 
- Sort the ships by Initiative
- Fire weapons for all ships of one initiative per player
- Determine the best available ship to hit (maybe by a threat ranking?)
- Remove any dead ships from the combat

"""

def generate_fake_ships(min_ships= 3, max_ships= 10) -> list:
    """Creates a list of randomly generated ships.

    Args:
        min_ships (int, optional): Minimum amount of ships to generate. 
        Defaults to 3.
        max_ships (int, optional): Maximum amount of ships to generate. 
        Defaults to 10.

    Returns:
        list: A list of ships with randomly generated parts and entry orders
    """   
    return [Ship.random() for _ in range(randint(min_ships, max_ships))]


def compile_results(results):
    raise NotImplementedError

def run_simulation(ships):
    
    while ships_alive(ships):
        # In initiative order, fire missiles
        for group in ships_in_initiative_order(ships, missiles_only=True):
            raise NotImplementedError

def fire_weapons(ships: list, missiles:bool = False) -> dict:
    """Takes a list of ships and fires all the weapons on them, returning a list
    of hits. The value of each hit is the die roll (ignoring ones) added to the
    total computer modifiers of the ship.

    Args:
        ships (list): The list of ships
        missiles (bool, optional): If Tru, fire only missiles. If False, fire 
        only non-missile weapons. Defaults to False.

    Returns:
        dict: The hits
    """    
    results= {
        'yellow_hits': [],
        'orange_hits': [],
        'blue_hits': [],
        'red_hits': [],
        'rift_3_hits': 0,
        'rift_2_hits': 0,
        'rift_1_hit': 0,
        'rift_self_hits': 0,
    }

    def _roll(dice, attack):
        """Roll a number of dice, omit any ones, and return the result as a 
        list with each hit having the computer modifier of the ship added to it.
        """
        return [d + attack for _ in range(dice) if (d := randint(1,6)) != 1]
          
    def _fire(color, ship, missiles=False):
        """Fire all weapons (or missiles) of a particular color and collect the 
        results of the attack in a list."""
        m_text = '_missiles' if missiles else ''
        results[f'{color}_hits'].extend(
            _roll(getattr(ship, f'total_{color}{m_text}'), ship.total_attack))

    def _fire_rift(dice):
        '''Fire rift cannons'''
        for _ in range(dice):
            if (d := randint(1,6)) > 2:
                # 1 and 2 are blank faces
                if d == 3: results['rift_self_hits'] += 1
                elif d == 4: results['rift_1_hit'] += 1
                elif d == 5: results['rift_2_hits'] += 1
                elif d == 5: results['rift_3_hits'] += 1
                elif d == 6: 
                    results['rift_3_hits'] += 1
                    results['rift_self_hits'] += 1
                
    # Fire each ships' weapons.
    for ship in ships:
        # Fire colored weapons and missiles
        for color in ['yellow', 'orange', 'blue', 'red']:
            _fire(color, ship, missiles=missiles)
        _fire_rift(ship.total_rifts)  # Fire rift cannons

    return results


def ships_in_initiative_order(
    ships: list, 
    missiles_only: bool= False) -> Generator[list, None, None]:
    """Iterate over all ships in a battle, yielded as a group by entry order in

    the hex and then by initiative. The result could look similar to:
    > [All ships from the defender, highest initiative]
    > [All ships from the next person to enter the hex, highest initiative]
    > [All ships from the defender, second highest initiative]
    ...etc

    This could have been done a fair bit more simply by using a single for loop,
    except that then this couldn't have been edited in place. This way of doing
    the generator makes it so that you can remove ships and not affect anything.

    Args:
        ships (list): The ordered list of all ships in a battle, resulting from
        the sort_ships() function.
        missiles_only (bool): If True, returns only ships that have missiles

    Yields:
        Iterator[list]: All ships of one initiative in hex entry order
    """
    # Get the highest initiative among ships
    highest_init = max(initiative for initiative in ships)
    
    # Get the participants in the battle
    entry_order = []
    for players in ships.values():
        for player in players.keys():
            if player not in entry_order:
                entry_order.append(player)
    
    # Get the last two combatants by entry order: last in, first to fight
    entry_order= sorted(entry_order)[-2:]

    # Yield the ships
    for current_init in range(highest_init, -1, -1):
        for current_player in entry_order:
            # Skip if a player has no ships at the current initiative
            if not ((current_init in ships) and
                    (current_player in ships[current_init])):
                continue
            if missiles_only:
                yield [s for s in ships[current_init][current_player] if
                    any((s.total_yellow_missiles, 
                        s.total_orange_missiles,
                        s.total_blue_missiles,
                        s.total_red_missiles,
                    ))]
            else:
                yield ships[current_init][current_player]



def ships_alive(ships: dict) -> bool:
    """Verifies if ships from more than one player are still alive

    Args:
        ships (dict): The organized dict of ships

    Returns:
        bool: True if two or more players' ships are still alive.
    """    
    players = {}
    for initiative in ships:
        for order in initiative:           
            for ship in order:
                if ship.alive: 
                    players[order] = True
    
    if len(players) > 1:
        return True
    else:
        return False

def ask_user_for_ships() -> list:
    raise NotImplementedError

def add_parts_to_ships(ships: list) -> list:
    raise NotImplementedError

def sort_ships(ships: list) -> dict:
    """Sorts ships into groups based on initiative and the order of entry into 
    the hex. The result will resemble this:
    {
        1: {       # Initiative
            1: [   # Entry order into the hex
                Ship1,
                Ship2,
            ]
            2: [
                Ship
            ]
        }
    } 

    Args:
        ships (list): The list of ships to organize

    Returns:
        dict: A dict of ships in entry order
    """    
    ordered_ships = {}

    # Orders by Initiative and then entry order, creating the relevant dict or
    # list if it doesn't already exist.
    for ship in ships:
        ordered_ships.setdefault(ship.total_initiative, {}
            ).setdefault(ship.order, []).append(ship)

    return ordered_ships

    
def main():
    results = list()
    
    # Set up the simulation
    # ships= ask_user_for_ships()
    # ships= add_parts_to_ships(ships)
    ships= generate_fake_ships()
    ships= sort_ships(ships)

    # Run the simulator
    for _ in range(9999):
        results.append(run_simulation(ships))

    # Deal with the results
    result= compile_results(results)
    print(result)

ships = generate_fake_ships()
ships = sort_ships(ships)
for group in ships_in_initiative_order(ships, missiles_only=False):
    print(fire_weapons(group))
# for x in ships_in_initiative_order(ships):
#     print(x)
