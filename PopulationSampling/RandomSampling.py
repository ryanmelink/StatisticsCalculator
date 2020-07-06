#Simple random sampling

import random


def random_sampling(series, itemsToReturn):
    return random.choices(series, k=itemsToReturn)