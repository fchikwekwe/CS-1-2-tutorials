import random
import dict_histogram_maker

# code comes from @DacioRomero's method

def histogram_sample(histogram):
    weighted_sample = random_choice(zip(histogram.items()))
    return weighted_sample

def histogram_samples(histogram, k=1):
    """returns a random, weighted sample from a histogram"""
    weighted_sample = random_choices(zip(histogram.items()), k=k)
    return weighted_sample

def random_choices(sequence, weights=None, cumulative_weights=None, k=1):
    cumulative_weights = convert_weights(weights)

    return [random_choice(sequence, cumulative_weights=cumulative_weights) for _ in range(k)]

def random_choice(sequence, weights=None, cumulative_weights=None):
    equal_len_err = ValueError('all provided iterables must be equal length')
    # convert weights to cumulative weights
    if weights is not None:
        # make sure that they are the same length
        if len(sequence) != len(weights):
            raise equal_len_err
        cumulative_weights = convert_weights(weights)

    elif cumulative_weights is not None:
        if len(sequence) != len(cumulative_weights):
            raise equal_len_err

    choice = None

    # choose completely randomly if no weights given
    if cumulative_weights is None:
        choice = random.choice(sequence)
    else:
        max_weight = cumulative_weights[-1]
        sample = random.random() * max_weight # [0, max_weight]

        if sample < 0 or sample >= max_weight:
            raise ValueError('sample generated out of range')

        # Loop over the sequence and cumulative weights together
        for item, cumulative_weight in zip(sequence, cumulative_weights):
            # sample is in the range of this weight
            if sample < cumulative_weight:
                choice = item
                break
    return choice

def convert_weights(weights):
    cumulative_weights = []
    current_total = 0

    for weight in weights:
        current_total += weight
        cumulative_weights.append(current_total)

    return cumulative_weights

if __name__ in '__main__':
    text = "And the Raven, never flitting, still is sitting, still is sitting"
    histogram = dict_histogram_maker.histogram(' '.join(text))
    samples = histogram_samples(histogram, k=100000)
    print(dict_histogram_maker.histogram(samples))
