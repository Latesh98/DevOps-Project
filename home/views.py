from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

'''
In Django, context is a way to send data from your views (Python functions or classes) to your templates (HTML files). It acts like a "bag of information" that holds all the variables and data you want to display on a webpage.

Here's a simple breakdown:

What is context?

It’s a dictionary (a key-value pair in Python) that contains data.
Keys are the variable names you'll use in the template, and values are the actual data.
Why is it needed?

To display dynamic content in templates (instead of hardcoding values).
For example, showing a user's name, a list of products, or the current date.
'''

def home(request):
    people=[
        {'name':'John', 'age':30},
        {'name':'Anna', 'age':25},
        {'name':'Peter', 'age':40}
    ]

    sendtext= """Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui repellendus, ab veniam fuga nisi sapiente quae voluptatibus iste eius alias nemo praesentium maiores explicabo consequatur fugiat. Fugiat quis, cum ea deleniti laboriosam, esse nihil voluptate inventore repellat fugit error! Similique eos consectetur corporis. Similique."""



    return render(request,"index.html",context={'peoples':people,'sendtext':sendtext})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")