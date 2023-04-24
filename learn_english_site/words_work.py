VOCABULARY_CSV = "./data/vocabulary.csv"


def get_words():
    words = []
    with open(VOCABULARY_CSV, "r", encoding="utf-8") as f:
        for cnt, line in enumerate(f.readlines()[1:]):
            word, translation, comment = line.split(";")
            words.append([cnt + 1, word, translation, comment])
    return words


def write_word(new_word, new_translation, new_comment):
    new_word_line = f"{new_word};{new_translation};{new_comment}"
    with open(VOCABULARY_CSV, "r", encoding="utf-8") as f:
        existing_words = [l.strip("\n") for l in f.readlines()]
        title = existing_words[0]
        old_words = existing_words[1:]
    words_sorted = old_words + [new_word_line]
    words_sorted.sort()
    new_words = [title] + words_sorted
    with open(VOCABULARY_CSV, "w", encoding="utf-8") as f:
        f.write("\n".join(new_words))
