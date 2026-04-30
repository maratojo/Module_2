# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: maratojo <maratojo@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/29 13:39:56 by maratojo        #+#    #+#               #
#  Updated: 2026/04/30 14:15:08 by maratojo        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    test_case = ["25", "abc", "100", "-50"]
    for test in test_case:
        print(f"\nInput data is '{test}'")
        try:
            result = input_temperature(test)
            print(f"Temperature is now {result}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")

test_temperature()
