from random import randrange


class SimpleDie:
    """Basic class for YZE dice
    """
    def __init__(self, size=6):
        """Check size of the dice, 6 by default or 8, 10, 12. Return a dice
        object with a size attribute.
        """
        dice_sizes = [6, 8, 10, 12]
        d = [x for x in dice_sizes if x == size]
        if len(d) != 1:
            raise ValueError(f"Dice size should be one of 6, 8, 10, 12. {size} was provided.")
        self.size = size

    def throw(self):
        """Generate a pseudo-random number in the range of the SimpleDie
        Object. It returns an int.
        """
        return randrange(1, self.size + 1)


def main():
    """Do the magic
    """
    d = SimpleDie()
    print("""

 Jet normal :

    """)
    for i in range(1, 7):
        print(f"Attribut: {i}")
        total_successes = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            }
        for wow in range(1000000):
            successes = 0
            for j in range(1, 4):
                r = d.throw()
                if r <= i:
                    successes += 1
                    total_successes[successes] += 1
            if successes == 0:
                total_successes[0] += 1
            successes = 0
        print(f"0 réussites -> {total_successes[0] / 10000} %")
        print(f"1 réussites -> {total_successes[1] / 10000} %")
        print(f"2 réussites -> {total_successes[2] / 10000} %")
        print(f"3 réussites -> {total_successes[3] / 10000} %")

    print("""

 Avec avantage :
    
    """)
    for i in range(1, 7):
        print(f"Attribut: {i}")
        total_successes = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            }
        for wow in range(1000000):
            successes = 0
            for j in range(1, 5):
                r = d.throw()
                if r <= i:
                    successes += 1
                    total_successes[successes] += 1
            if successes == 0:
                total_successes[0] += 1
            successes = 0
        print(f"0 réussites -> {total_successes[0] / 10000} %")
        print(f"1 réussites -> {total_successes[1] / 10000} %")
        print(f"2 réussites -> {total_successes[2] / 10000} %")
        print(f"3 réussites -> {total_successes[3] / 10000} %")
        print(f"4 réussites -> {total_successes[4] / 10000} %")

    print("""

 Avec désavantage :
    
 """)
    for i in range(1, 7):
        print(f"Attribut: {i}")
        total_successes = {
            0: 0,
            1: 0,
            2: 0,
            }
        for wow in range(1000000):
            successes = 0
            for j in range(1, 3):
                r = d.throw()
                if r <= i:
                    successes += 1
                    total_successes[successes] += 1
            if successes == 0:
                total_successes[0] += 1
            successes = 0
        print(f"0 réussites -> {total_successes[0] / 10000} %")
        print(f"1 réussites -> {total_successes[1] / 10000} %")
        print(f"2 réussites -> {total_successes[2] / 10000} %")


if __name__ == "__main__":
    main()
