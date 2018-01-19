from django.shortcuts import render


def students(request):
    name = "Andrew"
    friends = ["a", "b", "c"]
    return render(request, 'students.html', {"name": name, "friends": friends})