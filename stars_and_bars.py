import numpy as np
from itertools import combinations_with_replacement


def place_bars(raw_stars, raw_bar_locs):
    """
    Generates all possible bar placements in the 'Stars and Bars' Model by placing bars in available gaps
    :param raw_stars: A list representing the stars with gaps where stars are * and gaps are empty strings ''
    :param raw_bar_locs: A list of Lists containing all the variations of bar locations
    :return: A list of Lists containing all variations of bar placements
    """
    sb = []  # initializing list to hold bar placement variations
    stars_and_bars_item = raw_stars.copy()

    for item_p in raw_bar_locs:
        for sub_item in item_p:
            stars_and_bars_item[sub_item] = stars_and_bars_item[sub_item] + '|'

        sb.append(stars_and_bars_item)
        stars_and_bars_item = raw_stars.copy()

    return sb


def count_buckets(sb):
    """
    Generate the array representing the number of stars in each bucket of the current variation

    :param sb: A single stars and bars variation as a List
    :return: An array representing counts in each bucket
    """

    for sb_item in sb:  # Removing the gaps, not required once bars are placed
        if sb_item == '':
            sb.remove('')

    buckets = np.zeros(k)   # empty bucket to fill with counts
    bucket_pos = 0          # initializing index counter
    bucket_count = 0        # initializing counter

    for position in sb:
        if position == '*':
            bucket_count += 1
            buckets[bucket_pos] = bucket_count
        else:
            bars = len(position)
            bucket_pos += bars
            bucket_count = 0

    return buckets


n = 2  # what the non-negative integers must sum to
k = 3  # number of non-negative integers

stars = [''] + ['*', ''] * n    # represent the integer as string of stars with gaps

pos_bar_locs = range(0, 2*n+1, 2)  # locations of the gaps along the stars list

bar_locs = list(combinations_with_replacement(pos_bar_locs, r=k-1))  # set of all possible bar locations based on number
#                                                                   # of non-negative integers

stars_and_bars = place_bars(stars, bar_locs)  # Generate all variations of bar placements in gaps
print('\n')
print('Number of ways to write a number (n) as the sum of (k) non-negative integers.')
print('\n')
print(f'n: (number of stars *) = {n}')
print(f'k: (numbber of bars |) = {k}', '\n')

print(f'number of possible variations: {len(stars_and_bars)}', '\n')

label_sb = 'Stars and Bars'
label_bc = 'Bucket Counts'
print(f'{label_sb:{6*(n+k)}} {label_bc:{10}}')

bucket_count_list = []    # list to hold the individual bucket count variations

for item in stars_and_bars:
    current_bucket = count_buckets(item).astype('int')
    print(f'{str(item):{6*(n+k)}}', str(current_bucket))
    bucket_count_list.append(current_bucket)
