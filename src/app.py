def parse_input(input_str: str) -> list[int] | None:
    tokens = input_str.split()
    try:
        return [int(token) for token in tokens]
    except Exception:
        print("Could not parse input. Only integers allowed.")
        return None


if __name__ == "__main__":
    while user_input := input():
        if numbers := parse_input(user_input):
            numbers.sort()
            result = " ".join(str(number * number) for number in numbers)
            print(result)
