from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

class Search(forms.Form):
    search = forms.CharField(label="Search Encyclopedia")

class NewPageForm(forms.Form):
    title = forms.CharField()
    new_entry = forms.CharField(widget=forms.Textarea)
    
class EditPage(forms.Form):
    title = forms.CharField()
    new_entry = forms.CharField(widget=forms.Textarea)

def index(request):
    if request.method == "GET":
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "form": Search()
        })
    else:
        search = Search(request.POST)
        related = []

        if search.is_valid():
            searched_entry = search.cleaned_data["search"]

            for entry in util.list_entries():
                if searched_entry.lower() == entry.lower():
                    return render(request, "encyclopedia/entry.html", {
                        "entry": util.get_entry(entry),
                        "title": entry.capitalize(),
                        "form": Search()
                    })
                elif searched_entry.lower() in entry.lower():
                    related.append(entry)

            return render(request, "encyclopedia/related.html", {
                "related": related,
                "searched_entry": searched_entry,
                "title": entry.capitalize(),
                "form": Search()
            })

def get_page(request, entry):
    if request.method == "GET":
        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry(entry),
            "title": entry.capitalize(),
            "form": Search()
        })
    # else:
    #   this is where we'll put logic for submitting the new edited text

    

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html", {
            "new_entry_form": NewPageForm(),
            "form": Search()
        })

    else:
        new_post = NewPageForm(request.POST)

        if new_post.is_valid():
            title = new_post.cleaned_data["title"]
            title = title.capitalize()
            content = new_post.cleaned_data["new_entry"]

            if title.capitalize() in util.list_entries():
                return render(request, "encyclopedia/page_exists.html", {
                    "title": title,
                    "form": Search()
                })

            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("wiki:page_entry", args={title}))

def edit_page(request, entry):
    if request.method == "GET":
        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry(entry),
            "title": entry.capitalize(),
            "form": Search(),
            "edit_page_form": EditPage()
        })
    


