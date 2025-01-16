def parse_integers_from_string(input_str: str) -> list[int] | None:
    tokens = input_str.split()
    try:
        if tokens:
            return [int(token) for token in tokens]
        else:
            return None
    except Exception:
        print("Could not parse input. Only integers allowed.")
        return None


def process_list(integers: list[int]) -> list[int]:
    return [integer * integer for integer in sorted(integers)]


def run_app():
    while user_input := input():
        if numbers := parse_integers_from_string(user_input):
            result = process_list(numbers)
            print(" ".join(str(element) for element in result))


if __name__ == "__main__":
    run_app()
