# Live Coding 2023-03-15
def lyric(activity):
    line_end = "doo-doo, "*3
    line_end = line_end[:-2]
    for lyric_line in range(0, 3):
        print(f"{activity}, {line_end}")
    print(f"{activity}")
    print()

def baby_shark():
    lyric("Baby Shark")


def mommy_shark():
    lyric("Mommy Shark")


def daddy_shark():
    print("Daddy Shark, doo-doo, doo-doo")
    print("Daddy Shark, doo-doo, doo-doo")
    print("Daddy Shark, doo-doo, doo-doo")
    print("Daddy Shark")
    print()


def grandma_shark():
    print("Grandma Shark, doo-doo, doo-doo")
    print("Grandma Shark, doo-doo, doo-doo")
    print("Grandma Shark, doo-doo, doo-doo")
    print("Grandma Shark")
    print()


def grandad_shark():
    print("Grandpa Shark, doo-doo, doo-doo")
    print("Grandpa Shark, doo-doo, doo-doo")
    print("Grandpa Shark, doo-doo, doo-doo")
    print("Grandpa Shark")
    print()


def hunting_shark():
    print("Let's go hunt, doo-doo, doo-doo")
    print("Let's go hunt, doo-doo, doo-doo")
    print("Let's go hunt, doo-doo, doo-doo")
    print("Let's go hunt")
    print()


def run_away_shark():
    print("Run away, doo-doo, doo-doo")
    print("Run away, doo-doo, doo-doo")
    print("Run away, doo-doo, doo-doo")
    print("Run away (ah!)")
    print()


def safe_shark():
    print("Safe at last, doo-doo, doo-doo")
    print("Safe at last, doo-doo, doo-doo")
    print("Safe at last, doo-doo, doo-doo")
    print("Safe at last (phew)")
    print()


def end_shark():
    print("It's the end, doo-doo, doo-doo")
    print("It's the end, doo-doo, doo-doo")
    print("It's the end, doo-doo, doo-doo")
    print("It's the end")
    print()


def sing_along():
    baby_shark()
    mommy_shark()
    # daddy_shark()
    # grandma_shark()
    # grandad_shark()
    # hunting_shark()
    # run_away_shark()
    # safe_shark()
    # end_shark()


if __name__ == "__main__":
    sing_along()
