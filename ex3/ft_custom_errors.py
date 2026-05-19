#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: maratojo <maratojo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/19 13:46:51 by maratojo            #+#    #+#            #
#   Updated: 2026/05/19 13:46:53 by maratojo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


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
    if nb <= 5:
        raise WaterError("Not enough water in the tank!")
    else:
        print("The tank is full")


def test() -> None:
    print("\nTesting PlantError...")
    try:
        Plant("tomato")
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}")

    print("\nTesting WaterError...")
    try:
        Water(5)
    except WaterError as e:
        print(f"Caught {type(e).__name__}: {e}")

    print("\nTesting catching all garden errors...")
    try:
        Plant("tomato")
    except GardenError as e:
        print(f"Caught {type(e).__name__}: {e}")

    try:
        Water(5)
    except GardenError as e:
        print(f"Caught {type(e).__name__}: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test()
    print("\nAll custom error types work correctly!")
