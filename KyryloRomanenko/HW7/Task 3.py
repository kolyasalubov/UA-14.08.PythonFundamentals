from typing import Dict


def letter_calculater() -> dict[str, int]:
    """
    input str and comeback dict with iformation how mach each letter
    :return: dict[str, int], print dict
    """
    result = {}
    string = input("Enter your text:")
    for item in string:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    print(result)
    return result


def main():
    letter_calculater()


if __name__ == "__main__":
    main()
