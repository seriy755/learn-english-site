import linecache
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.cache import cache
from .works import get, get_all, write, edit, delete


VOCABULARY_CSV = "./data/vocabulary.csv"
EDUCATION_MATERIALS_CSV = "./data/educational_materials.csv"


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def vocabulary(request):
    if request.method == "POST":
        pk = int(request.POST.get("edit"))
        word = request.POST.get("word")
        translation = request.POST.get("translation")
        comment = request.POST.get("comment", "").rstrip()
        new_line = (";").join([word, translation, comment])
        edit(VOCABULARY_CSV, pk, new_line)
        linecache.clearcache()
    search = request.GET.get("search")
    if search is not None:
        words_list = get(VOCABULARY_CSV, search)
    else:
        words_list = get_all(VOCABULARY_CSV)
    return render(request, "vocabulary.html", context={"data": words_list})


def education_materials(request):
    if request.method == "POST":
        pk = int(request.POST.get("edit"))
        materials = {"lesson": "Урок",
                     "literature": "Литература",
                     "audio": "Аудиоматериал",
                     "video": "Видеоматериал"}
        material = materials[request.POST.get("dselect-material")]
        link = request.POST.get("link")
        description = request.POST.get("description")
        new_line = (";").join([material, link, description]).rstrip()
        edit(EDUCATION_MATERIALS_CSV, pk, new_line)
        linecache.clearcache()
    educate_list = get_all(EDUCATION_MATERIALS_CSV)
    return render(request, "educational_materials.html", context={"data": educate_list})


def cards(request, current=None):
    cards_list = get_all(VOCABULARY_CSV)
    num_cards = len(cards_list)
    if current == None:
        card = cards_list[0]  
    else:
        card = cards_list[current-1]
    context = {"cur_card": card[0],
               "prev_card": card[0] - 1  if card[0] > 1 else None,
               "next_card": card[0] + 1 if card[0] < num_cards else None,
               "front": card[2],
               "back": card[3],
               "num_cards": num_cards}
    return render(request, "cards.html", context)


def word_add(request):
    return render(request, "word_add.html")


def word_edit(request, pk):
    line = linecache.getline(VOCABULARY_CSV, pk + 1)
    word, translation, comment = line.split(";")
    context = {"pk": pk,
               "word": word,
               "translation": translation,
               "comment": comment}
    return render(request, "word_edit.html", context)


def word_del(request, pk):
    delete(VOCABULARY_CSV, pk)
    next = request.GET.get("next")
    return HttpResponseRedirect(next)


def material_add(request):
    return render(request, "material_add.html")


def material_edit(request, pk):
    line = linecache.getline(EDUCATION_MATERIALS_CSV, pk + 1)
    material, link, description = line.split(";")
    context = {"pk": pk,
               "material": material,
               "link": link,
               "description": description}
    return render(request, "material_edit.html", context)


def material_del(request, pk):
    delete(EDUCATION_MATERIALS_CSV, pk)
    next = request.GET.get("next")
    return HttpResponseRedirect(next)


def send_word(request):
    if request.method == "POST":
        cache.clear()
        new_word = request.POST.get("new_word")
        new_translation = request.POST.get("new_translation")
        comment = request.POST.get("new_comment", "").rstrip()
        context = {}
        if len(new_word) == 0:
            context["success"] = False
            context["comment"] = "Вы не ввели изученное слово!"
        elif len(new_translation) == 0:
            context["success"] = False
            context["comment"] = "Вы не ввели перевод!"
        else:
            context["success"] = True
            context["comment"] = "Слово добавлено в словарь!"
            write(VOCABULARY_CSV, [new_word, new_translation, comment])
        return render(request, "word_request.html", context)
    else:
        word_add(request)


def send_material(request):
    if request.method == "POST":
        cache.clear()
        materials = {"lesson": "Урок",
                     "literature": "Литература",
                     "audio": "Аудиоматериал",
                     "video": "Видеоматериал"}
        new_material = materials[request.POST.get("dselect-material")]
        new_link = request.POST.get("new_link")
        new_description = request.POST.get("new_description").rstrip()
        context = {}
        if len(new_link) == 0:
            context["success"] = False
            context["comment"] = "Вы не оставили ссылку на учебный материал!"
        elif len(new_description) == 0:
            context["success"] = False
            context["comment"] = "Вы не оставили описание учебного материала!"
        else:
            context["success"] = True
            context["comment"] = "Учебный материал добавлен!"
            write(EDUCATION_MATERIALS_CSV, [new_material, new_link, new_description])
        return render(request, "material_request.html", context)
    else:
        material_add(request)
