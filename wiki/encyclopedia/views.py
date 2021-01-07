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

def index(request):
    if request.method == "GET":
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "form": Search()
        })
    else:
        search = Search(request.POST)

        if search.is_valid():
            searched_entry = search.cleaned_data["search"]

            for entry in util.list_entries():
                if searched_entry.lower() == entry.lower():
                    return HttpResponseRedirect(searched_entry)
                elif searched_entry.lower() in entry.lower():
                    return render(request, "encyclopedia/related.html", {
                        "entry": entry,
                        "title": entry.capitalize(),
                        "form": Search()
                    })
            return render(request, "encyclopedia/related.html", {
                "searched_entry": searched_entry
            })

def get_page(request, entry):
    return render(request, "encyclopedia/wiki/entry.html", {
        "entry": util.get_entry(entry),
        "title": entry.capitalize(),
        "form": Search()
    })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html", {
            "new_entry_form": NewPageForm(),
            "form": Search()
        })

