"""
The 3d6 system is a role-playing system available under ORC license. This little script simulates
rolls to give you an idea of your chances of success.

For more informations about the role-playing system, please see: https://3d6.ovh/ and about ORC
License: https://paizo.com/orclicense
"""


def factorial(n: int):
    """Compute n factorial."""
    return 1 if n == 0 else n * factorial(n - 1)


def binomial_coeff(n: int, p: int):
    """Compute the binomial coefficient nCp."""
    return factorial(n) // (factorial(p) * factorial(n - p))


def binomial_distribution(success_probability: float, nb_experiences: int, nb_success: int):
    """
    Calculate the probability of having ``nb_success`` from ``nb_experiments`` Bernoulli
    experiments.

    Parameters
    ----------
    success_probability : float
        The probability of having a success. Must be between 0 and 1.
    nb_experiences : int
        The number of Bernoulli experiments that make up the binomial distribution.
    nb_success : int
        The number of success (should be less than the number of experiments).

    Returns
    -------
    float
        The probability of having ``nb_success``.

    Raises
    ------
    ValueError
        Raised if the requested number of successes is greater than the number of experiences.
    """
    if nb_success > nb_experiences:
        raise ValueError(
            f"the number of successes (given {nb_success}) must be less that the number of "
            f"experiments (given {nb_experiences})"
        )

    return (
        binomial_coeff(nb_experiences, nb_success)
        * success_probability**nb_success
        * (1 - success_probability) ** (nb_experiences - nb_success)
    )


def main():
    """Display the probabilities to have a given number of success, depending on the advantages."""
    for nb_dices, text in ((3, "Jeu normal"), (4, "Avec avantage"), (2, "Avec désavantage")):
        print(f"\t{text}\n\n")
        for attribute in range(1, 7):
            print(f"Attribut : {attribute}")
            for success in range(nb_dices + 1):
                print(
                    f"{success} réussites -> "
                    f"{binomial_distribution(attribute / 6, nb_dices, success) * 100:.2f} %"
                )
            print()
        print()


if __name__ == "__main__":
    main()
