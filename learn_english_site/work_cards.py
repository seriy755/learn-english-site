from .words_work import get_words


def get_cards():
    cards = []
    words = get_words()
    for word in words:
        card = {"id": word[0], 
                "front": word[1],
                "back": word[2],
                "comment": word[3]}
        cards.append(card)
    return cards