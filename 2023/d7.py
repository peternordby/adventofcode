import re

from utils import fetch_input


def read_input(TEST=0):
    filename = f"{__file__.split('.')[0]}{['', 'x1', 'x2'][TEST]}.txt"
    with open(filename) as f:
        puzzle = f.readlines()
    return puzzle

def hand_strength(hand):
    # Count the occurence of each card
    counts = {}
    [counts.update({card: counts.get(card, 0) + 1}) for card in hand]

    # Five of a kind
    if 5 in counts.values():
        return 7

    # Four of a kind
    if 4 in counts.values():
        return 6

    # Full house
    if 3 in counts.values() and 2 in counts.values():
        return 5

    # Three of a kind
    if 3 in counts.values() and 2 not in counts.values():
        return 4

    # Two pair
    if list(counts.values()).count(2) == 2:
        return 3

    # One pair
    if 2 in counts.values() and list(counts.values()).count(1) == 3:
        return 2

    # High card
    if list(counts.values()).count(1) == 5:
        return 1
    
def hand_strength_2(hand):
    # Count the occurence of each card
    # J can be whatever

    best_rank = 0
    for replacement in card_values.keys():
        new_hand = hand.replace('J', replacement)

        counts = {}
        [counts.update({card: counts.get(card, 0) + 1}) for card in new_hand]

        # Five of a kind
        if 5 in counts.values() or ():
            best_rank = max(best_rank, 7)

        # Four of a kind
        if 4 in counts.values():
            best_rank = max(best_rank, 6)

        # Full house
        if 3 in counts.values() and 2 in counts.values():
            best_rank = max(best_rank, 5)

        # Three of a kind
        if 3 in counts.values() and 2 not in counts.values():
            best_rank = max(best_rank, 4)

        # Two pair
        if list(counts.values()).count(2) == 2:
            best_rank = max(best_rank, 3)

        # One pair
        if 2 in counts.values() and list(counts.values()).count(1) == 3:
            best_rank = max(best_rank, 2)

        # High card
        if list(counts.values()).count(1) == 5:
            best_rank = max(best_rank, 1) 

    return best_rank
    
card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1,
}
    
def compare_same_strength(hands, bids, index=0):
    # Return the hands in order of strength based on the index
    ordered = []
    for key in card_values.keys():
        top_hands = []
        for hand in hands:
            if hand[index] == key:
                top_hands.append(hand)
        if len(top_hands) == 1:
            ordered.append(top_hands[0])
        elif len(top_hands) > 1:
            ordered += compare_same_strength(top_hands, bids, index + 1)
    return ordered
        

def part1(puzzle):
    hand_to_bid = {}
    hands = [line.split()[0] for line in puzzle]
    bids = [line.split()[1] for line in puzzle]
    [hand_to_bid.update({hand: int(bid)}) for hand, bid in zip(hands, bids)]
    hand_strengths = [hand_strength(hand) for hand in hands]
    
    # Order cards by strength and compare equal strength hands
    ranks = []
    for i in range(7, 0, -1):
        top_hands = []
        for j in range(len(hand_strengths)):
            if hand_strengths[j] == i:
                top_hands.append(hands[j])
        if len(top_hands) == 1:
            ranks.append(top_hands[0])
        elif len(top_hands) > 1:
            ranks += compare_same_strength(top_hands, bids)

    total = 0
    for i in range(len(ranks), 0, -1):
        total += hand_to_bid[ranks[-i]] * i

    return total
        

def part2(puzzle):
    hand_to_bid = {}
    hands = [line.split()[0] for line in puzzle]
    bids = [line.split()[1] for line in puzzle]
    [hand_to_bid.update({hand: int(bid)}) for hand, bid in zip(hands, bids)]
    hand_strengths = [hand_strength_2(hand) for hand in hands]
    
    # Order cards by strength and compare equal strength hands
    ranks = []
    for i in range(7, 0, -1):
        top_hands = []
        for j in range(len(hand_strengths)):
            if hand_strengths[j] == i:
                top_hands.append(hands[j])
        if len(top_hands) == 1:
            ranks.append(top_hands[0])
        elif len(top_hands) > 1:
            ranks += compare_same_strength(top_hands, bids)

    total = 0
    for i in range(len(ranks), 0, -1):
        total += hand_to_bid[ranks[-i]] * i

    return total

if __name__ == '__main__':
    day = int(re.findall(r'\d+', __file__)[-1])
    if fetch_input(day):
        TEST = 0
        puzzle = read_input(TEST)
        print(f'Part 1: {part1(puzzle)}')
        print(f'Part 2: {part2(puzzle)}')