from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_page(request, entry):
    return render(request, f"encyclopedia/{entry}.html", {
        "entry": util.get_entry(entry)
    })

