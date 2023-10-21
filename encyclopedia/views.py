from django.shortcuts import render
from . import util
import markdown
import random



def md_to_html(title):
    content =util.get_entry(title)
    markdowner = markdown.Markdown()
    if content is not None:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def Entry(request,title):
    html_content=md_to_html(title)
    if html_content is not None:
        return render(request,"encyclopedia/entry.html",
                {
                    'title':title,
                    'content':html_content

                })
    else:
        return render(request,'encyclopedia/error.html',{
            'message':'Entry not found'
        })

def Search(request):
    if request.method == 'POST':
        search_name = request.POST['q']
        html_content=md_to_html(search_name)
        if html_content is not None:
            return render(request,"encyclopedia/entry.html",
                {
                    'title':search_name,
                    'content':html_content

                })
        else:
            List_Entries = util.list_entries()
            search_item =[]
            for Entry in List_Entries:
                if search_name.lower() in Entry.lower(): 
                    search_item.append(Entry)
            return render(request,'encyclopedia/search.html',{
                'search_item':search_item,
                })
def NewEntryPage(request):
        if request.method=='POST':
            new_title = request.POST['t']
            new_cont = request.POST['Content']
            t_exist = util.get_entry(new_title)
            if t_exist is not None:
                return render(request,'encyclopedia/error.html',
                { 'message':'Entry already exist'})
            else:
                util.save_entry(new_title,new_cont)
                html_content=md_to_html(new_title)
                return render(request,'encyclopedia/entry.html',
                {'title':new_title,
                'content':html_content
                })
        else:
            return render(request,'encyclopedia/new_entry_page.html')

def EditEntry(request):
    if request.method=='POST':
        title = request.POST['edit']
        content= util.get_entry(title)
        return render(request,'encyclopedia/edit_entry.html',{
            'title':title,
            'content': content
        })

def EditSave(request):
    if request.method=='POST':
        title=request.POST['t']
        content = request.POST['Content']
        util.save_entry(title,content)
        html_content=md_to_html(title)
        return render(request,'encyclopedia/entry.html',
                {'title':title,
                'content':html_content
                })


def RandomPage(request):
   all_list =util.list_entries()
   t= random.choice(all_list)
   html_content=md_to_html(t)
   return render(request,'encyclopedia/random.html',{
    'title':t,
    'content':html_content
    })