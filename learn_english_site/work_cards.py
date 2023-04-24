from .words_work import get_words


class Card():
    def __init__(self, cnt, question, answer):
        self.cnt = cnt
        self.question = question
        self.answer = answer
        
        self.show_question = True
        self.show_answer = False
    
    def show(self):
        if self.show_question == True:
            self.show_question = False
            self.show_answer = True
        else:
            self.show_question = True
            self.show_answer = False
    
    def __str__(self):
        if self.show_question:
            return self.question
        else:
            return self.answer


def get_cards():
    cards = []
    words = get_words()
    for i, word in enumerate(words):
        cards.append(Card(word[0], word[1], word[2]))
    return cards