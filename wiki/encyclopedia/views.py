from django.shortcuts import render
from django.shortcuts import redirect
from . import util
import markdown2
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        # Try to find case-insensitive match
        entries = util.list_entries()
        for entry in entries:
            if entry.lower() == title.lower():
                content = util.get_entry(entry)
                title = entry  # Use the correct case
                break
        
        if content is None:
            return render(request, "encyclopedia/error.html", {
                "message": "Page not found!"
            })
    
    html_content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })

def search(request):
    query = request.GET.get("q")
    if not query:
        return redirect("index")
        
    entries = util.list_entries()
    
    # First check for exact match (case-insensitive)
    for entry in entries:
        if entry.lower() == query.lower():
            return redirect("entry", title=entry)
    
    # If no exact match, find substring matches
    results = [entry for entry in entries if query.lower() in entry.lower()]
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": results
    })
        
def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        
        if not title:
            return render(request, "encyclopedia/error.html", {
                "message": "Title cannot be empty."
            })
        
        if not content:
            return render(request, "encyclopedia/error.html", {
                "message": "Content cannot be empty."
            })
        
        # Check for existing entry (case-insensitive)
        entries = util.list_entries()
        for entry in entries:
            if entry.lower() == title.lower():
                return render(request, "encyclopedia/error.html", {
                    "message": f"A page with the title '{entry}' already exists."
                })
        
        util.save_entry(title, content)
        return redirect("entry", title=title)
    
    return render(request, "encyclopedia/new.html")

def edit_page(request, title):
    if request.method == "POST":
        content = request.POST.get("content", "").strip()
        
        if not content:
            return render(request, "encyclopedia/error.html", {
                "message": "Content cannot be empty."
            })
            
        util.save_entry(title, content)
        return redirect("entry", title=title)
    
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page not found!"
        })
        
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })
    
def random_page(request):
    entries = util.list_entries()
    if not entries:
        return render(request, "encyclopedia/error.html", {
            "message": "No pages available."
        })
    
    random_entry = random.choice(entries)
    return redirect("entry", title=random_entry)