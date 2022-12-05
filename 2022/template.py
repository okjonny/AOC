import argparse
import os
import requests
import sys

year = os.path.split(os.path.dirname(__file__))[-1]
day = os.path.splitext(os.path.basename(__file__))[0]


def part_1() -> int:
    input = open(os.path.join(os.path.dirname(__file__), f"{day}.txt")).read()

    return 0


def part_2() -> int:
    input = open(os.path.join(os.path.dirname(__file__), f"{day}.txt")).read()

    return 0


def cookie() -> str:
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")) as env:
        return env.read().strip()


def get(year: int, day: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    return requests.get(url, cookies={"session": cookie()}).text


def submit(year: int, day: int, part: int, answer: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    return requests.post(url, cookies={"session": cookie()}, data={"level": part, "answer": answer}).text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("part", type=int)
    args = parser.parse_args(args=None if sys.argv[1:] else ["--help"])

    if not os.path.exists(os.path.join(os.path.dirname(__file__), f"{day}.txt")):
        with open(os.path.join(os.path.dirname(__file__), f"{day}.txt"), "w") as f:
            f.write(get(int(year), int(day)))

    if args.part == 1:
        answer = part_1()
    elif args.part == 2:
        answer = part_2()
    else:
        raise ValueError(f"unknown part {args.part}")

    confirm = input(f"AoC {int(year)} Day {int(day)} Part {args.part}: {answer}\n"
                    f"Submit? [y/n]\n"
                    f"> ")

    if confirm.lower() == "y":
        res = submit(int(year), int(day), args.part, answer)
        if "That's the right answer!" in res:
            print("Correct!")
        elif "You gave an answer too recently." in res:
            print("Wait a bit before submitting again.")
        elif "That's not the right answer." in res:
            print("Incorrect, try again.")
        elif "Did you already complete it?" in res:
            print("Already completed.")
        else:
            print(res)
    elif confirm.lower() == "n":
        print("Canceled.")
    else:
        raise ValueError(f"unknown confirmation {confirm}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
