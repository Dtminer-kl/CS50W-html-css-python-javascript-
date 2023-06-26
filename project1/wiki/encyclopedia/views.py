from django.shortcuts import render
from django.http import HttpResponseRedirect
from markdown import markdown
import random

from . import util

def convert(title):
    content = util.get_entry(title)
    if content == None:
        return None
    else:
        return markdown(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    converted = convert(title)
    if converted == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This entry does not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title" : title,
            "entry": converted
        })

def search(request):
    if request.method == "POST":
        entrySearch = request.POST['q']
        converted =convert(entrySearch)
        if converted is not None:
            return render(request, "encyclopedia/entry.html", {
            "title" : entrySearch,
            "entry": converted
            })
        else:
            all = util.list_entries()
            recommendation= []
            for entry in all:
                if entrySearch.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html",{
                "recommendation" :recommendation
            })
        
def newPage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        if request.method == "POST":
            title = request.POST['title']
            content = request.POST['content']
            all = util.get_entry(title)
            if all is not None:
                return render(request, "encyclopedia/error.html",{
                    "message": "Page already exits"
                })
            else:
                util.save_entry(title, content)
                converted =convert(title)
                return render(request, "encyclopedia/entry.html", {
                    "title" : title,
                    "entry": converted
                })

def editPage(request):
    if request.method == "POST":
        title = request.POST['entryTitle']
        content = util.get_entry(title)
        return render(request, "encyclopedia/editpage.html",{
            "title": title,
            "entry": content
        })
    
def savePage(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        converted = convert(title)
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "title" : title,
            "entry": converted
        })
    
def rand(request):
    all = util.list_entries()
    rand = random.choice(all)
    converted = convert(rand)
    return render(request, "encyclopedia/entry.html", {
            "title" : random,
            "entry": converted
        })

       
