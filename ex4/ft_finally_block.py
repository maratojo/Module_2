# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: maratojo <maratojo@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/02 08:17:07 by maratojo        #+#    #+#               #
#  Updated: 2026/05/02 08:21:20 by maratojo        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Opening watering system")
    plants = ["tomato", "lettuce", "Carrots"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
