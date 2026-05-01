# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: maratojo <maratojo@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/01 14:20:06 by maratojo        #+#    #+#               #
#  Updated: 2026/05/01 16:54:56 by maratojo        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def Plant(plant_name: str) -> None:
    raise PlantError(f"The {plant_name} plant is wilting")

def Water(nb: int) -> None:
    raise WaterError("Not enough water in the tank!")

def test() -> None:

    tests = [(Plant, "tomato", PlantError), (Water,0, WaterError)]
    for (name, arg, error) in tests:
        print(f"\nTesting {error.__name__}...")
        try:
            fun(other)
        except error as e:
            print(f"Caught {type(e).__name__}: {e}")

    print("\nTesting catching all garden errors...")
    for name, arg, error in tests:
        try:
            name(arg)
        except error as e:
            print(f"Caught {type(e).__name__}: {e}")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test()
    print("\nAll custom error types work correctly!")



