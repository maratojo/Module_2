# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: maratojo <maratojo@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/30 15:05:03 by maratojo        #+#    #+#               #
#  Updated: 2026/05/01 14:17:58 by maratojo        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        result = 10 / 0
        print(result)
    elif operation_number == 2:
        print(open("/non/existent/file"))
    elif operation_number == 3:
        "hello" + 10
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    i = 0
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught {type(e).__name__}: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
