from collections import defaultdict
import random
from typing import List, Dict

class BigramModel:
    def __init__(self, corpus: List[str]):
        self.bigram_counts: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
        for line in corpus:
            tokens = [t.strip().lower() for t in line.split() if t.strip()]
            for a, b in zip(tokens, tokens[1:]):
                self.bigram_counts[a][b] += 1

    def next_word(self, current: str) -> str:
        current = current.lower()
        candidates = self.bigram_counts.get(current, {})
        if not candidates:
            return current
        words = list(candidates.keys())
        weights = list(candidates.values())
        return random.choices(words, weights=weights, k=1)[0]

    def generate_text(self, start_word: str, length: int) -> str:
        if length <= 1:
            return start_word
        seq = [start_word]
        cur = start_word
        for _ in range(length - 1):
            cur = self.next_word(cur)
            seq.append(cur)
        return " ".join(seq)
