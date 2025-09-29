from functools import lru_cache
import spacy
from typing import List

@lru_cache(maxsize=1)
def get_nlp():
    return spacy.load("en_core_web_md")

def embed_word(word: str) -> List[float]:
    nlp = get_nlp()
    return nlp(word).vector.tolist()
