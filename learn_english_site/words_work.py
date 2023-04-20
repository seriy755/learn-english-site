VOCABULARY_CSV = "./data/vocabulary.csv"

def get_words_for_table():
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


# def get_terms_stats():
#     db_terms = 0
#     user_terms = 0
#     defin_len = []
#     with open(VOCABULARY_CSV, "r", encoding="utf-8") as f:
#         for line in f.readlines()[1:]:
#             term, defin, added_by = line.split(";")
#             words = defin.split()
#             defin_len.append(len(words))
#             if "user" in added_by:
#                 user_terms += 1
#             elif "db" in added_by:
#                 db_terms += 1
#     stats = {
#         "terms_all": db_terms + user_terms,
#         "terms_own": db_terms,
#         "terms_added": user_terms,
#         "words_avg": sum(defin_len)/len(defin_len),
#         "words_max": max(defin_len),
#         "words_min": min(defin_len)
#     }
#     return stats