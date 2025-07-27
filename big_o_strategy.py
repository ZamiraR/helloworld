"""Simple heuristics for Big O (five-card Omaha hi/lo) strategy."""

from collections import Counter

RANKS = "23456789TJQKA"
SUITS = "shdc"


def parse_card(card):
    """Parse a card string like 'As' into (rank_index, suit)."""
    if len(card) != 2 or card[0] not in RANKS or card[1] not in SUITS:
        raise ValueError(f"Invalid card: {card}")
    return RANKS.index(card[0]), card[1]


def evaluate_hand(hole_cards):
    """Return a rating from 1 (weak) to 10 (strong) for a Big O starting hand."""
    if len(hole_cards) != 5:
        raise ValueError("Big O uses exactly five hole cards")

    ranks = [parse_card(c)[0] for c in hole_cards]
    suits = [parse_card(c)[1] for c in hole_cards]

    rating = 1

    # Pairs and sets
    rank_counts = Counter(ranks)
    if 4 in rank_counts.values():
        rating += 5  # four of a kind
    elif 3 in rank_counts.values() and 2 in rank_counts.values():
        rating += 4  # full house
    elif 3 in rank_counts.values():
        rating += 3
    elif list(rank_counts.values()).count(2) == 2:
        rating += 3  # two pair
    elif 2 in rank_counts.values():
        rating += 2

    # Double suited bonus
    suit_counts = Counter(suits)
    if list(suit_counts.values()).count(2) >= 2:
        rating += 2
    elif max(suit_counts.values()) >= 4:
        rating += 1

    # Low potential (A-5)
    low_ranks = {RANKS.index(r) for r in "A2345"}
    if sum(1 for r in ranks if r in low_ranks) >= 3:
        rating += 2

    return min(rating, 10)


def preflop_action(hole_cards):
    """Suggest preflop action based on hand strength."""
    rating = evaluate_hand(hole_cards)
    if rating >= 8:
        return "raise"
    if rating >= 5:
        return "call"
    return "fold"


if __name__ == "__main__":
    sample_hand = ["As", "Kd", "Qc", "Jh", "2s"]
    print(f"Hand: {sample_hand}")
    print("Rating:", evaluate_hand(sample_hand))
    print("Suggested action:", preflop_action(sample_hand))
