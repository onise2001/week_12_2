from django.shortcuts import render, redirect
from .models import Note

# Create your views here.

def index(request):

    notes = Note.objects.all()
    context = {
        "notes": notes
    }
    return render(request, "notes/index.html", context)


def add_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        date = request.POST.get("date")
        note = Note(title=title, content=content, date=date)
        note.save()

    return render(request, "notes/add_note.html")



def show_note(request, id):
    note = Note.objects.filter(pk=id)
    print(note)
    context = {
        "note": note[0]
    }
    return render(request, "notes/note.html", context)



def delete_note(request, id):
    note = Note.objects.filter(pk=id)
    note.delete()
    return redirect(index)