from django.shortcuts import render
from django.core.cache import cache
from .words_work import get_words, write_word
from .work_cards import get_cards

cards_list = get_cards()

def index(request):
    return render(request, "index.html")


def vocabulary(request):
    words_list = get_words()
    return render(request, "vocabulary.html", context={"data": words_list})


def word_add(request):
    return render(request, "word_add.html")


def send_word(request):
    if request.method == "POST":
        cache.clear()
        new_word = request.POST.get("new_word")
        new_translation = request.POST.get("new_translation")
        comment = request.POST.get("new_comment", "")
        context = {}
        if len(new_word) == 0:
            context["success"] = False
            context["comment"] = "Вы не ввели изученное слово!"
        elif len(new_translation) == 0:
            context["success"] = False
            context["comment"] = "Вы не ввели перевод!"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            write_word(new_word, new_translation, comment)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "word_request.html", context)
    else:
        word_add(request)


def cards(request):
    cards_list = get_cards()
    return render(request, "cards.html", context={"data": cards_list})


def show_translate(request, cnt):
    for card in cards_list:
        if cnt == card.cnt:
            card.show()
    return render(request, "cards.html", context={"data": cards_list})
